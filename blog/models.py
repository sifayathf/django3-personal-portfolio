from django.db import models

class Blog(models.Model):
    title =models.CharField(max_length=1000)
    description = models.CharField(max_length = 1000)
    blogpost = models.TextField(max_length = 10000)
    createddatetime = models.DateTimeField(auto_now_add= True)
