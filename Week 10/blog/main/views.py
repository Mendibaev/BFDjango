from django.shortcuts import render, redirect
from django.http import Http404
from main.models import Post, Comment
from main.forms import PostForm, CommentForm
import datetime

app_name = 'main'

def index(request):
	latest_post_list = Post.objects.order_by('-created_at')
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/blog/')
	else:
		form = PostForm()
	context = {
		'latest_post_list': latest_post_list,
		'form': form
	}
	return render(request, 'main/index.html', context)

def post_details(request, post_list_id):
	try:
		latest_post = Post.objects.get(id=post_list_id)
	except Post.DoesNotExist:
		raise Http404("Post not found")
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/blog/'+str(post_list_id)+'/')
	else:
		form = CommentForm()
	context = {
		'latest_post': latest_post,
		'comments': latest_post.comments.all(),
		'form': form
	}
	return render(request, 'main/detail.html', context)