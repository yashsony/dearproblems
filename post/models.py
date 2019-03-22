
from django.db import models
#from django.contrib.auth.models import User

from django.conf import settings

class post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    like = models.ForeignKey(post,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)




class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return self.comment


class search(models.Model):
    q = models.CharField(max_length=30)



