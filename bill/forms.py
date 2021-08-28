from django.forms import ModelForm
from .models import temp

class billgenerator(ModelForm):
	class Meta:
		model = temp
		fields = '__all__'