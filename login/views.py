from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from quiz.models import MyUser
from .forms import LoginForm, EditProfileForm, ForgotPasswordForm
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate, login, logout
import hashlib

# Create your views here.
def index(request):
	return HttpResponse("Hello World")

def user_login(request):
	
	if request.method == 'POST':
		form = LoginForm(request.POST)
		
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			print("user is not none")

			if user.is_active:
				print("user is active")
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				print("user is not active")
				return HttpResponseRedirect('/login/')
		else:
			print("user is none")
	else:

		print("not post")
		form = LoginForm()
	
	return render(request, 'quiz/login.html', {'form': form})


def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def results(request, question_id):
	return HttpResponse("you put in a number")

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        
        username = request.POST['email']
        if MyUser.objects.filter(username=username).exists():
            u = MyUser.objects.get(username=username)
            email = u.username
            print email
            hash_object = hashlib.sha256(email.encode())
            hex_dig = hash_object.hexdigest()
            print hex_dig
            u.reset_hash = hex_dig
            u.save()
            print email
            subject = 'Raize Reset Password'
            text_message = 'A password reset has been requested for your Raize account. If you did not request a password reset, ignore this message. If you did, you can continue by clicking the following link: http://www.raizeme.com/login/reset_password/{}/{}/'.format(str(email), str(hex_dig))
            from_email = 'raizemeapp@gmail.com'

            html_message = 'A password reset has been requested for your Raize account. If you did not request a password reset, ignore this message. If you did, you can continue by clicking the following link: <a href="http://www.raizeme.com/login/reset_password/{}/{}/">Click Here</a>'.format(str(email), str(hex_dig))
            print html_message

            msg = EmailMultiAlternatives(subject, text_message, from_email, [email])
            msg.attach_alternative(html_message,"text/html")
            msg.send()
            
            return render(request, 'login/password_reset_confirm.html', {'form': form} )
        else:
            print 'no user with that email'
            return render(request, 'login/password_reset_confirm.html', {'form': form} )
        
    form = ForgotPasswordForm()
    
    return render(request, 'login/forgot_password.html', {'form': form} )