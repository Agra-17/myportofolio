from django.forms import DateInput, ModelForm, Select, TextInput, Textarea, URLInput

from main.models import Achievement, Experience

class AchievementForm(ModelForm):
    class Meta:
        model = Achievement
        fields = [
            "title",
            "description",
            "scale",
            "date_achieved",
            "issuer",
        ]

        labels = {
            "title": "Nama Achievement",
            "description": "Deskripsi Achievement",
            "scale": "Skala Lomba",
            "date_achieved": "Tanggal Peraihan",
            "issuer": "Nama Penyelenggara",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Nama Achievement",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Acievementsmu",
                    "rows": 3,
                }
            ),
            "scale": Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "date_achieved": DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "issuer": TextInput(
                attrs={
                    "placeholder": "Nama Penyelenggara",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            "started_at",
            "ended_at"
        ]

        labels = {
            "title": "Nama Experience",
            "description": "Deskripsi Experience",
            "thumbnail": "URL Gambar Experience",
            "started_at": "Tanggal Mulai",
            "ended_at" : "Tanggal selesai"
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Nama Experience",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Experiencemu",
                    "rows": 3,
                }
            ),
            "thumbnail": Textarea(
                attrs={
                    
                    "placeholder": "https://drive.google.com/thumbnail?id=1gmPT5o1wBoplW1TbYqbP0h6J68SVvkqI&sz=w1000",
                }
            ),
            "category": Select(
                attrs={
                    "class": "form-select",
                }
            ),
            "started_at": DateInput(
                attrs={
                    "type": "date",
                }
            ),
            "ended_at": TextInput(
                attrs={
                    "type": "date",
                }
            ),
        }