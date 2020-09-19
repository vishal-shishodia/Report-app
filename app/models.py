from django.db import models
from django.contrib.auth.models import User
import datetime

class Report(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	location=(('headoffice','Corporate Headoffice'),
		('home','Home'),)
	location=models.CharField(max_length=20,choices=location,default='headoffice',null=False,blank=False)
	incident_description=models.CharField(max_length=200,null=False,blank=False,verbose_name='Description')
	date_time=models.DateTimeField(("Date"), default=datetime.datetime.today)
	incident_Location=models.CharField(max_length=50,verbose_name='Incident Location',null=True,blank=True)
	severity=(('minor','minor'),
		('moderate','moderate'),
		('critical','critical')
		)
	intial_severity=models.CharField(max_length=20,null=False,blank=False,choices=severity)
	cause=models.CharField(max_length=200)
	action_taken=models.CharField(max_length=200)
	reported_by=models.CharField(max_length=50,null=False,blank=False)
	incident_type=models.CharField(max_length=50)

	def __str__(self):
		return str(self.user.get_full_name())
