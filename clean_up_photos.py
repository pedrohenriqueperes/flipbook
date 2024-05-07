import os
import django

# Configure o caminho para as configurações do Django.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")
django.setup()

from flipbook.models import Photo  # Verifique se flipbook é o nome correto do seu app
from django.conf import settings

def cleanup_photos():
    photos = Photo.objects.all()
    for photo in photos:
        photo_path = os.path.join(settings.MEDIA_ROOT, str(photo.image))
        if not os.path.exists(photo_path):
            print(f"Deleting missing photo: {photo_path}")
            photo.delete()

if __name__ == '__main__':
    cleanup_photos()
