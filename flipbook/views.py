from django.shortcuts import render, redirect

from setup import settings
from .forms import PhotoForm
from .models import Photo
from reportlab.pdfgen import canvas
import os


def upload(request):
    if request.method == 'POST':
        files = request.FILES.getlist('images')  # Pega a lista de arquivos enviados
        for file in files:
            photo = Photo(image=file)
            photo.save()  # Salva cada foto individualmente
        return redirect('gallery')
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {'form': form})
def gallery(request):
    photos = Photo.objects.all()
    return render(request, 'galeria.html', {'photos': photos})

def create_flipbook(request):
    photos = Photo.objects.all()  # Supondo que você tenha um modelo Photo para suas imagens
    c = canvas.Canvas("flipbook.pdf")
    for photo in photos:
        image_path = os.path.join(settings.MEDIA_ROOT, photo.image.name)
        c.drawImage(image_path, 100, 750, width=400, preserveAspectRatio=True, mask='auto')
        c.showPage()
    c.save()
    return render(request, 'flipbook_created.html')

