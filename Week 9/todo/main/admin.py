from django.contrib import admin

from .models import Task, Task_List

class TaskInline(admin.TabularInline):
	model = Task
	extra = 3

class TaskListAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name']}),
		("Date Created", {'fields': ['created_at'], 'classes': ['collapse']}),
	]
	inlines = [TaskInline]
	list_display = ('name', 'owner', 'created_at')
	list_filter = ['created_at']
	search_fields = ['name']

admin.site.register(Task_List, TaskListAdmin)