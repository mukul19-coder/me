from django.db import models

# Create your models here.
class client(models.Model):
	gstm = (
		('I-GST', 'I-GST'),
		('C-GST & S-GST', 'C-GST & S-GST'),
		)

	name=models.CharField(max_length=100)
	gstin=models.CharField(max_length=50)
	add1=models.CharField(max_length=100)
	add2=models.CharField(max_length=100)
	phone=models.CharField(max_length=30)
	gst=models.CharField(max_length=50, choices=gstm, default="I-GST")

	def __str__(self):
		return self.name + " - " + self.add2

class transport(models.Model):
	name=models.CharField(max_length=100)
	gstin=models.CharField(max_length=50)
	add1=models.CharField(max_length=100)
	add2=models.CharField(max_length=100)
	location=models.CharField(max_length=100, blank=True)
	phone=models.CharField(max_length=20)

	def __str__(self):
		return self.name + " - " + self.location