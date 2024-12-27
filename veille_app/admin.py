
# Register your models here.

from django.contrib import admin
from .models import Category, Source, Content, Task, Report

# Register models here
admin.site.register(Category)
admin.site.register(Source)
admin.site.register(Content)
admin.site.register(Task)
admin.site.register(Report)
