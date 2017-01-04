from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from .forms import QuizForm, FriendQuizForm, EmailForm
from quiz.models import Response, MyUser, UserScore, AlumniScores, MajorScores, UserMajors
from django.core.urlresolvers import reverse
import random
from django.contrib.auth.decorators import login_required
from decimal import Decimal
from django.core.mail import EmailMultiAlternatives
import operator


def index(request):
	return render(request, 'quiz/index.html')


def students(request):
	return render(request, 'quiz/students.html')


def graduates(request):
	return render(request, 'quiz/graduates.html')


def team(request):
	return render(request, 'quiz/team.html')



@login_required(login_url="/login/")
def profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST)

		if form.is_valid():
			
			first_name = form.cleaned_data['first_name']
			last_name = form.cleaned_data['last_name']

			user_id = request.user.id


			u = MyUser.objects.filter(id=user_id).update(
				first_name = first_name,
				last_name = last_name
			)
		
	else:
		
		first_name = request.user.first_name
		last_name = request.user.last_name
		
		form = EditProfileForm(
			initial={
				'first_name':first_name,
				'last_name':last_name
			}
		)
		
		user_id = request.user.id
		print("user: " + str(user_id))
		context = {
			'form': form,
			'user_id': user_id
		}
		
	return render(request, 'quiz/profile.html', context)



def quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)

        if form.is_valid():

            user_form = {
                'user_id': None,
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password'],
                'password2': form.cleaned_data['password2'],
                'value_1': form.cleaned_data['value_1'],
                'value_2': form.cleaned_data['value_2'],
                'value_3': form.cleaned_data['value_3'],
                'value_4': form.cleaned_data['value_4'],
                'value_5': form.cleaned_data['value_5'],
                'value_6': form.cleaned_data['value_1'],
                'value_7': form.cleaned_data['value_2'],
                'value_8': form.cleaned_data['value_3'],
                'value_9': form.cleaned_data['value_4'],
                'value_10': form.cleaned_data['value_5'],
                'interest_1': form.cleaned_data['interest_1'],
                'interest_2': form.cleaned_data['interest_2'],
                'interest_3': form.cleaned_data['interest_3'],
                'interest_4': form.cleaned_data['interest_4'],
                'interest_5': form.cleaned_data['interest_5'],
                'interest_6': form.cleaned_data['interest_1'],
                'interest_7': form.cleaned_data['interest_2'],
                'interest_8': form.cleaned_data['interest_3'],
                'interest_9': form.cleaned_data['interest_4'],
                'interest_10': form.cleaned_data['interest_5'],
                'interest_11': form.cleaned_data['interest_1'],
                'interest_12': form.cleaned_data['interest_2'],
                'interest_13': form.cleaned_data['interest_3'],
                'interest_14': form.cleaned_data['interest_4'],
                'interest_15': form.cleaned_data['interest_5'],
                'interest_16': form.cleaned_data['interest_1'],
                'interest_17': form.cleaned_data['interest_2'],
                'interest_18': form.cleaned_data['interest_3'],
                'adjective_1': form.cleaned_data['adjective_1'],
                'adjective_2': form.cleaned_data['adjective_2'],
                'adjective_3': form.cleaned_data['adjective_3'],
                'adjective_4': form.cleaned_data['adjective_4'],
                'adjective_5': form.cleaned_data['adjective_5'],
                'adjective_6': form.cleaned_data['adjective_1'],
                'adjective_7': form.cleaned_data['adjective_2'],
                'adjective_8': form.cleaned_data['adjective_3'],
                'adjective_9': form.cleaned_data['adjective_4'],
                'adjective_10': form.cleaned_data['adjective_5'],
                'adjective_11': form.cleaned_data['adjective_1'],
                'adjective_12': form.cleaned_data['adjective_2'],
                'metric_1': form.cleaned_data['metric_1'],
                'metric_2': form.cleaned_data['metric_2'],
                'metric_3': form.cleaned_data['metric_3'],
                'metric_4': form.cleaned_data['metric_4'],
                'metric_5': form.cleaned_data['metric_5'],
                'metric_6': form.cleaned_data['metric_6'],
                'metric_7': form.cleaned_data['metric_7'],
                'metric_8': form.cleaned_data['metric_8'],
                'metric_9': form.cleaned_data['metric_9'],
                'metric_10': form.cleaned_data['metric_10'],
                'metric_11': form.cleaned_data['metric_11'],
                'metric_12': form.cleaned_data['metric_12'],
                'metric_13': form.cleaned_data['metric_13'],
                'metric_14': form.cleaned_data['metric_14'],
                'metric_15': form.cleaned_data['metric_15'],
                'metric_16': form.cleaned_data['metric_16'],
                'metric_17': form.cleaned_data['metric_17'],
                'metric_18': form.cleaned_data['metric_18']
            }
        
            u_id = get_results(request,user_form)
            return HttpResponseRedirect('/quiz/{}/profile_results/'.format(u_id))
        else:
            print("Form not valid")
    else:
        form = QuizForm()

    #	emails = MyUser.objects.values_list("email", flat=True).distinct()

    context = {
        'form': form
    }

    return render(request, 'quiz/quiz.html', context)


def logistic_regression(po_score, pc_score, pe_score, pn_score, pa_score, ii_score, ia_score, ic_score, is_score, ir_score, ie_score, vlp_score, vps_score, vfr_score, vff_score, vl_score, vbc_score, va_score, vr_score, vjs_score, vrt_score):
	
	majors = MajorScores.objects.distinct('major')

	major_results = {};
	
	for major in majors:
		print("major: " + major.major)
	
		intercept = major.intercept
		po_weight = major.po_weight
		pc_weight = major.pc_weight
		pe_weight = major.pe_weight
		pn_weight = major.pn_weight
		pa_weight = major.pa_weight
		ii_weight = major.ii_weight
		ia_weight = major.ia_weight
		ic_weight = major.ic_weight
		is_weight = major.is_weight
		ir_weight = major.ir_weight
		ie_weight = major.ie_weight
		vlp_weight = major.vlp_weight
		vps_weight = major.vps_weight
		vfr_weight = major.vfr_weight
		vff_weight = major.vff_weight
		vl_weight = major.vl_weight
		vbc_weight = major.vbc_weight
		va_weight = major.va_weight
		vr_weight = major.vr_weight
		vjs_weight = major.vjs_weight
		vrt_weight = major.vrt_weight

		major_result = (intercept+po_weight*Decimal(po_score)) \
						+(pc_weight*Decimal(pc_score)) \
						+(pe_weight*Decimal(pe_score)) \
						+(pn_weight*Decimal(pn_score)) \
						+(pa_weight*Decimal(pa_score)) \
						+(ii_weight*Decimal(ii_score)) \
						+(ia_weight*Decimal(ia_score)) \
						+(ic_weight*Decimal(ic_score)) \
						+(is_weight*Decimal(is_score)) \
						+(ir_weight*Decimal(ir_score)) \
						+(ie_weight*Decimal(ie_score)) \
						+(vlp_weight*Decimal(vlp_score)) \
						+(vps_weight*Decimal(vps_score)) \
						+(vfr_weight*Decimal(vfr_score)) \
						+(vff_weight*Decimal(vff_score)) \
						+(vl_weight*Decimal(vl_score)) \
						+(vbc_weight*Decimal(vbc_score)) \
						+(va_weight*Decimal(va_score)) \
						+(vr_weight*Decimal(vr_score)) \
						+(vjs_weight*Decimal(vjs_score)) \
						+(vrt_weight*Decimal(vrt_score))
	
		print(major_result)
		major_results[major.major] = round(major_result,4)
	sorted_major_results = sorted(major_results.items(), key=operator.itemgetter(1), reverse=True)
	print("sorted major results: " + str(sorted_major_results))
	
	top_major_results = {}
	i = 0
	for sorted_major_result in sorted_major_results:
		if i == 0:
			if sorted_major_result[1] < .5:
				top_major_results[i] = 'Accounting'
			else:
				top_major_results[i] = sorted_major_result[0]
		elif i < 8:
			top_major_results[i] = sorted_major_result[0]
		else:
			break
		i += 1
		
	return top_major_results
	
	
	



def knn_algorithm(po_score, pc_score, pe_score, pn_score, pa_score, ii_score, ia_score, ic_score, is_score, ir_score, ie_score, vlp_score, vps_score, vfr_score, vff_score, vl_score, vbc_score, va_score, vr_score, vjs_score, vrt_score):
	return po_score
	
	

def euclidean_distance(row):
	"""
	A SIMPLE EUCLIDEAN DISTANCE FUNCTION
	"""
	inner_value = 0
	for k in distance_columns:
		inner_value += (row[k] - selected_player[k]) ** 2
	return math.sqrt(inner_value)


def average_list(list):
	return float(sum(list))/len(list) if len(list) > 0 else float('nan')



def reverse_personality(score):
	if score == 0:
		new_score = 6
	elif score == 1:
		new_score = 5
	elif score == 2:
		new_score = 4
	elif score == 3:
		new_score = 3
	elif score == 4:
		new_score = 2
	elif score == 5:
		new_score = 1
	elif score == 6:
		new_score = 0
	else:
		new_score = 0
	
	return new_score


def profile_results(request, u_id):
    context = get_majors(u_id)
    return render(request, 'quiz/results.html', context)
	

def friend_complete(request, id):
	u = MyUser.objects.get(id=id)

	first_name = u.first_name
	full_name = u.first_name + ' ' + u.last_name
	
	context = {
		'id': id,
		'first_name' : first_name,
		'full_name' : full_name
	}
	
	return render(request, 'quiz/friend_complete.html', context)


def send_emails(request, id):
	form = EmailForm(request.POST)
		
	if form.is_valid():
		print("errors:" + str(form.errors))
		email_1 = form.cleaned_data['email_1']
		email_2 = form.cleaned_data['email_2']
		email_3 = form.cleaned_data['email_3']
		email_4 = form.cleaned_data['email_4']
		email_5 = form.cleaned_data['email_5']
		email_6 = form.cleaned_data['email_6']
		email_7 = form.cleaned_data['email_7']
		email_8 = form.cleaned_data['email_8']
		email_9 = form.cleaned_data['email_9']
		email_10 = form.cleaned_data['email_10']

		print("Email 1: " + email_1)
		print("Email 2: " + email_2)
		print("Email 3: " + email_3)
		print("Email 4: " + email_4)
		print("Email 5: " + email_5)
		print("Email 6: " + email_6)
		print("Email 7: " + email_7)
		print("Email 8: " + email_8)
		print("Email 9: " + email_9)
		print("Email 10: " + email_10)
		
		u = MyUser.objects.get(id=id)

		u.email_1 = email_1
		u.email_2 = email_2
		u.email_3 = email_3
		u.email_4 = email_4
		u.email_5 = email_5
		u.email_6 = email_6
		u.email_7 = email_7
		u.email_8 = email_8
		u.email_9 = email_9
		u.email_10 = email_10
		u.save()

		full_name = u.first_name + ' ' + u.last_name
		
		subject = 'Feedback for ' + full_name
		text_message = full_name + ' wants to find a future that fits their unique situation and attributes. Raize is a service that collects current criteria for students by issuing self and crowd-sourced questionnaires. This information allows the student to understand more about themselves and how they fit relevant to their situation. This student has selected you as someone who understands them well and would like you to take 4 minutes to complete a questionnaire about their attributes. The questionnaire is completely anonymous and can be started by clicking the link: http://raizeme.herokuapp.com/quiz/' + str(id) + '/'
		from_email = 'raizemeapp@gmail.com'
		
		emails = [email_1, email_2, email_3, email_4, email_5, email_6, email_7, email_8, email_9, email_10]
		
		recipients = []
		for email in emails:
			if email is not None:
				recipients.append(email)
		
		html_message = full_name + ' wants to find a future that fits their unique situation and attributes. Raize is a service that collects current criteria for students by issuing self and crowd-sourced questionnaires. This information allows the student to understand more about themselves and how they fit relevant to their situation. This student has selected you as someone who understands them well and would like you to take 4 minutes to complete a questionnaire about their attributes. The questionnaire is completely anonymous and can be started by clicking the link: <a href="http://raizeme.herokuapp.com/quiz/' + str(id) + '/">Click Here</a>'
		
		msg = EmailMultiAlternatives(subject, text_message, from_email, [email_1])
		msg.attach_alternative(html_message,"text/html")
		msg.send()

		print("sent")
		
	return render(request, 'quiz/confirmation.html')
	
	

def friend_quiz(request, id):
    if request.method == 'POST':
        form = FriendQuizForm(request.POST)

        if form.is_valid():
			
            user_form = {
                'user_id': form.cleaned_data['user_id'],
                'value_1': form.cleaned_data['value_1'],
                'value_2': form.cleaned_data['value_2'],
                'value_3': form.cleaned_data['value_3'],
                'value_4': form.cleaned_data['value_4'],
                'value_5': form.cleaned_data['value_5'],
                'value_6': form.cleaned_data['value_1'],
                'value_7': form.cleaned_data['value_2'],
                'value_8': form.cleaned_data['value_3'],
                'value_9': form.cleaned_data['value_4'],
                'value_10': form.cleaned_data['value_5'],
                'interest_1': form.cleaned_data['interest_1'],
                'interest_2': form.cleaned_data['interest_2'],
                'interest_3': form.cleaned_data['interest_3'],
                'interest_4': form.cleaned_data['interest_4'],
                'interest_5': form.cleaned_data['interest_5'],
                'interest_6': form.cleaned_data['interest_1'],
                'interest_7': form.cleaned_data['interest_2'],
                'interest_8': form.cleaned_data['interest_3'],
                'interest_9': form.cleaned_data['interest_4'],
                'interest_10': form.cleaned_data['interest_5'],
                'interest_11': form.cleaned_data['interest_1'],
                'interest_12': form.cleaned_data['interest_2'],
                'interest_13': form.cleaned_data['interest_3'],
                'interest_14': form.cleaned_data['interest_4'],
                'interest_15': form.cleaned_data['interest_5'],
                'interest_16': form.cleaned_data['interest_1'],
                'interest_17': form.cleaned_data['interest_2'],
                'interest_18': form.cleaned_data['interest_3'],
                'adjective_1': form.cleaned_data['adjective_1'],
                'adjective_2': form.cleaned_data['adjective_2'],
                'adjective_3': form.cleaned_data['adjective_3'],
                'adjective_4': form.cleaned_data['adjective_4'],
                'adjective_5': form.cleaned_data['adjective_5'],
                'adjective_6': form.cleaned_data['adjective_1'],
                'adjective_7': form.cleaned_data['adjective_2'],
                'adjective_8': form.cleaned_data['adjective_3'],
                'adjective_9': form.cleaned_data['adjective_4'],
                'adjective_10': form.cleaned_data['adjective_5'],
                'adjective_11': form.cleaned_data['adjective_1'],
                'adjective_12': form.cleaned_data['adjective_2'],
                'metric_1': form.cleaned_data['metric_1'],
                'metric_2': form.cleaned_data['metric_2'],
                'metric_3': form.cleaned_data['metric_3'],
                'metric_4': form.cleaned_data['metric_4'],
                'metric_5': form.cleaned_data['metric_5'],
                'metric_6': form.cleaned_data['metric_6'],
                'metric_7': form.cleaned_data['metric_7'],
                'metric_8': form.cleaned_data['metric_8'],
                'metric_9': form.cleaned_data['metric_9'],
                'metric_10': form.cleaned_data['metric_10'],
                'metric_11': form.cleaned_data['metric_11'],
                'metric_12': form.cleaned_data['metric_12'],
                'metric_13': form.cleaned_data['metric_13'],
                'metric_14': form.cleaned_data['metric_14'],
                'metric_15': form.cleaned_data['metric_15'],
                'metric_16': form.cleaned_data['metric_16'],
                'metric_17': form.cleaned_data['metric_17'],
                'metric_18': form.cleaned_data['metric_18']
            }

            u_id = get_results(request,user_form)

            average_user_scores(u_id)
           
            return friend_complete(request, u_id)
        else:
            print("Form not valid")
            print(form.errors)
    else:
        try:
            user = MyUser.objects.get(id=id)
        except MyUser.DoesNotExist:
            return render(request, 'quiz/friend_quiz_error.html')

        else:
            form = FriendQuizForm(initial={'user_id': id})

            print(form)

            u = MyUser.objects.get(id=id)

            first_name = u.first_name
            full_name = u.first_name + ' ' + u.last_name

            context = {
                'form' : form,
                'first_name' : first_name,
                'full_name' : full_name
            }
    return render(request, 'quiz/friend_quiz.html', context)


def get_results(request, user_form):

#    NORMALIZE VALUES
    value_list = [user_form['value_1'],
                 user_form['value_2'],
                 user_form['value_3'],
                 user_form['value_4'],
                 user_form['value_5'],
                 user_form['value_6'],
                 user_form['value_7'],
                 user_form['value_8'],
                 user_form['value_9'],
                 user_form['value_10']]
    value_average = sum(value_list) / float(len(value_list))

    normalized_value_1 = user_form['value_1'] - value_average
    normalized_value_2 = user_form['value_2'] - value_average
    normalized_value_3 = user_form['value_3'] - value_average
    normalized_value_4 = user_form['value_4'] - value_average
    normalized_value_5 = user_form['value_5'] - value_average
    normalized_value_6 = user_form['value_6'] - value_average
    normalized_value_7 = user_form['value_7'] - value_average
    normalized_value_8 = user_form['value_8'] - value_average
    normalized_value_9 = user_form['value_9'] - value_average
    normalized_value_10 = user_form['value_10'] - value_average

    if not user_form['user_id']:
        u = MyUser.objects.create_user(user_form['email'], user_form['email'], user_form['password'])
        u.first_name = user_form['first_name']
        u.last_name = user_form['last_name']

        u.save()
        u_id = u.id
    else:
        u_id = user_form['user_id']
        u = MyUser.objects.get(id=u_id)

    r = Response(
        value_1 = normalized_value_1,
        value_2 = normalized_value_2,
        value_3 = normalized_value_3,
        value_4 = normalized_value_4,
        value_5 = normalized_value_5,
        value_6 = normalized_value_6,
        value_7 = normalized_value_7,
        value_8 = normalized_value_8,
        value_9 = normalized_value_9,
        value_10 = normalized_value_10,
        interest_1 = user_form['interest_1'],
        interest_2 = user_form['interest_2'],
        interest_3 = user_form['interest_3'],
        interest_4 = user_form['interest_4'],
        interest_5 = user_form['interest_5'],
        interest_6 = user_form['interest_6'],
        interest_7 = user_form['interest_7'],
        interest_8 = user_form['interest_8'],
        interest_9 = user_form['interest_9'],
        interest_10 = user_form['interest_10'],
        interest_11 = user_form['interest_11'],
        interest_12 = user_form['interest_12'],
        interest_13 = user_form['interest_13'],
        interest_14 = user_form['interest_14'],
        interest_15 = user_form['interest_15'],
        interest_16 = user_form['interest_16'],
        interest_17 = user_form['interest_17'],
        interest_18 = user_form['interest_18'],
        adjective_1 = user_form['adjective_1'],
        adjective_2 = user_form['adjective_2'],
        adjective_3 = user_form['adjective_3'],
        adjective_4 = user_form['adjective_4'],
        adjective_5 = user_form['adjective_5'],
        adjective_6 = user_form['adjective_6'],
        adjective_7 = user_form['adjective_7'],
        adjective_8 = user_form['adjective_8'],
        adjective_9 = user_form['adjective_9'],
        adjective_10 = user_form['adjective_10'],
        adjective_11 = user_form['adjective_11'],
        adjective_12 = user_form['adjective_12'],
        metric_1 = user_form['metric_1'],
        metric_2 = user_form['metric_2'],
        metric_3 = user_form['metric_3'],
        metric_4 = user_form['metric_4'],
        metric_5 = user_form['metric_5'],
        metric_6 = user_form['metric_6'],
        metric_7 = user_form['metric_7'],
        metric_8 = user_form['metric_8'],
        metric_9 = user_form['metric_9'],
        metric_10 = user_form['metric_10'],
        metric_11 = user_form['metric_11'],
        metric_12 = user_form['metric_12'],
        metric_13 = user_form['metric_13'],
        metric_14 = user_form['metric_14'],
        metric_15 = user_form['metric_15'],
        metric_16 = user_form['metric_16'],
        metric_17 = user_form['metric_17'],
        metric_18 = user_form['metric_18'],
        user = u
        )
    r.save();

    po_list = [reverse_personality(normalized_value_1),normalized_value_7]
    pc_list = [reverse_personality(normalized_value_2),normalized_value_4]
    pe_list = [reverse_personality(normalized_value_3),normalized_value_9]
    pn_list = [reverse_personality(normalized_value_8),normalized_value_5]
    pa_list = [reverse_personality(normalized_value_10),normalized_value_6]
    print("po_list: " + str(po_list))
    print("pc_list: " + str(pc_list))
    print("pe_list: " + str(pe_list))
    print("pn_list: " + str(pn_list))
    print("pa_list: " + str(pa_list))

    po_score = average_list(po_list)
    pc_score = average_list(pc_list)
    pe_score = average_list(pe_list)
    pn_score = average_list(pn_list)
    pa_score = average_list(pa_list)
    print("po_score: " + str(po_score))
    print("pc_score: " + str(pc_score))
    print("pe_score: " + str(pe_score))
    print("pn_score: " + str(pn_score))
    print("pa_score: " + str(pa_score))

    ii_list = [user_form['interest_1'],user_form['interest_7'],user_form['interest_15'],user_form['adjective_5'],user_form['adjective_7']]
    ia_list = [user_form['interest_3'],user_form['interest_9'],user_form['interest_18'],user_form['adjective_10'],user_form['adjective_12']]
    ic_list = [user_form['interest_5'],user_form['interest_11'],user_form['interest_14'],user_form['adjective_2'],user_form['adjective_4']]
    is_list = [user_form['interest_2'],user_form['interest_8'],user_form['interest_17'],user_form['adjective_9'],user_form['adjective_11']]
    ir_list = [user_form['interest_4'],user_form['interest_10'],user_form['interest_13'],user_form['adjective_1'],user_form['adjective_3']]
    ie_list = [user_form['interest_6'],user_form['interest_12'],user_form['interest_16'],user_form['adjective_6'],user_form['adjective_8']]
    print("ii_list: " + str(ii_list))
    print("ia_list: " + str(ia_list))
    print("ic_list: " + str(ic_list))
    print("is_list: " + str(is_list))
    print("ir_list: " + str(ir_list))
    print("ie_list: " + str(ie_list))

    ii_score = average_list(ii_list)
    ia_score = average_list(ia_list)
    ic_score = average_list(ic_list)
    is_score = average_list(is_list)
    ir_score = average_list(ir_list)
    ie_score = average_list(ie_list)
    print("ii_score: " + str(ii_score))
    print("ia_score: " + str(ia_score))
    print("ic_score: " + str(ic_score))
    print("is_score: " + str(is_score))
    print("ir_score: " + str(ir_score))
    print("ie_score: " + str(ie_score))

    vlp_score = (user_form['metric_1'])
    vps_score = (user_form['metric_2'])
    vfr_score = (user_form['metric_3'])
    vff_score = (user_form['metric_4'])
    vl_score = (user_form['metric_5'])
    vbc_score = (user_form['metric_6'])
    va_score = (user_form['metric_7'])
    vr_score = (user_form['metric_8'])
    vjs_score = (user_form['metric_9'])
    vrt_score = (user_form['metric_10'])
    print("vlp_score: " + str(vlp_score))
    print("vps_score: " + str(vps_score))
    print("vfr_score: " + str(vfr_score))
    print("vff_score: " + str(vff_score))
    print("vl_score: " + str(vl_score))
    print("vbc_score: " + str(vbc_score))
    print("va_score: " + str(va_score))
    print("vr_score: " + str(vr_score))
    print("vjs_score: " + str(vjs_score))
    print("vrt_score: " + str(vrt_score))

    us = UserScore(
        PO_score = po_score,
        PC_score = pc_score,
        PE_score = pe_score,
        PN_score = pn_score,
        PA_score = pa_score,
        II_score = ii_score,
        IA_score = ia_score,
        IC_score = ic_score,
        IS_score = is_score,
        IR_score = ir_score,
        IE_score = ie_score,
        VLP_score = vlp_score,
        VPS_score = vps_score,
        VFR_score = vfr_score,
        VFF_score = vff_score,
        VL_score = vl_score,
        VBC_score = vbc_score,
        VA_score = va_score,
        VR_score = vr_score,
        VJS_score = vjs_score,
        VRT_score = vrt_score,
        user = u
    )

    us.save()

    majors = logistic_regression(po_score,
                                 pc_score,
                                 pe_score,
                                 pn_score,
                                 pa_score,
                                 ii_score,
                                 ia_score,
                                 ic_score,
                                 is_score,
                                 ir_score,
                                 ie_score,
                                 vlp_score,
                                 vps_score,
                                 vfr_score,
                                 vff_score,
                                 vl_score,
                                 vbc_score,
                                 va_score,
                                 vr_score,
                                 vjs_score,
                                 vrt_score)
    print("Majors: " + str(majors))

    
    if not user_form['user_id']:
        um = UserMajors(
            user = u,
            major_1 = majors[0],
            major_2 = majors[1],
            major_3 = majors[2],
            major_4 = majors[3],
            major_5 = majors[4],
            major_6 = majors[5],
            major_7 = majors[6],
            major_8 = majors[7]
        )
        um.save()
        
        full_name = '{} {}'.format(user_form['first_name'], user_form['last_name'])
        link = '<a href="http://raizeme.herokuapp.com/quiz/{}/profile_results/">this link</a>'.format(u_id)

        subject = 'Raize questionnaire submitted for {}'.format(full_name)
        text_message = '{}, thanks for submitting your Raize questionnaire. To see your results, go to http://raizeme.herokuapp.com/quiz/{}/profile_results/'.format(user_form['first_name'], u_id)
        from_email = 'raizemeapp@gmail.com'

        html_message = '{}, thanks for submitting your Raize questionnaire. To see your results, click on {}'.format(user_form['first_name'], link)

        msg = EmailMultiAlternatives(subject, text_message, from_email, [user_form['email']])
        msg.attach_alternative(html_message,"text/html")
        msg.send()

        user = authenticate(username=user_form['email'], password=user_form['password'])
        login(request, user)
    
    return u_id


def average_user_scores(u_id):
    scores = UserScore.objects.filter(user=u_id)
			
    num_scores = scores.count()
    total_po_score = 0
    total_pc_score = 0
    total_pe_score = 0
    total_pn_score = 0
    total_pa_score = 0
    total_ii_score = 0
    total_ia_score = 0
    total_ic_score = 0
    total_is_score = 0
    total_ir_score = 0
    total_ie_score = 0
    total_vlp_score = 0
    total_vps_score = 0
    total_vfr_score = 0
    total_vff_score = 0
    total_vl_score = 0
    total_vbc_score = 0
    total_va_score = 0
    total_vr_score = 0
    total_vjs_score = 0
    total_vrt_score = 0

    for score in scores:
        total_po_score += score.PO_score
        total_pc_score += score.PC_score
        total_pe_score += score.PE_score
        total_pn_score += score.PN_score
        total_pa_score += score.PA_score
        total_ii_score += score.II_score
        total_ia_score += score.IA_score
        total_ic_score += score.IC_score
        total_is_score += score.IS_score 
        total_ir_score += score.IR_score
        total_ie_score += score.IE_score
        total_vlp_score += score.VLP_score
        total_vps_score += score.VPS_score
        total_vfr_score += score.VFR_score
        total_vff_score += score.VFF_score
        total_vl_score += score.VL_score
        total_vbc_score += score.VBC_score
        total_va_score += score.VA_score
        total_vr_score += score.VR_score
        total_vjs_score += score.VJS_score
        total_vrt_score += score.VRT_score

    average_po_score = total_po_score / num_scores
    average_pc_score = total_pc_score / num_scores
    average_pe_score = total_pe_score / num_scores
    average_pn_score = total_pn_score / num_scores
    average_pa_score = total_pa_score / num_scores
    average_ii_score = total_ii_score / num_scores
    average_ia_score = total_ia_score / num_scores
    average_ic_score = total_ic_score / num_scores
    average_is_score = total_is_score / num_scores
    average_ir_score = total_ir_score / num_scores
    average_ie_score = total_ie_score / num_scores
    average_vlp_score = total_vlp_score / num_scores
    average_vps_score = total_vps_score / num_scores
    average_vfr_score = total_vfr_score / num_scores
    average_vff_score = total_vff_score / num_scores
    average_vl_score = total_vl_score / num_scores
    average_vbc_score = total_vbc_score / num_scores
    average_va_score = total_va_score / num_scores
    average_vr_score = total_vr_score / num_scores
    average_vjs_score = total_vjs_score / num_scores
    average_vrt_score = total_vrt_score / num_scores

    majors = logistic_regression(
        average_po_score,
        average_pc_score,
        average_pe_score,
        average_pn_score,
        average_pa_score,
        average_ii_score,
        average_ia_score,
        average_ic_score,
        average_is_score,
        average_ir_score,
        average_ie_score,
        average_vlp_score,
        average_vps_score,
        average_vfr_score,
        average_vff_score,
        average_vl_score,
        average_vbc_score,
        average_va_score,
        average_vr_score,
        average_vjs_score,
        average_vrt_score)
    print("Majors: " + str(majors))

    print(majors[0])
    print(majors[1])
    print(majors[2])
    print(majors[3])
    print(majors[4])
    print(majors[5])
    print(majors[6])
    print(majors[7])

    um = UserMajors.objects.get(user_id=u_id)
    um.major_1 = majors[0]
    um.major_2 = majors[1]
    um.major_3 = majors[2]
    um.major_4 = majors[3]
    um.major_5 = majors[4]
    um.major_6 = majors[5]
    um.major_7 = majors[6]
    um.major_8 = majors[7]
    um.save()
    
    

def get_majors(u_id):
    u = MyUser.objects.get(id=u_id)

    first_name = u.first_name
    full_name = '{} {}'.format(u.first_name, u.last_name)

    um = UserMajors.objects.get(user_id=u_id)

    majors = [um.major_1,
              um.major_2,
              um.major_3,
              um.major_4,
              um.major_5,
              um.major_6,
              um.major_7,
              um.major_8]

    us = UserScore.objects.filter(user_id=u_id)

    score_count = us.count()

    if score_count == 1:
        accuracy_percentage = 10
    elif score_count == 2:
        accuracy_percentage = 20
    elif score_count == 3:
        accuracy_percentage = 30
        del majors[-1:]
    elif score_count == 4:
        accuracy_percentage = 40
    elif score_count == 5:
        accuracy_percentage = 50
        del majors[-2:]
    elif score_count == 6:
        accuracy_percentage = 60
    elif score_count == 7:
        accuracy_percentage = 70
        del majors[-3:]
    elif score_count == 8:
        accuracy_percentage = 80
    elif score_count == 9:
        accuracy_percentage = 90
        del majors[-4:]
    else:
        accuracy_percentage = 90
        del majors[-5:]
        
    form = EmailForm()
    link = 'http://raizeme.herokuapp.com/quiz/{}/'.format(u_id)
    
    context = {
        'id': u_id,
        'form': form,
        'link': link,
        'first_name': first_name,
        'full_name': full_name,
        'majors': majors,
        'result_num': len(majors),
        'accuracy_percentage': accuracy_percentage
    }
    
    return context


##############ONE TIME SCRIPTS#############

#def populate_major_scores(request):
#	majors = AlumniScores.objects.distinct('major')
#	
#	for major in majors:
#		print("major: " + major.major)
#		
#		m = MajorScores(
#			major = major.major,
#			po_weight = 1,
#			pc_weight = 1,
#			pe_weight = 1,
#			pn_weight = 1,
#			pa_weight = 1,
#			ii_weight = 1,
#			ia_weight = 1,
#			ic_weight = 1,
#			is_weight = 1,
#			ir_weight = 1,
#			ie_weight = 1,
#			vlp_weight = 1,
#			vps_weight = 1,
#			vfr_weight = 1,
#			vff_weight = 1,
#			vl_weight = 1,
#			vbc_weight = 1,
#			va_weight = 1,
#			vr_weight = 1,
#			vjs_weight = 1,
#			vrt_weight = 1
#		)
#		m.save()
#	
#	
#	return majors

#TODO: For the new algorithm, need to create a new table from the alumni table. Run the regression algorithm for each of the alumni, which will create additional 69 columns for each alumni. Then, when a new user submits, find the top 5 majors using regression algorithm, and then find the probabilities from those 5 majors in the alumni table. Then, find the euclidean distance between the 5. then go through and find the difference between the euclidean distance of the alumni and the new user. You will have a list of differences, get the smallest 8, and find the majors for those alumni. Those are the ones you display.

#TODO: run 30% of alumni through the algorithm, find their top 8, and make a report of their top 8 and their actual major.

def forgot_password(request):
    return render(request, 'login/forgot_password.html')