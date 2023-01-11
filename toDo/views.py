from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.viewsets import ModelViewSet
from .serializers import toDoserializer
from .models import toDo
from rest_framework import status
from rest_framework.status import *
from rest_framework import permissions
# Create your views here.




todo={
    '1':'Cook Food',
    '2':'Watch Movies',
    '3':'Do Laundry',
    '4':'Go Shopping'

}

class toDoList(APIView):
    def get(self,request,*args,**kwargs):
        return Response(todo)
    


#CRUD
#Create, Update, Delete, Detail , List
class toDoListViewset(ModelViewSet):
    serializer_class=toDoserializer #define serializer class
    queryset=toDo.objects.all() #tells model to fetch everything
    # permission_classes=[permissions.AllowAny]

    def list(self, request):

        todo_List=toDo.objects.all()
        SerializedToDoList=toDoserializer(todo_List,many=True)
        return Response(data={
            'message':'ToDo List has been fetched Successfully!',
            'data':SerializedToDoList.data
        },status=HTTP_200_OK)
 
