import datetime
from hashlib import md5

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .models import UserProfile, Session

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username',)
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(
            required=True,
            widget=forms.PasswordInput()
            )
    next = forms.CharField(
            required=False,
            widget=forms.HiddenInput()
            )


    def clean_email(self):
        email = self.cleaned_data['email']
        if UserProfile.profiles.exists(email=email):
            raise forms.ValidationError(
                    "This email address is already registered"
                    )
        return email

    def save(self, *args, **kwargs):
        username = self.cleaned_data['username']
        # TODO: Consider using the slug mixin to create a username
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

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(
            required=True,
            widget=forms.PasswordInput()
            )
    next = forms.CharField(
            required=False,
            widget=forms.HiddenInput()
            )

    def clean(self, *args, **kwargs):
        data = super(LoginForm, self).clean(*args, **kwargs)
        user = User.objects.filter(email=data['email'])
        if not user.exists():
            raise forms.ValidationError(
                    "No user with this email address is registered"
                    )
        auth_user = authenticate(
                username=user[0].username,
                password=data['password']
                )
        if not auth_user:
            raise forms.ValidationError(
                    "Wrong password"
                    )
        self.user = auth_user
        return data

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = (
                'title',
                'description',
                )
