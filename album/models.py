from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    picture = models.ImageField(upload_to = 'pictures')
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title