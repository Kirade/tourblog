from django.shortcuts import render
from .models import Photo


def photo_list(request):
    photo_qs = Photo.objects.all()
    return render(request, 'photos/list.html', {
        'photo_list': photo_qs,
    })

