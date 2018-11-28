from django.shortcuts import render, redirect
from django.http import Http404
from main.models import Task_List, Task
from main.forms import TaskListForm, TaskForm
from main.serializers import TaskListSerializer, TaskSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
import json

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

@csrf_exempt
def todo_list_JSON_Format(request):
    if request.method == 'GET':
        task_list = Task_List.objects.all()
        tasks = [ts.to_json() for ts in task_list]
        return JsonResponse(tasks, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        task_list = Task_List(id=data['id'], name=data['name'], owner=User.objects.first(), created_at=data['created_at'])
        task_list.save()
        return JsonResponse(task_list.to_json())

@csrf_exempt
def todo_list_detail_JSON_Format(request, pk):
    try:
        task_list = Task_List.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)
    if request.method == 'GET':
        return JsonResponse(task_list.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        task_list.name = data.get('name', task_list.name)
        task_list.owner = User.objects.first()
        task_list.created_at = data.get('created_at', task_list.created_at)
        task_list.save()
        return JsonResponse(task_list.to_json())
    elif request.method == 'DELETE':
        task_list.delete()
        return JsonResponse({'deleted': True}, status=204)

@api_view(['GET', 'POST'])
@csrf_exempt
def todo_list_Serializer_Format(request):
    if request.method == 'GET':
        task_list = Task_List.objects.all()
        serializer = TaskListSerializer(task_list, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE', 'PUT', 'GET'])
@csrf_exempt
def todo_list_detail_Serializer_Format(request, pk):
	try:
		task_list = Task_List.objects.get(pk=pk)
	except Task_List.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = TaskListSerializer(task_list)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = TaskListSerializer(task_list, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		task_list.delete()
		return HttpResponse(status=204)