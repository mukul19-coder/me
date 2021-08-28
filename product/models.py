from django.db import models

# Create your models here.
class product(models.Model):
	hsn = (
		('5806', '5806'),
		('6002', '6002'),		
		)
	name=models.CharField(max_length=100)
	description=models.CharField(max_length=100)
	category=models.CharField(max_length=100)
	hsn=models.CharField(max_length=100, choices=hsn, default="5806")

	def __str__(self):
		return self.description + " - " + self.name