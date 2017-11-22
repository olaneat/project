from  django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length = 50, required = True)
	last_name = forms.CharField(max_length = 50, required = True)
	email = forms.EmailField(max_length = 300, help_text = 'valid email address is required')

	class Meta:
		models = User
		field = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
		