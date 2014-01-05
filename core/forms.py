import md5
import datetime

from django import forms
from django.contrib.auth.models import User

from .models import UserProfile

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name',)
    email = forms.EmailField(required=True)
    password = forms.CharField(
            required=True,
            widget=forms.PasswordInput()
            )

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserProfile.profiles.exists(email=email):
            raise forms.ValidationError(
                    "This email address is already registered"
                    )
        return email

    def save(self, *args, **kwargs):
        username = md5.new(str(datetime.datetime.now())).hexdigest()
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        user = User.objects.create_user(
                username=username,
                email=email,
                password=password
                )
        profile = super(RegisterForm, self).save(*args, commit=False, **kwargs)
        profile.user = user
        profile.save()
        return profile

class LoginForm(forms.ModelForm):
    pass
