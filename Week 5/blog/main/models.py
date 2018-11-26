from django.db import models
from django.contrib.auth.models import User

app_name = 'main'

class Post(models.Model):
	class Meta:
		verbose_name = 'Post'
		verbose_name_plural = 'Posts'
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=1000)
	created_at = models.DateTimeField('date created')
	def __str__(self):
		return self.title

class Comment(models.Model):
	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comments'
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	text = models.CharField(max_length=1000)
	created_at = models.DateTimeField('date created')