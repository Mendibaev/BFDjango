from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404, HttpResponseForbidden
from main.models import Task_List, Task
from main.forms import TaskListForm, TaskForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import FormMixin, SingleObjectMixin
import datetime

app_name = 'main'

class IndexView(FormMixin, ListView):
	model = Task_List
	form_class = TaskListForm
	template_name = "main/index.html"

	def get_success_url(self):
		return redirect('/todos/')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['latest_task_list'] = Task_List.objects.all().order_by('-created_at')
		context['form'] = self.get_form()
		return context

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		# Here, we would record the user's interest using the message
		# passed in form.cleaned_data['message']
		return super().form_valid(form)

class TodoListView(LoginRequiredMixin, FormMixin, DetailView):
	model = Task
	form_class = TaskForm
	template_name = "main/todo_list.html"
	redirect_field_name = "/todos/"

	def get_success_url(self):
		return redirect('/todos/'+str(self.object.pk)+'/')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		task_list = Task_List.objects.get(pk=self.object.pk)
		context['task_list'] = task_list
		tasks = task_list.tasks.all()
		context['tasks'] = tasks
		context['form'] = self.get_form()
		return context

	def post(self, request, *args, **kwargs):
		return FormView.post(self, request, *args, **kwargs)
		if not request.user.is_authenticated:
			return HttpResponseForbidden()
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)

	def form_valid(self, form):
		# Here, we would record the user's interest using the message
		# passed in form.cleaned_data['message']
		return super().form_valid(form)

class CompletedTodoListView(LoginRequiredMixin, DetailView):
	model = Task
	template_name = "main/completed_todo_list.html"
	redirect_field_name = "/todos/"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		task_list = Task_List.objects.get(pk=self.object.task_list_id)
		context['task_list'] = task_list
		tasks = task_list.tasks.all()
		context['tasks'] = tasks
		return context

def deleteList(request, task_list_id):
	if(request.POST.get('deleteListBtn')):
		Task_List.objects.get(pk=task_list_id).delete()
	return redirect('/todos/')