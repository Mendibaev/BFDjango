from django import forms
from main.models import Task_List, Task
from django.contrib.auth.models import User

app_name = 'main'

class TaskListForm(forms.ModelForm):
	class Meta:
		model = Task_List
		fields = ['name', 'owner', 'created_at']

class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ('task_list', 'name', 'created_at', 'due_on', 'owner', 'mark')