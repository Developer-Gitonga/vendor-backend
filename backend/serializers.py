from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


# class FormSerializer(ModelSerializer):
#     class Meta:
#         model = Form
#         fields = '__all__'