import re
import uuid
from urllib.parse import parse_qs, urlparse

from django.db import models
from django.utils import timezone

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(blank=True, null=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title

    @property
    def is_ongoing(self):
        return self.ended_at is None or self.ended_at > timezone.now()

    @property
    def thumbnail_url(self):
        if not self.thumbnail:
            return ""

        parsed_url = urlparse(self.thumbnail)
        if parsed_url.netloc not in {"drive.google.com", "www.drive.google.com"}:
            return self.thumbnail

        file_id = parse_qs(parsed_url.query).get("id", [None])[0]
        if not file_id:
            match = re.search(r"/file/d/([^/]+)", parsed_url.path)
            file_id = match.group(1) if match else None

        if not file_id:
            return self.thumbnail

        return f"https://drive.google.com/thumbnail?id={file_id}&sz=w1000"


class Achievement(models.Model):
    ACHIEVEMENT_SCALE = [
        ('international', 'International'),
        ('national', 'National'),
        ('provincial', 'Provincial'),
        ('district', "District"),
    ] 

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    scale = models.CharField(max_length=20, choices=ACHIEVEMENT_SCALE, default='national')
    date_achieved = models.DateField()
    issuer = models.CharField(max_length=255)

    def __str__(self):
        return self.title
        