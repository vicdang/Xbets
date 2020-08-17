from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from bets.models import UserProfile


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class':'form-control','placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

class SignUpForm(UserCreationForm):
    # declare the fields you will show
    username = forms.EmailField(
        label="Username",
        help_text="Username should be your email address.",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder': 'Username@example.com'}))
    first_name = forms.CharField(
        label="First Name",
        widget=forms.TextInput(
            attrs={
                'autofocus': 'autofocus',
                'class':'form-control',
                'placeholder': 'First Name'}))
    last_name = forms.CharField(
        label="Last Name",
        widget=forms.TextInput(
            attrs={
                'autofocus': 'autofocus',
                'class':'form-control',
                'placeholder': 'Last Name'}))
    group_id = forms.CharField(
        label="Group ID",
        help_text="Top secret code to register for this site.",
        widget=forms.TextInput(
            attrs={
                'autofocus': 'autofocus',
                'class':'form-control',
                'placeholder': 'Group ID'}))

    password1 = forms.CharField(
        label="Password",
        widget=PasswordInput(
            attrs={
                'class':'form-control',
                 'placeholder':'Password'}))
    password2 = forms.CharField(
        label="Confirm Password",
        widget=PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Confirm Password'}))

    # this sets the order of the fields
    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "group_id",
            "password1",
            "password2",
        )

    # this redefines the save function to include the fields you added
    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["username"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
        return user


class UserProfileForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=255)
    last_name = forms.CharField(label="Last Name", max_length=255)
    email = forms.EmailField(label="Email", disabled=True, required=False)
    get_prop_bet_emails = forms.BooleanField(required=False)
    get_accepted_bet_emails = forms.BooleanField(required=False)
