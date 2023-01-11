#add your serializers
from rest_framework import serializers
from .models import toDo

#creating a serializer class to serialize our data from models to Json
class toDoserializer(serializers.ModelSerializer):


    class Meta:
        model=toDo
        fields='__all__'
        #you can use exclude when you don't want to list all the fields