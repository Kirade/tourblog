from django.shortcuts import render, redirect
from .forms import SignUpForm


def signup(request):
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignUpForm()

    return render(request, 'accounts/account_form.html', {
        'form': form,
    })
