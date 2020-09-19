from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserForm(UserCreationForm):
	first_name=forms.CharField(max_length=30)
	last_name=forms.CharField(max_length=30)
	email=forms.EmailField(max_length=50)
	class Meta:
		model=User
		fields=['first_name','last_name','username','password1','password2','email']

class ReportForm(forms.ModelForm):
	inc_type=(('environmental_incident','Environmental Incident'),
		('injury','Injury/Illness'),
		('property_dammage','Property Damage'),
		('vehicle','Vehicle')
		)
	
	incident_type=forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=inc_type)

	class Meta:
		model=Report
		exclude=['user','reported_by']
