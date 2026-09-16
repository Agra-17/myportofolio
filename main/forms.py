from django.forms import DateInput, ModelForm, Select, TextInput, Textarea, URLInput

from main.models import Achievement

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