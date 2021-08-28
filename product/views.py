from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.contrib import messages
from product.models import product

def addproduct(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			name = request.POST['name']
			description = request.POST['desc']
			category = request.POST['cat']
			hsn = request.POST['hsn']

			p = product(name=name, description=description, category=category, hsn=hsn)
			p.save()
			return render(request, "addproduct.html", {})
		else:
			return render(request, "addproduct.html", {})
	else:
		return redirect('/')


def product_list(request):
	if request.user.is_authenticated:
		p = product.objects.all()
		return render(request, "product.html", {'product':p})
	else:
		return redirect('/')