from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['title','created_at','due_date','completed']
    list_filter  = ['title','completed']
    search_fields = ['title']

admin.site.register(Task,TaskAdmin)