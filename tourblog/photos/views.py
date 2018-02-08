from django.shortcuts import render


def photo_list(request):
    return render(request, 'photos/list.html')
