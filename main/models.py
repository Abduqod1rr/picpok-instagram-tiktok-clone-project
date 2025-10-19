from django.db import models
from django.contrib.auth.models import User

class Poc(models.Model):
    title=models.CharField(max_length=20)
    content=models.FileField(upload_to='/picpokcontent')
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)