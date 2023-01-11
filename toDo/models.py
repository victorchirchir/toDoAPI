from django.db import models

# Create your models here.

class toDo(models.Model):
    task=models.CharField(max_length=100,db_index=True,help_text='The task to be done') #default null=false,blank=false
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    compleated=models.BooleanField(default=False,help_text='The Status of the Task')



    class Meta:
        verbose_name='Todo List'
        verbose_name_plural='Todo Lists'


    def __str__(self) -> str:
        return self.task