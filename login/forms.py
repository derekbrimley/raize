from django import forms
from django.contrib.auth import authenticate, login
from quiz.models import MyUser

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form_input'}), max_length=100, label='Email')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form_input'}), label='Password')
	
	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		if not user or not user.is_active:
			raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
		return self.cleaned_data
	
	def login(self, request):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		return user
	
class EditProfileForm(forms.Form):
	first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form_input'}))
	last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form_input'}))
	
class ForgotPasswordForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form_input'}), max_length=100, label='Email')