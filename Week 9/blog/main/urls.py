from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [

	# ex: /blog/
	path('', views.index, name='index'),
	# ex: /blog/1/
	path('<int:post_list_id>/', views.post_details, name='post_details'),

];