from django.db import models

# Create your models here.

class Task(models.Model):
     task_type = models.CharField(max_length=50)
     description = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at =  models.DateTimeField(auto_now=True)

#  def __str__(self):
#         return self.description

class Catalogue(models.Model):
    pass
    # id = models.IntegerField(primary_key=True)
    # task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    # name = models.Textfield()
    # description = models.TextField()
    # offers = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at =  models.DateTimeField(auto_now=True)



