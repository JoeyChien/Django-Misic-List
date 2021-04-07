from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(
        widget = forms.PasswordInput
    )
    password2 = forms.CharField(
        widget = forms.PasswordInput
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact = username)
        if qs.exists():
            raise forms.ValidationError("使用者名稱重複")
        return username

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget = forms.PasswordInput
    )

    def clean(self):
        username = self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact = username)
        if not qs.exists():
            raise forms.ValidationError("使用者不存在")
        return username
