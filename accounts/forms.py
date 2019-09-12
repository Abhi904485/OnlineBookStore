from PIL import Image
from django import forms
from django.contrib.auth import get_user_model

from accounts.models import Profile

User = get_user_model()


class GeneralForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
                               required=True,
                               error_messages={'required': "please enter the username"}, )

    password = forms.CharField(label="Password", widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
                               required=True,
                               error_messages={'required': "please enter the password"}, )


class LoginForm(GeneralForm):
    pass


class RegisterForm(GeneralForm):
    password1 = forms.CharField(label="Confirm password", error_messages={'required': "please enter the password"},
                                widget=forms.PasswordInput(
                                        attrs={'class': 'form-group', 'placeholder': 'Renter your password'}),
                                required=True,
                                )

    first_name = forms.CharField(label="First Name", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
                                 required=True,
                                 error_messages={'required': "please enter the first name"}, )

    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
                                required=True,
                                error_messages={'required': "please enter the last name"}, )

    email = forms.EmailField(label="Email", widget=forms.EmailInput(
            attrs={'class': 'form-group', 'placeholder': 'Enter your mail'}),
                             required=True,
                             error_messages={'required': "please enter the mail"}, )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username.lower()).exists():
            raise forms.ValidationError("User Already Exists!")
        return username.lower()

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email.lower()).exists():
            raise forms.ValidationError("Email  Already Exists!")
        return email.lower()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.lower()

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name.lower()

    def clean(self):
        data = self.cleaned_data
        if data:
            password = data['password']
            password1 = data['password1']
            if password != password1:
                raise forms.ValidationError("Password should match!")
            return data


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': "form-row", 'id': "first_name", 'placeholder': "Enter First name",
                   'name': "first_name"}), )
    last_name = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': "form-row", 'id': "last_name", 'placeholder': "Enter Last name",
                   'name': "last_name"}))
    username = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': "form-row", 'id': "username", 'placeholder': "Enter username",
                   'name': "username"}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
            attrs={'class': "form-row", 'id': "email", 'placeholder': "Enter email",
                   'name': "email"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class ProfileUpdateFrom(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        labels = {
                'image': "Upload Profile Picture"
        }

    def save(self, commit=True):
        super().save()
        img = Image.open(self.instance.image.path)
        if img.height > 300 and img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.instance.image.path)
