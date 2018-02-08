from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignUpForm(UserCreationForm):

    address = forms.CharField()
    phone_number = forms.CharField()

    def save(self):
        user = super().save()
        profile = Profile.objects.create(user=user,
                address=self.cleaned_data['address'],
                phone_number=self.cleaned_data['phone_number'])
        profile.save()
