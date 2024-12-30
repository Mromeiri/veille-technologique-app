from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name



class TaskStatus(models.TextChoices):
    TODO = 'To Do', 'To Do'
    IN_PROGRESS = 'In Progress', 'In Progress'
    COMPLETED = 'Completed', 'Completed'

class TaskPriority(models.TextChoices):
    LOW = 'Low', 'Low Priority'
    MEDIUM = 'Medium', 'Medium Priority'
    HIGH = 'High', 'High Priority'
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()
    priority = models.CharField(
        max_length=50,
        choices=TaskPriority.choices,
        default=TaskPriority.MEDIUM,
    )
    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO,
    )

    def __str__(self):
        return self.title
class Source(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    category = models.ForeignKey(Category, related_name="sources", on_delete=models.CASCADE)
    task = models.ForeignKey(Task, related_name="sources", on_delete=models.CASCADE, null=True, blank=True)
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

class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, related_name="assignments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="assignments", on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} assigned to {self.task}"

class Report(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name="reports", on_delete=models.CASCADE)
    related_task = models.ForeignKey(Task, related_name="reports", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title