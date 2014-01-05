from django import forms
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
