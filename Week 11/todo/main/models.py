import datetime

from django.db import models
from django.contrib.auth.models import User

app_name = 'main'

class TaskListManager(models.Manager):
	def for_user(self, user):
		return self.filter(id=user)

class Task_List(models.Model):
	class Meta:
		verbose_name = 'Task List'
		verbose_name_plural = 'Task Lists'
	name = models.CharField(max_length=200)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	created_at = models.DateTimeField('date created')
	objects = TaskListManager()
	def __str__(self):
		return self.name

class Task(models.Model):
	class Meta:
		verbose_name = 'Task'
		verbose_name_plural = 'Tasks'
	task_list = models.ForeignKey(Task_List, on_delete=models.CASCADE, related_name='tasks')
	name = models.CharField(max_length=200)
	created_at = models.DateTimeField('date created')
	due_on = models.DateTimeField('deadline')
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	mark = models.BooleanField(default=False)
	def __str__(self):
		return self.name