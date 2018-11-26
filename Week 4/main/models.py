import datetime

from django.db import models
from django.contrib.auth.models import User

class Task_List(models.Model):
	name = models.CharField(max_length=200)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	created_at = models.DateTimeField('date created')
	def __str__(self):
		return self.name

class Task(models.Model):
	task_list = models.ForeignKey(Task_List, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	created_at = models.DateTimeField('date created')
	due_on = models.DateTimeField('deadline')
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	mark = models.BooleanField(default=False)