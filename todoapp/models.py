from django.db import models

class TodoModel(models.Model):
    name=models.CharField(max_length=30)
    text=models.CharField(max_length=100)


class Meta:
      db_table = "TodoModel"

