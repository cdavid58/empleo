from django.shortcuts import render, redirect
from .operations import User
from company.operations_c import Company_O, Authentication_Company
import base64, json

message = ""


def Login(request):
	global message
	if request.method == "POST":
		data = request.POST
		result = False
		if int(data['type_user']) == 2:
			result = Authentication_Company().Login_Company(data)
		else:
			result = User().Login(data)
		if result['result']:
			request.session['type_user'] = int(result['type_user'])
			request.session['pk_user'] = int(result['pk_user'])
			return redirect('/')
		else:
			message = result['message']

	return render(request,'authentication/login.html',{'message':message})


def LogOut(request):
	for i,j in list(request.session.items()):
		del request.session[i]
	return redirect('/')


def Settings_Profile(request):
	data = User().Get_User()
	data['studies']
	return render(request,'settings/settings.html',{
		'user':data,
		"city": Company_O().Get_City(),
		"we":data['Work_Experience'],
		'studies':data['studies']
	})

def Profile(request):
	return render(request,'settings/profile.html')


def Update_Information_Person(request):
	if request.method == 'POST':
		encoded_content = None
		if 'file' in request.FILES:
			doc = request.FILES['file']
			file_content = doc.read()
			encoded_content = base64.b64encode(file_content).decode('utf-8')
		mutable_post_data = request.POST.copy()
		mutable_post_data['doc'] = encoded_content
		mutable_post_data['pk_user'] = request.session['pk_user']
		payload = json.dumps(mutable_post_data)
		User().Update_Information_Person(payload)
	return redirect('Settings_Profile')

def Register_Company(request):
	if request.method == 'POST':
		result = Authentication_Company().Create_Company(request.POST)
		if result['result']:
			return redirect('/')
	return render(request,'authentication/register_company.html')


def Register_User(request):
	term = True
	if request.method == 'POST':
		if 'termino' in request.POST:
			result = User().Create_User(request.POST)
			print(result)
			term = True
			if result['result']:
				request.session['pk_user'] = result['pk_user']
				return redirect('/')
		else:
			term = False
	return render(request,'authentication/register.html',{'term':term})



def Create_Studies(request):
	if request.method == 'POST':
		mutable_post_data = request.POST.copy()
		mutable_post_data['user'] = request.session['pk_user']
		result = User().Create_Studies(mutable_post_data)
		return redirect('/')


def Validation_Email(request):
	return render(request,'authentication/confirm-mail.html')