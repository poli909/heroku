from django.db import models

class Group(models.Model) : 
    name = models.CharField(max_length=200)
    leader = models.CharField(max_length=50)
    create_date = models.DateField()
    location = models.CharField(max_length=200)
    introduce = models.CharField(max_length=1000)
    