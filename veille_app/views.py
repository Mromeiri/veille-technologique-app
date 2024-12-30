# <<<<<<< HEAD
# # from django.shortcuts import render
# # from django.contrib.auth.decorators import login_required
# # from django.contrib.auth.views import LoginView
# # from django.urls import reverse_lazy

# # # Create your views here.
# # @login_required
# # def index(request):
# #     # Fetch stats
# #     context = {
# #         # You can add stats to the context here
# #     }
# #     return render(request, 'index.html', context)

# # class Login(LoginView):
# #     template_name = 'auth-login-basic.html'

# #     def form_valid(self, form):
# #         # After login, redirect to the admin page
# #         return super().form_valid(form)

# #     def get_success_url(self):
# #         # You can customize the success URL here
# #         return reverse_lazy('admin:index')  # Redirect to Django Admin


# # from .models import Task

# # def kanban_board(request):
# #     tasks = Task.objects.all()  # Get all tasks
# #     context = {
# #         'tasks': tasks,
# #     }
# #     return render(request, 'kanban_board.html', context)


# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import LoginView
# from .models import Task

# # Create your views here.
# @login_required
# def index(request):
#     tasks_todo = Task.objects.filter(is_completed=False, is_in_progress=False)
#     tasks_in_progress = Task.objects.filter(is_in_progress=True)
#     tasks_completed = Task.objects.filter(is_completed=True)
    
#     context = {
#         'tasks_todo': tasks_todo,
#         'tasks_in_progress': tasks_in_progress,
#         'tasks_completed': tasks_completed,
#     }
#     return render(request, 'index.html', context)

# class Login(LoginView):
#     template_name = 'auth-login-basic.html'

#     def form_valid(self, form):
#         # Add any extra logic here if needed
#         return super().form_valid(form)
    

# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Task
# import json

# @csrf_exempt
# def update_task_status(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         task_id = data.get('task_id')
#         status = data.get('status')

#         # Update the task status
#         task = Task.objects.get(id=task_id)
#         task.status = status
#         task.save()

#         return JsonResponse({'success': True})
# =======




# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import LoginView
# from django.urls import reverse_lazy

# # Create your views here.
# @login_required
# def index(request):
#     # Fetch stats
#     context = {
#         # You can add stats to the context here
#     }
#     return render(request, 'index.html', context)

# class Login(LoginView):
#     template_name = 'auth-login-basic.html'

#     def form_valid(self, form):
#         # After login, redirect to the admin page
#         return super().form_valid(form)

#     def get_success_url(self):
#         # You can customize the success URL here
#         return reverse_lazy('admin:index')  # Redirect to Django Admin


# from .models import Task

# def kanban_board(request):
#     tasks = Task.objects.all()  # Get all tasks
#     context = {
#         'tasks': tasks,
#     }
#     return render(request, 'kanban_board.html', context)


from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .models import Content, Task

# Create your views here.
@login_required
def index(request):
     # Check if the logged-in user is in the 'decideur' group
    if request.user.groups.filter(name='Décideur').exists():
        # If user is in 'decideur' group, fetch all tasks
        tasks = Task.objects.all()
        tasks_todo = tasks.filter(status='To Do')
        tasks_in_progress = tasks.filter(status='In Progress')
        tasks_completed = tasks.filter(status='Completed')

    else:
        # If user is not in 'decideur' group, fetch tasks assigned to the logged-in user
        if request.user.groups.filter(name='Veilleur').exists():
        # If user is in 'decideur' group, fetch all tasks
        
            return redirect(veilleur_view)
        

    return render(request, 'kanban.html', {'tasks': tasks,'tasks_todo':tasks_todo,'tasks_in_progress':tasks_in_progress,'tasks_completed':tasks_completed})

class Login(LoginView):
    template_name = 'auth-login-basic.html'

    def form_valid(self, form):
        # Add any extra logic here if needed
        return super().form_valid(form)
    
from django.shortcuts import render
from .models import Task


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import Group
from .models import Task

@login_required
def kanban_view(request):

    # Check if the logged-in user is in the 'decideur' group
    if request.user.groups.filter(name='Décideur').exists():
        # If user is in 'decideur' group, fetch all tasks
        tasks = Task.objects.all()
        
    else:
        if request.user.groups.filter(name='Veilleur').exists():
        # If user is in 'decideur' group, fetch all tasks
        
            return redirect(veilleur_view)

    return render(request, 'kanban.html', {'tasks': tasks})

# @login_required
# def kanban_view(request):
#     # Get tasks assigned to the logged-in user
#     tasks = Task.objects.filter(assignments__user=request.user).prefetch_related('assignments__user')

#     return render(request, 'kanban.html', {'tasks': tasks})



import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task, TaskStatus


@csrf_exempt  # You might need to remove this in production and use proper CSRF token handling
def update_task_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        task_id = data.get('task_id')
        new_status = data.get('status')
        if new_status== "in-progress-column":
            new_status = "In Progress"
        elif new_status== "to-do-column":
            new_status = "To Do"
        else :
            new_status = "Completed"
        print(new_status)
        try:
            task = Task.objects.get(id=task_id)
            task.status = new_status
            task.save()
            return JsonResponse({'success': True, 'message': 'Task status updated.'})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Task not found.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


@login_required
def veilleur_view(request):
    # Get tasks assigned to the logged-in user
    tasks = Task.objects.filter(assignments__user=request.user).prefetch_related('assignments__user')
    
    tasks_todo = tasks.filter(status='To Do')
    tasks_in_progress = tasks.filter(status='In Progress')
    tasks_completed = tasks.filter(status='Completed')

    return render(request, 'veilleur.html', {'tasks': tasks,'tasks_todo':tasks_todo,'tasks_in_progress':tasks_in_progress,'tasks_completed':tasks_completed})


def task_content(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    # Fetch all content related to the task's source
    contents = Content.objects.filter(source__task=task)
    return render(request, 'task_content.html', {'task': task, 'contents': contents})
# >>>>>>> origin/main
