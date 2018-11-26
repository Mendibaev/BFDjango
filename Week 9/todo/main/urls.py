from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [

	# ex: /todos/
	path('', views.IndexView.as_view(), name='index'),
	# ex: /todos/1/
	path('<int:pk>/', views.TodoListView.as_view(), name='todo_list'),
	# ex: /todos/1/completed/
	path('<int:pk>/completed/', views.CompletedTodoListView.as_view(), name='completed_todo_list'),
	# ex: /todos/1/deleteList/
	path('<int:pk>/deletelist/', views.deleteList, name='delete_list'),

];