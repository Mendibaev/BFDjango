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
	# ex: /todos/1/deleteList/
	path('<int:task_list_id>/deletelist/', views.deleteList, name='delete_list'),
	path('json_format/', views.todo_list_JSON_Format),
    path('json_format/<int:pk>/', views.todo_list_detail_JSON_Format),
	path('serializer_format/', views.todo_list_Serializer_Format),
    path('serializer_format/<int:pk>/', views.todo_list_detail_Serializer_Format)

];