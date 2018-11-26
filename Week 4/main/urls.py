from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [

	# ex: /todos/
	path('', views.index, name='index'),
	# ex: /todos/1/
	path('<int:task_list_id>/', views.todo_list, name='todo_list'),
	# ex: /todos/1/completed/
	path('<int:task_list_id>/completed/', views.completed_todo_list, name='completed_todo_list'),

];