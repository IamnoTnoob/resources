from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='<b>Username</b>',
        help_text='<b>Username digunakan pada saat login</b>'
    )
    email = forms.EmailField(
        label='<b>Email</b>',
        max_length=100,
        help_text='<b>Gunakan email bisnis anda.</b>'
    )
    password1 = forms.CharField(
        label='<b>Password</b>',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='<b>Use Secure Password!</b>'
    )
    password2 = forms.CharField(
        label='<b>Konfirmasi Password</b>',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        help_text='<b>Samakan dengan password di atas</b>',
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    phone = forms.NumberInput()

    class Meta:
        model = Profile
        fields = ['my_photo', 'phone']
