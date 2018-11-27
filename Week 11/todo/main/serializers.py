from main.models import Task_List, Task
from rest_framework import serializers

app_name = 'main'

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=300)
    password = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField()

class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_List
        fields = ['id', 'name', 'owner', 'created_at']

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'task_list', 'name', 'created_at', 'due_on', 'owner', 'mark')