from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.user_login, name='user_login'),
    url(r'^logout', views.user_logout, name='user_logout'),
	url(r'^', views.index, name='index'),
	url(r'^(?P<question_id>[0-9]+)/$', views.results, name='results'),
    url(r'^forgot_password', views.forgot_password, name='forgot_password'),
#    url(r'^user/password/reset/$', 
#        'django.contrib.auth.views.password_reset', 
#        {'post_reset_redirect' : '/user/password/reset/done/'},
#        name="password_reset"),
#    (r'^user/password/reset/done/$',
#        'django.contrib.auth.views.password_reset_done'),
#    (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
#        'django.contrib.auth.views.password_reset_confirm', 
#        {'post_reset_redirect' : '/user/password/done/'}),
#    (r'^user/password/done/$', 
#        'django.contrib.auth.views.password_reset_complete'),
]