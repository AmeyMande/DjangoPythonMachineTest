from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at']

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField(read_only=True)
    users = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['project_name', 'client', 'users']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
