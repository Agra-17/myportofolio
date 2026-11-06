import uuid

from django.contrib.auth.models import Group, User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from main.models import Achievement, Experience


class AchievementAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner", password="test-password", email="owner@example.com",
        )
        self.visitor = User.objects.create_user(username="visitor", password="test-password")
        self.achievement = Achievement.objects.create(
            title="National Competition", description="First place",
            scale="national", date_achieved="2026-03-15", issuer="University",
        )
        self.list_url = reverse("api:achievement-list")
        self.detail_url = reverse("api:achievement-detail", args=[self.achievement.id])
        self.star_url = reverse("api:achievement-star", args=[self.achievement.id])
        self.payload = {
            "title": "New achievement", "description": "A competition award",
            "scale": "national", "date_achieved": "2026-04-01", "issuer": "Organizer",
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["id"], str(self.achievement.id))
        self.assertFalse(response.data[0]["is_starred"])
        self.assertNotIn("fields", response.data[0])
        self.assertEqual(self.client.get(self.detail_url).status_code, status.HTTP_200_OK)

    def test_search_and_empty_results(self):
        response = self.client.get(self.list_url, {"title": "NATIONAL"})
        self.assertEqual(len(response.data), 1)
        response = self.client.get(self.list_url, {"title": "not-found"})
        self.assertEqual(response.data, [])

    def test_missing_achievement(self):
        url = reverse("api:achievement-detail", args=[uuid.uuid4()])
        self.assertEqual(self.client.get(url).status_code, status.HTTP_404_NOT_FOUND)

    def test_guest_and_visitor_cannot_write(self):
        for user in (None, self.visitor):
            self.client.force_authenticate(user=user)
            self.assertEqual(self.client.post(self.list_url, self.payload, format="json").status_code, 403)
            self.assertEqual(self.client.patch(self.detail_url, {"title": "Changed"}, format="json").status_code, 403)
            self.assertEqual(self.client.delete(self.detail_url).status_code, 403)
        self.assertEqual(Achievement.objects.count(), 1)
        self.achievement.refresh_from_db()
        self.assertEqual(self.achievement.title, "National Competition")

    def test_owner_can_create(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Achievement.objects.filter(pk=response.data["id"]).exists())

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)
        for changes, field in [
            ({"title": " "}, "title"),
            ({"title": '<img src="x" onerror="alert(1)">'}, "title"),
            ({"date_achieved": "not-a-date"}, "date_achieved"),
            ({"scale": "worldwide"}, "scale"),
        ]:
            response = self.client.post(self.list_url, {**self.payload, **changes}, format="json")
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            self.assertIn(field, response.data)
        self.assertEqual(Achievement.objects.count(), 1)

    def test_patch_put_and_delete(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.patch(self.detail_url, {"title": "Changed"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.achievement.refresh_from_db()
        self.assertEqual(self.achievement.description, "First place")
        response = self.client.put(self.detail_url, {"title": "Incomplete"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        response = self.client.put(self.detail_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.content, b"")
        self.assertFalse(Achievement.objects.filter(pk=self.achievement.id).exists())

    def test_star_requires_login_and_toggles(self):
        self.assertEqual(self.client.post(self.star_url).status_code, status.HTTP_403_FORBIDDEN)
        self.client.force_authenticate(user=self.visitor)
        response = self.client.post(self.star_url)
        self.assertTrue(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 1)
        response = self.client.post(self.star_url)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["star_count"], 0)

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)
        response = self.client.post(self.list_url, {
            **self.payload, "star_count": 99, "is_starred": True,
            "starred_by_names": "forged", "starred_by": [self.visitor.id],
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])

    def test_staff_and_editor_cannot_manage_achievements(self):
        self.visitor.is_staff = True
        self.visitor.save()
        self.visitor.groups.add(Group.objects.create(name="Editor"))
        self.client.force_authenticate(user=self.visitor)
        response = self.client.patch(self.detail_url, {"title": "Changed"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_wrong_method(self):
        self.client.force_authenticate(user=self.owner)
        self.assertEqual(self.client.delete(self.list_url).status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))
        response = client.post(self.list_url, self.payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Achievement.objects.count(), 1)

    def test_session_write_with_csrf_succeeds(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(client.login(username="owner", password="test-password"))
        page = client.get(self.list_url, HTTP_ACCEPT="text/html")
        self.assertEqual(page.status_code, status.HTTP_200_OK)
        token = client.cookies["csrftoken"].value
        response = client.post(
            self.list_url, self.payload, format="json", HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ExperienceAPITest(APITestCase):
    def setUp(self):
        self.owner = User.objects.create_superuser(
            username="owner",
            password="test-password",
            email="owner@example.com",
        )
        self.regular = User.objects.create_user(
            username="regular",
            password="test-password",
        )
        self.editor = User.objects.create_user(
            username="editor",
            password="test-password",
        )
        self.editor.groups.add(
            Group.objects.create(name="Editor")
        )

        self.experience = Experience.objects.create(
            title="Asisten Dosen",
            description="Membantu kegiatan praktikum.",
            category="part-time",
        )

        self.list_url = reverse("api:experience-list")
        self.detail_url = reverse(
            "api:experience-detail",
            args=[self.experience.id],
        )
        self.star_url = reverse(
            "api:experience-star",
            args=[self.experience.id],
        )

        self.payload = {
            "title": "Research Assistant",
            "description": "Membantu penelitian.",
            "category": "research",
            "thumbnail": "",
            "started_at": None,
            "ended_at": None,
        }

    def test_public_list_and_detail(self):
        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.data[0]["id"],
            str(self.experience.id),
        )
        self.assertEqual(
            response.data[0]["category_display"],
            "Part-Time",
        )
        self.assertEqual(response.data[0]["star_count"], 0)
        self.assertFalse(response.data[0]["is_starred"])
        self.assertNotIn("starred_by", response.data[0])

        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "Asisten Dosen")

    def test_search(self):
        response = self.client.get(
            self.list_url,
            {"title": "ASISTEN"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(
            self.list_url,
            {"title": "tidak-ditemukan"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_missing_experience(self):
        url = reverse(
            "api:experience-detail",
            args=[uuid.uuid4()],
        )
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_guest_and_regular_cannot_write(self):
        for user in (None, self.regular):
            self.client.force_authenticate(user=user)

            response = self.client.post(
                self.list_url,
                self.payload,
                format="json",
            )
            self.assertEqual(response.status_code, 403)

            response = self.client.patch(
                self.detail_url,
                {"title": "Diubah tanpa izin"},
                format="json",
            )
            self.assertEqual(response.status_code, 403)

            response = self.client.put(
                self.detail_url,
                self.payload,
                format="json",
            )
            self.assertEqual(response.status_code, 403)

            response = self.client.delete(self.detail_url)
            self.assertEqual(response.status_code, 403)

            self.assertEqual(Experience.objects.count(), 1)
            self.experience.refresh_from_db()
            self.assertEqual(
                self.experience.title,
                "Asisten Dosen",
            )
            self.assertEqual(
                self.experience.description,
                "Membantu kegiatan praktikum.",
            )

    def test_editor_can_update(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.patch(
            self.detail_url,
            {"title": "Asisten Dosen PBP"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)

        self.experience.refresh_from_db()
        self.assertEqual(
            self.experience.title,
            "Asisten Dosen PBP",
        )
        self.assertEqual(
            self.experience.description,
            "Membantu kegiatan praktikum.",
        )

        response = self.client.put(
            self.detail_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 200)

        self.experience.refresh_from_db()
        self.assertEqual(
            self.experience.title,
            "Research Assistant",
        )

    def test_editor_cannot_create_or_delete(self):
        self.client.force_authenticate(user=self.editor)

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 403)

        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Asisten Dosen")
        self.assertEqual(Experience.objects.count(), 1)

    def test_owner_can_create_update_and_delete(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 201)

        created = Experience.objects.get(pk=response.data["id"])
        self.assertEqual(created.title, self.payload["title"])

        response = self.client.patch(
            self.detail_url,
            {"title": "Judul Baru"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)

        self.experience.refresh_from_db()
        self.assertEqual(self.experience.title, "Judul Baru")

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.content, b"")
        self.assertFalse(
            Experience.objects.filter(
                pk=self.experience.id,
            ).exists()
        )

    def test_validation(self):
        self.client.force_authenticate(user=self.owner)

        invalid_inputs = [
            ({"title": "   "}, "title"),
            ({"title": "<b></b>"}, "title"),
            ({"description": "<p></p>"}, "description"),
            ({"category": "invalid"}, "category"),
            ({"thumbnail": "javascript:alert(1)"}, "thumbnail"),
            ({"started_at": "bukan-tanggal"}, "started_at"),
        ]

        for changes, field in invalid_inputs:
            with self.subTest(field=field, changes=changes):
                response = self.client.post(
                    self.list_url,
                    {**self.payload, **changes},
                    format="json",
                )
                self.assertEqual(response.status_code, 400)
                self.assertIn(field, response.data)
                self.assertEqual(Experience.objects.count(), 1)

    def test_html_tags_are_removed(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            {
                **self.payload,
                "title": " <b>Research Assistant</b> ",
                "description": "<p>Membantu penelitian.</p>",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)

        created = Experience.objects.get(pk=response.data["id"])
        self.assertEqual(created.title, "Research Assistant")
        self.assertEqual(
            created.description,
            "Membantu penelitian.",
        )

    def test_star_requires_login_and_toggles(self):
        response = self.client.post(self.star_url)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(self.experience.starred_by.count(), 0)

        for user in (self.regular, self.editor, self.owner):
            with self.subTest(username=user.username):
                self.client.force_authenticate(user=user)

                response = self.client.post(
                    self.star_url,
                    {"user_id": self.owner.id},
                    format="json",
                )
                self.assertEqual(response.status_code, 200)
                self.assertTrue(response.data["is_starred"])
                self.assertEqual(response.data["star_count"], 1)
                self.assertEqual(
                    list(
                        self.experience.starred_by.values_list(
                            "pk",
                            flat=True,
                        )
                    ),
                    [user.pk],
                )

                response = self.client.post(self.star_url)
                self.assertEqual(response.status_code, 200)
                self.assertFalse(response.data["is_starred"])
                self.assertEqual(response.data["star_count"], 0)
                self.assertEqual(
                    self.experience.starred_by.count(),
                    0,
                )

    def test_computed_fields_are_read_only(self):
        self.client.force_authenticate(user=self.owner)

        response = self.client.post(
            self.list_url,
            {
                **self.payload,
                "star_count": 99,
                "is_starred": True,
                "starred_by_names": "forged",
                "starred_by": [self.regular.pk],
                "is_ongoing": False,
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["star_count"], 0)
        self.assertFalse(response.data["is_starred"])
        self.assertEqual(response.data["starred_by_names"], "")
        self.assertTrue(response.data["is_ongoing"])

        created = Experience.objects.get(pk=response.data["id"])
        self.assertEqual(created.starred_by.count(), 0)

    def test_session_write_without_csrf_is_rejected(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(
            client.login(
                username="owner",
                password="test-password",
            )
        )

        response = client.post(
            self.list_url,
            self.payload,
            format="json",
        )
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Experience.objects.count(), 1)

    def test_session_write_with_csrf_succeeds(self):
        client = APIClient(enforce_csrf_checks=True)
        self.assertTrue(
            client.login(
                username="owner",
                password="test-password",
            )
        )

        page = client.get(
            self.list_url,
            HTTP_ACCEPT="text/html",
        )
        self.assertEqual(page.status_code, 200)

        token = client.cookies["csrftoken"].value

        response = client.post(
            self.list_url,
            self.payload,
            format="json",
            HTTP_X_CSRFTOKEN=token,
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Experience.objects.count(), 2)
