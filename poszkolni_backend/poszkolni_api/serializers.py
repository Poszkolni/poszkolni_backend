from rest_framework import serializers
from .models import Todo_list_model 

class Todo_list_serializer(serializers.ModelSerializer):
    class Meta:
        model = Todo_list_model
        fields = '__all__'