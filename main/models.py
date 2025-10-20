from django.db import models
from django.contrib.auth.models import User


class Poc(models.Model):
    title=models.CharField(max_length=20)
    content=models.FileField(upload_to='picpokcontent')
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    like=models.ManyToManyField(User,related_name='liked_poc')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    poc=models.ForeignKey(Poc, on_delete=models.CASCADE)
    text=models.TextField()
    coment_owner=models.ForeignKey(User, on_delete=models.CASCADE)
    comented_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    

class Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    bio=models.CharField(max_length=50)
    picture=models.ImageField(default='default.png',upload_to='profile_pictures')

    def __str__(self):
        return self.user