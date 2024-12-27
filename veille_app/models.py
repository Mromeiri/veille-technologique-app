# from django.db import models

# class SavedArticle(models.Model):
#     title = models.CharField(max_length=500)
#     link = models.URLField(unique=True)
   

#     def __str__(self):
#         return self.title


# class DeletedArticle(models.Model):
#     title = models.CharField(max_length=500)
#     link = models.URLField(unique=True)

#     def __str__(self):
#         return self.title




# class CryptographyArticle(models.Model):
#     title = models.TextField()
#     date = models.DateField()
#     authors = models.TextField()
#     content = models.TextField()
#     keywords = models.TextField()
#     url = models.URLField()

#     def __str__(self):
#         return self.title





# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Source(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    category = models.ForeignKey(Category, related_name="sources", on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    summary = models.TextField(blank=True, null=True)
    source = models.ForeignKey(Source, related_name="contents", on_delete=models.CASCADE)
    date_fetched = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="contents", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    # assigned_to = models.ForeignKey(User, related_name="tasks", on_delete=models.SET_NULL, null=True)
    assigned_to = models.ManyToManyField(User, related_name="tasks", blank=True) 
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Report(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="reports", on_delete=models.CASCADE)
    related_task = models.ForeignKey(Task, related_name="reports", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title