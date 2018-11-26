from django.shortcuts import get_object_or_404, render
from .models import Task_List, Task

def index(request):
	latest_task_list = Task_List.objects.order_by('-created_at')[:5]
	context = {'latest_task_list': latest_task_list}
	return render(request, 'main/index.html', context)

def todo_list(request, task_list_id):
	task_list = get_object_or_404(Task_List, pk=task_list_id)
	return render(request, 'main/todo_list.html', {'task_list': task_list})

def completed_todo_list(request, task_list_id):
	task_list = get_object_or_404(Task_List, pk=task_list_id)
	return render(request, 'main/completed_todo_list.html', {'task_list': task_list})