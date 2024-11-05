from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    todo = models.TextField()

    def __str__(self):
        return self.todo
