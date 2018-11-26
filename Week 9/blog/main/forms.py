from django import forms
from main.models import Post, Comment

app_name = 'main'

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['owner', 'title', 'description', 'created_at']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('post', 'owner', 'text', 'created_at')