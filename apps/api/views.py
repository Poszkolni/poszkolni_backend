from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Todo_list_serializer
from .models import Todo_list_model


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<int:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<int:pk>/',

    }

    return Response(api_urls)


@api_view(['GET'])
def tasks_list(request):
    tasks = Todo_list_model.objects.all()
    serializer = Todo_list_serializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    tasks = Todo_list_model.objects.get(id=pk)
    serializer = Todo_list_serializer(tasks, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = Todo_list_serializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def task_update(request, pk):
    task = Todo_list_model.objects.get(id=pk)
    serializer = Todo_list_serializer(instance=post, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):
    task = Todo_list_model.objects.get(id=pk)
    task.delete()

    return Response('Task deleted!')