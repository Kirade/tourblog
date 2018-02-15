from django.shortcuts import render


def column_list(request):
    column_qs = Column.objects.all().prefetch_related('tag_set', 'column_comment_set').select_related('author')
    return render(request, 'column/list.html', {
        'column_list': column_qs,
    }
