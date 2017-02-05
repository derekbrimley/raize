from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import UserManager

class MyUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('email address'), max_length=254, unique=True)
	username = models.CharField(_('username'), max_length=75, blank=True)
	first_name = models.CharField(max_length=30, blank=True)
	last_name = models.CharField(max_length=30, blank=True)
	
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	
	email_1 = models.EmailField()
	email_2 = models.EmailField()
	email_3 = models.EmailField()
	email_4 = models.EmailField()
	email_5 = models.EmailField()
	email_6 = models.EmailField()
	
	
	
	date_joined = models.DateTimeField(default=timezone.now)
	
	USERNAME_FIELD = 'email'
	
	REQUIRED_FIELDS = ['first_name', 'last_name', 'username']
	
	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		return self.first_name
	
	def email_user(self, subject, message, from_email=None):
		send_mail(subject, message, from_email, [self.email])
	
	def __unicode__(self):
		return self.email
	
	objects = UserManager()
	
class Response(models.Model):
	value_1 = models.IntegerField()
	value_2 = models.IntegerField()
	value_3 = models.IntegerField()
	value_4 = models.IntegerField()
	value_5 = models.IntegerField()
	value_6 = models.IntegerField(default=0)
	value_7 = models.IntegerField(default=0)
	value_8 = models.IntegerField(default=0)
	value_9 = models.IntegerField(default=0)
	value_10 = models.IntegerField(default=0)
	interest_1 = models.BooleanField(default=False)
	interest_2 = models.BooleanField(default=False)
	interest_3 = models.BooleanField(default=False)
	interest_4 = models.BooleanField(default=False)
	interest_5 = models.BooleanField(default=False)
	interest_6 = models.BooleanField(default=False)
	interest_7 = models.BooleanField(default=False)
	interest_8 = models.BooleanField(default=False)
	interest_9 = models.BooleanField(default=False)
	interest_10 = models.BooleanField(default=False)
	interest_11 = models.BooleanField(default=False)
	interest_12 = models.BooleanField(default=False)
	interest_13 = models.BooleanField(default=False)
	interest_14 = models.BooleanField(default=False)
	interest_15 = models.BooleanField(default=False)
	interest_16 = models.BooleanField(default=False)
	interest_17 = models.BooleanField(default=False)
	interest_18 = models.BooleanField(default=False)
	adjective_1 = models.BooleanField(default=False)
	adjective_2 = models.BooleanField(default=False)
	adjective_3 = models.BooleanField(default=False)
	adjective_4 = models.BooleanField(default=False)
	adjective_5 = models.BooleanField(default=False)
	adjective_6 = models.BooleanField(default=False)
	adjective_7 = models.BooleanField(default=False)
	adjective_8 = models.BooleanField(default=False)
	adjective_9 = models.BooleanField(default=False)
	adjective_10 = models.BooleanField(default=False)
	adjective_11 = models.BooleanField(default=False)
	adjective_12 = models.BooleanField(default=False)
	metric_1 = models.CharField(max_length=50)
	metric_2 = models.CharField(max_length=50)
	metric_3 = models.CharField(max_length=50)
	metric_4 = models.CharField(max_length=50)
	metric_5 = models.CharField(max_length=50)
	metric_6 = models.CharField(max_length=50)
	metric_7 = models.CharField(max_length=50)
	metric_8 = models.CharField(max_length=50)
	metric_9 = models.CharField(max_length=50)
	metric_10 = models.CharField(max_length=50)
	metric_11 = models.CharField(max_length=50, default=0)
	metric_12 = models.CharField(max_length=50, default=0)
	metric_13 = models.CharField(max_length=50, default=0)
	metric_14 = models.CharField(max_length=50, default=0)
	metric_15 = models.CharField(max_length=50, default=0)
	metric_16 = models.CharField(max_length=50, default=0)
	metric_17 = models.CharField(max_length=50, default=0)
	metric_18 = models.CharField(max_length=50, default=0)
#	major_1 = models.CharField(max_length=50)
#	major_2 = models.CharField(max_length=50)
#	major_3 = models.CharField(max_length=50)
#	major_4 = models.CharField(max_length=50)
#	major_5 = models.CharField(max_length=50)
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	
class UserScore(models.Model):
	PO_score = models.DecimalField(max_digits=5, decimal_places=2)
	PC_score = models.DecimalField(max_digits=5, decimal_places=2)
	PE_score = models.DecimalField(max_digits=5, decimal_places=2)
	PN_score = models.DecimalField(max_digits=5, decimal_places=2)
	PA_score = models.DecimalField(max_digits=5, decimal_places=2)
	II_score = models.DecimalField(max_digits=5, decimal_places=2)
	IA_score = models.DecimalField(max_digits=5, decimal_places=2)
	IC_score = models.DecimalField(max_digits=5, decimal_places=2)
	IS_score = models.DecimalField(max_digits=5, decimal_places=2)
	IR_score = models.DecimalField(max_digits=5, decimal_places=2)
	IE_score = models.DecimalField(max_digits=5, decimal_places=2)
	VLP_score = models.DecimalField(max_digits=5, decimal_places=2)
	VPS_score = models.DecimalField(max_digits=5, decimal_places=2)
	VFR_score = models.DecimalField(max_digits=5, decimal_places=2)
	VFF_score = models.DecimalField(max_digits=5, decimal_places=2)
	VL_score = models.DecimalField(max_digits=5, decimal_places=2)
	VBC_score = models.DecimalField(max_digits=5, decimal_places=2)
	VA_score = models.DecimalField(max_digits=5, decimal_places=2)
	VR_score = models.DecimalField(max_digits=5, decimal_places=2)
	VJS_score = models.DecimalField(max_digits=5, decimal_places=2)
	VRT_score = models.DecimalField(max_digits=5, decimal_places=2)
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	
class AlumniScores(models.Model):
	major = models.CharField(max_length=50)
	PO_score = models.DecimalField(max_digits=5, decimal_places=2)
	PC_score = models.DecimalField(max_digits=5, decimal_places=2)
	PE_score = models.DecimalField(max_digits=5, decimal_places=2)
	PN_score = models.DecimalField(max_digits=5, decimal_places=2)
	PA_score = models.DecimalField(max_digits=5, decimal_places=2)
	II_score = models.DecimalField(max_digits=5, decimal_places=2)
	IA_score = models.DecimalField(max_digits=5, decimal_places=2)
	IC_score = models.DecimalField(max_digits=5, decimal_places=2)
	IS_score = models.DecimalField(max_digits=5, decimal_places=2)
	IR_score = models.DecimalField(max_digits=5, decimal_places=2)
	IE_score = models.DecimalField(max_digits=5, decimal_places=2)
	VLP_score = models.DecimalField(max_digits=5, decimal_places=2)
	VPS_score = models.DecimalField(max_digits=5, decimal_places=2)
	VFR_score = models.DecimalField(max_digits=5, decimal_places=2)
	VFF_score = models.DecimalField(max_digits=5, decimal_places=2)
	VL_score = models.DecimalField(max_digits=5, decimal_places=2)
	VBC_score = models.DecimalField(max_digits=5, decimal_places=2)
	VA_score = models.DecimalField(max_digits=5, decimal_places=2)
	VR_score = models.DecimalField(max_digits=5, decimal_places=2)
	VJS_score = models.DecimalField(max_digits=5, decimal_places=2)
	VRT_score = models.DecimalField(max_digits=5, decimal_places=2)
	
	class Meta:
		ordering = ['major']
		
class MajorScores(models.Model):
	major = models.CharField(max_length=50)
	intercept = models.DecimalField(max_digits=12, decimal_places=10)
	po_weight = models.DecimalField(max_digits=12, decimal_places=10)
	pc_weight = models.DecimalField(max_digits=12, decimal_places=10)
	pe_weight = models.DecimalField(max_digits=12, decimal_places=10)
	pn_weight = models.DecimalField(max_digits=12, decimal_places=10)
	pa_weight = models.DecimalField(max_digits=12, decimal_places=10)
	ii_weight = models.DecimalField(max_digits=12, decimal_places=10)
	ia_weight = models.DecimalField(max_digits=12, decimal_places=10)
	ic_weight = models.DecimalField(max_digits=12, decimal_places=10)
	is_weight = models.DecimalField(max_digits=12, decimal_places=10)
	ir_weight = models.DecimalField(max_digits=12, decimal_places=10)
	ie_weight = models.DecimalField(max_digits=12, decimal_places=10)
	vlp_weight = models.DecimalField(max_digits=12, decimal_places=10)
	vps_weight = models.DecimalField(max_digits=12, decimal_places=10)
	vfr_weight = models.DecimalField(max_digits=12, decimal_places=10)
	vff_weight = models.DecimalField(max_digits=12, decimal_places=10)
	vl_weight = models.DecimalField(max_digits=12, decimal_places=10)
	vbc_weight = models.DecimalField(max_digits=12, decimal_places=10)
	va_weight = models.DecimalField(max_digits=12, decimal_places=10)
	vr_weight = models.DecimalField(max_digits=12, decimal_places=10)
	vjs_weight = models.DecimalField(max_digits=12, decimal_places=10)
	vrt_weight = models.DecimalField(max_digits=12, decimal_places=10)
	
	class Meta:
		ordering = ['major']
		
class UserMajors(models.Model):
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	major_1 = models.CharField(max_length=150, blank=True, default="")
	major_2 = models.CharField(max_length=150, blank=True, default="")
	major_3 = models.CharField(max_length=150, blank=True, default="")
	major_4 = models.CharField(max_length=150, blank=True, default="")
	major_5 = models.CharField(max_length=150, blank=True, default="")
	major_6 = models.CharField(max_length=150, blank=True, default="")
	major_7 = models.CharField(max_length=150, blank=True, default="")
	major_8 = models.CharField(max_length=150, blank=True, default="")
