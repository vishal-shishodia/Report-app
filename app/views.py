from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *

# Create your views here.
def index(request):
	return render(request,'app/index.html')

def home(request):
	return render(request,'app/home.html')

def SignUp(request):
	context={}
	if request.POST:
		form=UserForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			password=form.cleaned_data.get('passsword1')
			user=authenticate(username=username,password=password)
			login(request,user)
			return redirect('app:index')
		context['form']=form
	else:
		form=UserForm()
		context['form']=form
	return render(request,'app/register.html',context)

def CreateReport(request):
	if not request.user.is_authenticated:
		return redirect('app:home')
	context={}
	if request.POST:
		form=ReportForm(request.POST)
		if form.is_valid():
			rep=form.save(commit=False)
			rep.user=request.user
			rep.reported_by=request.user.get_full_name()
			rep.save()
			
			return redirect('app:index')
		context['form']=form
	else:
		form=ReportForm()
		context['form']=form
	return render(request,'app/report_register.html',context)

def UserLogin(request):
	context={}
	if request.POST:
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user:
			login(request,user)
			return redirect('app:index')
		else:
			form=AuthenticationForm(request.POST)
			context['form']=form
			return render(request,'app/login.html',context)
	else:
		form=AuthenticationForm()
		context['form']=form
		return render(request,'app/login.html',context)


def Logout(request):
	logout(request)
	return redirect('app:home')



