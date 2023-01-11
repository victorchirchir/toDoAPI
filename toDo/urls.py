from django.contrib import admin
from django.urls import path, include
from toDo.views import toDoList


# urlpatterns = [
#     path("", toDoList.as_view(),name='home' ),
# ]



#Routers
from rest_framework.routers import DefaultRouter
from .views import toDoListViewset


router=DefaultRouter()
router.register('',toDoListViewset,basename='todo-list')
urlpatterns=router.urls