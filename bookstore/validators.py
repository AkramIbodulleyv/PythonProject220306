from django.core.exceptions import ValidationError
import os

def validate_file_type(value):
    # Fayl kengaytmasi olish
    valid_extensions = ['.pdf', '.epub', '.docx']
    ext = os.path.splitext(value.name)[-1].lower()  # Fayl kengaytmasini oladi

    if ext not in valid_extensions:
        raise ValidationError(
            f"Fayl turi ruxsat etilmagan. Faqat quyidagi formatlarga ruxsat beriladi: {', '.join(valid_extensions)}."
        )
