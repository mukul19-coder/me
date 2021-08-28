from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.contrib import messages
from adduser.models import transport, client

def add_data(request):
	return render(request, "addclient.html", {})


def addclient(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			name = request.POST['name']
			gstin = request.POST['gstin']
			add1 = request.POST['address1']
			add2 = request.POST['address2']
			number = request.POST['number']
			gst = request.POST['gst']

			c = client(name=name, gstin=gstin, add1=add1, add2=add2, phone=number, gst=gst)
			c.save()
			return render(request, "addclient.html", {})
		else:
			return render(request, "addclient.html", {})
	else:
		return redirect('/')


def addtransport(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			name = request.POST['name']
			gstin = request.POST['gstin']
			add1 = request.POST['address1']
			add2 = request.POST['address2']
			number = request.POST['number']
			location = request.POST['location']

			t = transport(name=name, gstin=gstin, add1=add1, add2=add2, phone=number, location=location)
			t.save()
			return render(request, "addclient.html", {})
		else:
			return render(request, "addclient.html", {})
	else:
		return redirect('/')


def beneficiary(request):
	if request.user.is_authenticated:
		c = client.objects.all()
		t = transport.objects.all()
		return render(request, "beneficiary.html", {'c':c, 't':t})
	else:
		return redirect('/')