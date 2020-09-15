from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from FirstApp.models import DataBase
from SaveYourPassword import settings
from django.core.mail import EmailMessage
# Create your views here.
def signup(request):
	if request.method=='POST':
		use=request.POST['us']
		pas=request.POST['pass']
		cpass=request.POST['cpass']
		email=request.POST['email']
		if use=="" or pas=="" or cpass=="" or email=="":
			#return HttpResponse('All fields are required')
			messages.warning(request,'All fields are required')
			return render(request,'signup.html')

		if pas!=cpass:
			messages.warning(request,'Passwords did not match')
			return render(request,'signup.html')
			#return HttpResponse('Passwords did not match')
		
		else:
			try:
				DataBase.objects.create(username=use,Email=email,password=pas)
				messages.warning(request,'Succesfully Signed Up')
				return render(request,'login.html')
				#return HttpResponse('Succesfully Signed Up')
			except:
				messages.warning(request,'This User is Already Exist')
				return render(request,'signup.html')
				#return HttpResponse("This User is Already Exist")

	return render(request,'signup.html')
def login(request):
	if request.method=='POST':
		username=request.POST['us']
		pwd=request.POST['pass']
		data=DataBase.objects.all().filter(username=username,password=pwd)
		if data:
			return render(request,'welcome.html',{'user':username})
		else:
			messages.warning(request,'Invalid User')
			return render(request,'login.html')
			#return HttpResponse('Invalid User')

	return render(request,'login.html')
def forgetpwd(request):
	if request.method=='POST':
		Email=request.POST['Email']
		data=DataBase.objects.get(Email=Email)
		sub="reg your password..."
		body="Your Username: "+data.username+"\n\n Your Password: "+data.password
		sender=settings.EMAIL_HOST_USER
		receiver=Email
		e=EmailMessage(sub,body,sender,[receiver])
		e.send()
		messages.warning(request,'Check your Mail for Password')
		return render(request,'forgetpwd.html')
		#return HttpResponse('Check your Mail for Password')
	return render(request,'forgetpwd.html')

def logout(request):
	return render(request,'logout.html')

def github(request):
	query = request.GET.get('data')
	data=DataBase.objects.get(username=query)
	print(data.Email)
	if request.method=='POST':
		us=request.POST['user']
		pa=request.POST['pass']
		
		data.gitu=us
		data.gitpas=pa
		data.save()
		messages.warning(request,'Details Saved Succesfully')
		return render(request,'github.html',{'us':us,'pa':pa,'user':query})
	if query!="":
		d=data.gitu
		e=data.gitpas
		print(d)
		return render(request,'github.html',{'us':d,'pa':e,'user':query})
	

def gitchange(request):	
	if request.method=='POST':
		oldpass=request.POST['oldpass']
		newpass=request.POST['newpass']
		conpass=request.POST['conpass']
		data=DataBase.objects.get(gitpas=oldpass)
		if oldpass=="" or newpass=="" or conpass=="":
			messages.warning(request,'All fields are required')
			return render(request,'gitchange.html')
		if newpass!=conpass:
			messages.warning(request,'Passwords did not match')
			return render(request,'gitchange.html')
		if data:
			data.gitpas=conpass
			data.save()
			messages.warning(request,'Password Succesfully Changes. PLease Login again')
			return render(request,'login.html')
		else:
			messages.warning(request,'Enter Correct Old Password')
			return render(request,'gitchange.html')
		
	return render(request,'gitchange.html')

def insta(request):
	query = request.GET.get('data')
	data=DataBase.objects.get(username=query)
	print(data.Email)
	if request.method=='POST':
		us=request.POST['user']
		pa=request.POST['pass']
		
		data.instau=us
		data.instapas=pa
		data.save()
		messages.warning(request,'Details Saved Succesfully')
		return render(request,'insta.html',{'us':us,'pa':pa,'user':query})
	if query!="":
		d=data.instau
		e=data.instapas
		print(d)
		return render(request,'insta.html',{'us':d,'pa':e,'user':query})

def instachange(request):
	query = request.GET.get('data')
	data=DataBase.objects.get(username=query)
	if request.method=='POST':
		oldpass=request.POST['oldpass']
		newpass=request.POST['newpass']
		conpass=request.POST['conpass']
		if oldpass=="" or newpass=="" or conpass=="":
			messages.warning(request,'All fields are required')
			return render(request,'instachange.html',{'user':query})
		if newpass!=conpass:
			messages.warning(request,'Passwords did not match')
			return render(request,'instachange.html',{'user':query})
		else:
			data.instapas=conpass
			data.save()
			messages.warning(request,'Password Succesfully Changes')
			return render(request,'welcome.html',{'user':query})
	return render(request,'instachange.html',{'user':query})

def facebook(request):
	query = request.GET.get('data')
	data=DataBase.objects.get(username=query)
	print(data.Email)
	if request.method=='POST':
		us=request.POST['user']
		pa=request.POST['pass']
		
		data.faceu=us
		data.facepas=pa
		data.save()
		messages.warning(request,'Details Saved Succesfully')
		return render(request,'facebook.html',{'us':us,'pa':pa,'user':query})
	if query!="":
		d=data.faceu
		e=data.facepas
		print(d)
		return render(request,'facebook.html',{'us':d,'pa':e,'user':query})
def facechange(request):
	query = request.GET.get('data')
	data=DataBase.objects.get(username=query)
	if request.method=='POST':
		oldpass=request.POST['oldpass']
		newpass=request.POST['newpass']
		conpass=request.POST['conpass']
		if oldpass=="" or newpass=="" or conpass=="":
			messages.warning(request,'All fields are required')
			return render(request,'facechange.html',{'user':query})
		if newpass!=conpass:
			messages.warning(request,'Passwords did not match')
			return render(request,'facechange.html',{'user':query})
		else:
			data.facepas=conpass
			data.save()
			messages.warning(request,'Password Succesfully Changes')
			return render(request,'welcome.html',{'user':query})
	return render(request,'facechange.html',{'user':query})

def stack(request):
	query = request.GET.get('data')
	data=DataBase.objects.get(username=query)
	print(data.Email)
	if request.method=='POST':
		us=request.POST['user']
		pa=request.POST['pass']
		
		data.stau=us
		data.stapas=pa
		data.save()
		messages.warning(request,'Details Saved Succesfully')
		return render(request,'stack.html',{'us':us,'pa':pa,'user':query})
	if query!="":
		d=data.stau
		e=data.stapas
		print(d)
		return render(request,'stack.html',{'us':d,'pa':e,'user':query})
def stackchange(request):
	query = request.GET.get('data')
	data=DataBase.objects.get(username=query)
	if request.method=='POST':
		oldpass=request.POST['oldpass']
		newpass=request.POST['newpass']
		conpass=request.POST['conpass']
		if oldpass=="" or newpass=="" or conpass=="":
			messages.warning(request,'All fields are required')
			return render(request,'stackchange.html',{'user':query})
		if newpass!=conpass:
			messages.warning(request,'Passwords did not match')
			return render(request,'stackchange.html',{'user':query})
		else:
			data.stapas=conpass
			data.save()
			messages.warning(request,'Password Succesfully Changes')
			return render(request,'welcome.html',{'user':query})
	return render(request,'stackchange.html',{'user':query})


