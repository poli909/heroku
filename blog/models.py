from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model) : 
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    body = models.TextField()
    
    def __str__(self) :
        return self.title
        
    def summary(self) : 
        return self.body[0:100]

class Comment(models.Model) : 
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete = models.CASCADE) 
    body = models.CharField(max_length=500)

    def __str__(self) :
        return self.title

