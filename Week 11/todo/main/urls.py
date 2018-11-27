from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [

	# ex: /todos/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /todos/api/
	path('api/', views.todo_list, name='api_list_get_post'),
	# ex: /todos/api/
	path('api/<int:pk>/', views.todo_list_detail, name='api_list_put_delete'),
	# ex: /todos/1/api/
	path('<int:pk>/api/', views.tasks_list, name='api_tasks_list_get_post'),
	# ex: /todos/1/api/1/
	path('<int:pk>/api/<int:task_id>/', views.task_detail, name='api_task_detail_put_delete'),
	# ex: /todos/1/
	path('<int:pk>/', views.TodoListView.as_view(), name='todo_list'),
	# ex: /todos/1/completed/
	path('<int:pk>/completed/', views.CompletedTodoListView.as_view(), name='completed_todo_list'),
	# ex: /todos/1/deleteList/
	path('<int:task_list_id>/deletelist/', views.deleteList, name='delete_list'),
	path('login/', views.login)
];