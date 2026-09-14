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
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "In progress")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Completed")
        self.assertNotContains(response, "In progress")

class AchievementTestCase(TestCase):

    def setUp(self):
        # URL untuk halaman achievement, diambil lewat named route
        self.achievement_url = reverse('main:show_achievements')

    # 1. URL dapat diakses dan menggunakan template yang tepat
    def test_achievement_url_accessible_and_uses_correct_template(self):
        response = self.client.get(self.achievement_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'achievements.html')

    # 2. Data model muncul di halaman HTML ketika ada data
    def test_achievement_data_appears_when_data_exists(self):
        Achievement.objects.create(
            title='Juara 1 Hackathon Nasional',
            description='Memenangkan hackathon tingkat nasional bidang AI',
            issuer='Kominfo',
            date_achieved=date(2026, 3, 15)
        )
        response = self.client.get(self.achievement_url)
        self.assertContains(response, 'Juara 1 Hackathon Nasional')
        self.assertContains(response, 'Kominfo')

    # 3. Halaman HTML menampilkan pesan kondisi kosong ketika belum ada data
    def test_empty_message_shown_when_no_data(self):
        response = self.client.get(self.achievement_url)
        self.assertContains(response, 'Belum ada achievement yang ditambahkan.')