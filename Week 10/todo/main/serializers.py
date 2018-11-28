from main.models import Task_List, Task
from rest_framework import serializers

app_name = 'main'

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_List
        fields = ['id', 'name', 'owner', 'created_at']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task_list', 'name', 'created_at', 'due_on', 'owner', 'mark')