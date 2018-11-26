from django.shortcuts import render, redirect
from django.http import Http404
from main.models import Task_List, Task
from main.forms import TaskListForm, TaskForm
import datetime

app_name = 'main'

def index(request):
	latest_task_list = Task_List.objects.order_by('-created_at')
	if request.method == 'POST':
		form = TaskListForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/todos/')
	else:
		form = TaskListForm()
	context = {
		'latest_task_list': latest_task_list,
		'form': form
	}
	return render(request, 'main/index.html', context)

def todo_list(request, task_list_id):
	try:
		task_list = Task_List.objects.get(id=task_list_id)
	except Task_List.DoesNotExist:
		raise Http404("Task List not found")
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/todos/'+str(task_list_id)+'/')
	else:
		form = TaskForm()
	context = {
		'task_list': task_list,
		'tasks': task_list.tasks.all(),
		'form': form
	}
	return render(request, 'main/todo_list.html', context)

def completed_todo_list(request, task_list_id):
	try:
		task_list = Task_List.objects.get(id=task_list_id)
	except Task_List.DoesNotExist:
		raise Http404("Task List not found")
	context = {
		'task_list': task_list,
		'tasks': task_list.tasks.all()
	}
	return render(request, 'main/completed_todo_list.html', context)

def deleteList(request, task_list_id):
	if(request.POST.get('deleteListBtn')):
		Task_List.objects.get(pk=task_list_id).delete()
	return redirect('/todos/')