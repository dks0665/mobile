from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
	if request.method == "POST":
		if request.POST['password1'] == request.POST['password2']:
			user = User.objects.create_user(
				username=request.POST['username'],password=request.POST["password1"])
			auth.login(request,user)
			return redirect('login')
		return render(request, 'signup.html')

	return render(request, 'signup.html')

def login(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(request, username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('homePage')
		else:
			return render(request, 'login.html', {'error': 'check ID or PassWord!'})
	else:
		return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return render(request, 'login.html')	
			
	  