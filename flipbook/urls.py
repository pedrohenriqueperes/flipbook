from django.urls import path
from flipbook.views import *



urlpatterns = [
    path('', upload, name='upload'),
    path('gallery/', gallery, name='gallery'),  # Adicione esta linha
]