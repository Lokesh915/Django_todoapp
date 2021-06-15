from django.contrib import admin

# Register your models here.
from todoapp.models import TodoModel

admin.site.register(TodoModel)