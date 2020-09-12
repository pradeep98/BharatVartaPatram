from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2' ]
    
    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='User Name')
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    firstname = forms.CharField(label='First Name')
    lastname = forms.CharField(label='Last Name')
    city = forms.CharField(label='City')
    occupation = forms.CharField(label='Occupation')
    image = forms.ImageField(label='Profile Pic')

    class Meta:
        model = Profile
        fields = ['firstname','lastname','city', 'occupation', 'image']