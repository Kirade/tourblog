from django.shortcuts import render, get_object_or_404
from .models import Photo


def photo_list(request):
    photo_qs = Photo.objects.all().prefetch_related('photo_comment_set').select_related('author')
    return render(request, 'photos/list.html', {
        'photo_list': photo_qs,
    })


def photo_detail(request, pk):
    photo = get_object_or_404(Photo.objects.select_related('author'), id=pk)
    return render(request, 'photos/detail.html', {
        'photo': photo,
    })
