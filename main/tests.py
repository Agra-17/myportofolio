from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from datetime import date

from main.models import Experience
from main.models import Achievement


class MainTest(TestCase):
    # test untuk experience
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, reverse("api:experience-list"))
        self.assertContains(response, "fetchExperiences(searchInput.value.trim())")
        self.assertContains(response, "buildExperienceCardElement")
        self.assertNotContains(response, "experience-page-submit")
        data = self.client.get(reverse("api:experience-list")).json()
        self.assertEqual(data[0]["title"], self.experience.title)
        self.assertEqual(data[0]["description"], self.experience.description)
        self.assertEqual(data[0]["category_display"], "Part-Time")
        self.assertTrue(data[0]["is_ongoing"])
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_experience_list_script_available_for_each_role(self):
        regular = User.objects.create_user(username="regular-page")
        editor = User.objects.create_user(username="editor-page")
        editor.groups.add(Group.objects.create(name="Editor"))
        owner = User.objects.create_user(username="owner-page", is_superuser=True)
        for user in (None, regular, editor, owner):
            with self.subTest(user=user):
                self.client.logout()
                if user is not None:
                    self.client.force_login(user)
                response = self.client.get(reverse("main:show_experience"))
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, reverse("api:experience-list"))
                self.assertContains(response, "function fetchExperiences")
                self.assertContains(response, "function writeExperience")
                self.assertContains(response, "X-CSRFToken")
                self.assertNotContains(response, "experience-page-submit")
                self.assertIn("csrftoken", response.cookies)

    def test_experience_edit_uses_existing_form_and_patch(self):
        editor = User.objects.create_user(username="editor-edit")
        editor.groups.add(Group.objects.create(name="Editor"))
        owner = User.objects.create_user(username="owner-edit", is_superuser=True)
        regular = User.objects.create_user(username="regular-edit")
        url = reverse("main:update_experience", args=[self.experience.id])
        for user in (editor, owner):
            with self.subTest(user=user):
                self.client.force_login(user)
                response = self.client.get(url)
                self.assertEqual(response.status_code, 200)
                self.assertTemplateUsed(response, "experience_form.html")
                self.assertContains(response, "experience-page-form")
                self.assertContains(response, "'PATCH'")
                self.assertContains(response, reverse("api:experience-detail", args=[self.experience.id]))
                self.assertContains(response, "X-CSRFToken")
        self.client.force_login(regular)
        self.assertEqual(self.client.get(url).status_code, 403)
        self.client.logout()
        self.assertEqual(self.client.get(url).status_code, 302)

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.get(reverse("main:get_experience_json")).json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:get_experience_json"))
        self.assertFalse(self.experience.is_ongoing)
        self.assertFalse(response.json()[0]["fields"]["is_ongoing"])

class AchievementTestCase(TestCase):

    def setUp(self):
        # URL untuk halaman achievement, diambil lewat named route
        self.achievement_url = reverse('main:show_achievements')

    # 1. URL dapat diakses dan menggunakan template yang tepat
    def test_achievement_url_accessible_and_uses_correct_template(self):
        response = self.client.get(self.achievement_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'achievements.html')

    # 2. Halaman memuat data melalui API DRF.
    def test_achievement_data_appears_when_data_exists(self):
        Achievement.objects.create(
            title='Juara 1 Hackathon Nasional',
            description='Memenangkan hackathon tingkat nasional bidang AI',
            issuer='Kominfo',
            date_achieved=date(2026, 3, 15)
        )
        response = self.client.get(self.achievement_url)
        self.assertContains(response, reverse('api:achievement-list'))
        data = self.client.get(reverse('api:achievement-list')).json()
        self.assertEqual(data[0]['title'], 'Juara 1 Hackathon Nasional')
        self.assertEqual(data[0]['issuer'], 'Kominfo')

    # 3. Halaman HTML menampilkan pesan kondisi kosong ketika belum ada data
    def test_empty_message_shown_when_no_data(self):
        response = self.client.get(self.achievement_url)
        self.assertContains(response, 'Belum ada achievement yang ditambahkan atau ditemukan.')
        self.assertEqual(self.client.get(reverse('api:achievement-list')).json(), [])
