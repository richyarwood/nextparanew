from django import forms
from .models import UserStoryParagraphs
from django.contrib.auth.models import User

class AddParagraphForm(forms.ModelForm):
    class Meta:
        model = UserStoryParagraphs
        fields = ('user_paragraph', )


# Registration form

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-field'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-field'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-field'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-field'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['confirm_password']:
            raise forms.ValidationError('Passwords do not match')
        return cd['confirm_password']