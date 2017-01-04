from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^students', views.students, name='students'),
	url(r'^graduates', views.graduates, name='graduates'),
	url(r'^team', views.team, name='team'),
	url(r'^profile', views.profile, name='profile'),
#	
#    url(r'^login/forgot_password', views.forgot_password, name='forgot_password'),
	
	url(r'^quiz/$', views.quiz, name='quiz'),
	url(r'^quiz/(?P<u_id>[0-9]+)/profile_results/$', views.profile_results, name='profile_results'),
	url(r'^quiz/(?P<id>[0-9]+)/send_emails/$', views.send_emails, name='send_emails'),
	url(r'^quiz/submit/$', views.quiz, name='submit'),
	url(r'^(?P<id>[0-9]+)/$', views.friend_quiz, name='friend_quiz'),
	url(r'^(?P<id>[0-9]+)/friend_submit/$', views.friend_quiz, name='friend_submit'),
#	url(r'^quiz/populate_major_scores/$', views.populate_major_scores, name='populate_major_scores'),
#	url(r'^quiz/logistic_regression/$', views.logistic_regression, name='logistic_regression'),
]