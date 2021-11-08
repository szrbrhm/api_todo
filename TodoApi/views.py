from django.shortcuts import render
from django.http.response import HttpResponse
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>')

@api_view()
def todoList(request):
    queryset = Todo.objects.all()
    
    serializer = TodoSerializer(queryset, many=True)
    return Response(serializer.data)