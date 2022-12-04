from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput
        }
        help_texts = {
            'username':None
        }

    def clean(self):
        super(LoginForm,self).clean()

        username = self.cleaned_data.get('username').lower()
        password = self.cleaned_data.get('password')

        if not authenticate(username=username,password=password):
            self._errors['username'] = self.error_class(['Username or Password is Incorrect'])
        return self.cleaned_data