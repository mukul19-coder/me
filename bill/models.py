from django.db import models
from django.db.models import Model
from django.db.models import Q
from adduser.models import client, transport
from product.models import product


# Create your models here.
class item(models.Model):
	product=models.ForeignKey(product, on_delete=models.CASCADE, default=None)
	quantity=models.CharField(max_length=100, blank=True)
	box=models.CharField(max_length=100, blank=True)
	rate=models.CharField(max_length=100, blank=True)
	mtr=models.CharField(max_length=50, blank=True)
	total=models.FloatField(max_length=100, blank=True)

class formatt(models.Model):
	img=models.ImageField(upload_to='pics', blank=True)
	invno=models.CharField(max_length=50, blank=True)

class temp(models.Model):
	method = (
		('CASH', 'CASH'),
		('NEFT', 'NEFT'),
		)

	user=models.ForeignKey(client, on_delete=models.PROTECT)
	transport=models.ForeignKey(transport, on_delete=models.PROTECT)
	payment=models.CharField(max_length=100, choices=method, default=None)
	tid=models.IntegerField(default=1)

class bill(models.Model):
	user=models.ForeignKey(client, on_delete=models.PROTECT)
	transport=models.ForeignKey(transport, on_delete=models.PROTECT)
	payment=models.CharField(max_length=100, blank=True)
	invoice_no=models.CharField(max_length=50, blank=True)
	ewaybill=models.CharField(max_length=100, blank=True, default="---------")
	date=models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.invoice_no + " " + self.user.name

class order(models.Model):
	product=models.ForeignKey(product, on_delete=models.PROTECT)
	invoice_no=models.CharField(max_length=50, blank=True)
	quantity=models.CharField(max_length=100, blank=True)
	rate=models.CharField(max_length=100, blank=True)
	box=models.CharField(max_length=100, blank=True)
	mtr=models.CharField(max_length=50, blank=True)
	total=models.FloatField(max_length=100, blank=True)

	def __str__(self):
		return "For " + self.invoice_no