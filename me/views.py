from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.contrib import messages
from adduser.models import client, transport
from product.models import product

def menu(request):
	return render(request, "menu.html", {})

def home(request):
	if request.user.is_authenticated:
		return redirect('/menu/')

	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = auth.authenticate(username=username, password=password)

			if user is not None:
				auth.login(request, user)
				return redirect('/')

			else:
				messages.info(request,'INVALID CREDENTIALS')
				return render(request, "home.html", {})

		else:
			return render(request, "home.html", {})

def logout(request):
	auth.logout(request)
	return redirect('/')



