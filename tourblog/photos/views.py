from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo, Comment
from .forms import PhotoForm, CommentForm


def photo_list(request):
    photo_qs = Photo.objects.all().prefetch_related('photo_comment_set').select_related('author')
    return render(request, 'photos/list.html', {
        'photo_list': photo_qs,
    })


def photo_detail(request, pk):
    photo = get_object_or_404(Photo.objects.select_related('author').prefetch_related('photo_comment_set'), id=pk)
    comment_set = Comment.objects.filter(author=photo.author).select_related('author')
    return render(request, 'photos/detail.html', {
        'photo': photo,
        'comment_set': comment_set
    })


def photo_new(request):
    
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            photo = form.save(commit=False)
            photo.author = request.user
            photo.save()
            return redirect(photo)
    else:
        form = PhotoForm()

    return render(request, 'photos/photo_form.html', {
        'form': form,
    })


def photo_edit(request, pk):
    photo = get_object_or_404(Photo, id=pk)
    
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)

        if form.is_valid():
            photo = form.save(commit=False) 
            photo.author = request.user
            photo.save()
            return redirect(photo)
    else:
        form = PhotoForm(instance=photo)

    return render(request, 'photos/photo_form.html', {
        'form': form,
    })


def photo_delete(request, pk):
    photo = get_object_or_404(Photo, id=pk)

    if request.method == 'POST':
        photo.delete()
        return redirect('photos:photo_list')
    else:
        return render(request, 'photos/delete_confirm.html', {
            'photo': photo,
        })

        
def new_comment(equest, pk):
    photo = get_object_or_404(Photo, id=pk)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.photo = photo
            comment.save()
            return redirect(photo)

    else:
        form = CommentForm()

    return render(request, 'photos/comment_form.html', {
        'form': form,
    })
