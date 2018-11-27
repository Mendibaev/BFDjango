from django.shortcuts import render, redirect
from main.models import Task_List, Task
from main.forms import TaskListForm, TaskForm
from main.serializers import TaskListSerializer, TaskSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.generic import ListView, DetailView
import datetime

app_name = 'main'

def deleteList(request, task_list_id):
	if(request.POST.get('deleteListBtn')):
		Task_List.objects.get(pk=task_list_id).delete()
	return redirect('/todos/')

class IndexView(ListView):
	template_name = 'main/index.html'
	serializer_class = TaskListSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)

	def get_queryset(self):
		return Task_List.objects.all()

	context_object_name = 'latest_task_list'

class TodoListView(DetailView):
	model = Task_List
	template_name = 'main/todo_list.html'
	serializer_class = TaskSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

class CompletedTodoListView(DetailView):
	model = Task_List
	template_name = 'main/completed_todo_list.html'
	serializer_class = TaskSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

@api_view(['POST'])
def login(request):
	username = request.data.get('username')
	password = request.data.get('password')
	user = authenticate(username=username, password=password)
	if user is None:
		return Response({'error': 'Invalid data'})
	token, created = Token.objects.get_or_create(user=user)
	return Response({'token': token.key})

@api_view(['GET', 'POST'])
@csrf_exempt
def todo_list(request):
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
def todo_list_detail(request, pk):
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

@api_view(['GET', 'POST'])
@csrf_exempt
def tasks_list(request, pk):
    if request.method == 'GET':
        task_list = Task_List.objects.get(pk=pk)
        tasks = task_list.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['DELETE', 'PUT', 'GET'])
@csrf_exempt
def task_detail(request, pk, task_id):
	try:
		task_list = Task_List.objects.get(pk=pk)
		task = task_list.tasks.get(pk=task_id)
	except Task.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = TaskSerializer(task)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = TaskSerializer(task, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		task.delete()
		return HttpResponse(status=204)