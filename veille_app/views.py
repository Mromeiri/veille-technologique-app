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




# VEILLLEUR ----


import requests 
import xml.etree.ElementTree as ET
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from .forms import ArxivSearchForm,ScholarSearchForm,ScholarsemSearchForm,PLOSOneSearchForm  
from .models import SavedArticle, DeletedArticle
from scholarly import scholarly
import pdfplumber  
from bs4 import BeautifulSoup 




def fetch_arxiv_articles(request):
    articles = []  
    form = ArxivSearchForm(request.GET or None)  

    if form.is_valid():
        mot_cle = form.cleaned_data['mot_cle']
        date_debut = form.cleaned_data['date_debut']
        date_fin = form.cleaned_data['date_fin']

        
        url = f"http://export.arxiv.org/api/query?search_query=all:{mot_cle}&start=0&max_results=10"
        response = requests.get(url)

        if response.status_code == 200:
            root = ET.fromstring(response.content)

            for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
                title = entry.find("{http://www.w3.org/2005/Atom}title").text
                summary = entry.find("{http://www.w3.org/2005/Atom}summary").text
                authors = [author.find("{http://www.w3.org/2005/Atom}name").text for author in entry.findall("{http://www.w3.org/2005/Atom}author")]
                link = entry.find("{http://www.w3.org/2005/Atom}link[@rel='alternate']").attrib['href']
                pdf_link = f"{link.replace('abs', 'pdf')}"

                published = entry.find("{http://www.w3.org/2005/Atom}published").text
                pub_date = datetime.strptime(published, "%Y-%m-%dT%H:%M:%S%z").date()

                if not DeletedArticle.objects.filter(link=link).exists():
                    is_saved = SavedArticle.objects.filter(link=link).exists()
                    if date_debut <= pub_date <= date_fin:
                        article_content = None
                        try:
                            # Télécharger et extraire le contenu du PDF
                            pdf_response = requests.get(pdf_link)
                            if pdf_response.status_code == 200:
                                with open("temp.pdf", "wb") as f:
                                    f.write(pdf_response.content)
                                with pdfplumber.open("temp.pdf") as pdf:
                                    article_content = "\n".join(page.extract_text() for page in pdf.pages)
                        except Exception as e:
                            article_content = f"Impossible d'extraire le contenu : {e}"

                        articles.append({
                            'title': title,
                            'summary': summary,
                            'authors': authors,
                            'link': link,
                            'published': pub_date,
                            'is_saved': is_saved,
                            'content': article_content
                        })
        else:
            return render(request, 'error.html', {'error_message': f"Erreur lors de la requête. Statut : {response.status_code}"})

    return render(request, 'articles.html', {'form': form, 'articles': articles})


def save_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        link = request.POST.get('link')
        content = request.POST.get('content')  
        summary = request.POST.get('summary')  

       
        SavedArticle.objects.get_or_create(
            title=title,
            link=link,
            content=content, 
            summary=summary  
        )

        return JsonResponse({'message': 'Article saved successfully!'})
    return JsonResponse({'message': 'Invalid request'}, status=400)



def delete_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        link = request.POST.get('link')

       
        DeletedArticle.objects.get_or_create(title=title, link=link)

        return JsonResponse({'message': 'Article deleted successfully!'})
    return JsonResponse({'message': 'Invalid request'}, status=400)



def fetch_plosone_articles(request):
    articles = [] 
    form = PLOSOneSearchForm(request.GET or None)  # Initialiser le formulaire

    if form.is_valid():
        mot_cle = form.cleaned_data['mot_cle']
        url = f"https://api.plos.org/search?q=title:{mot_cle}&wt=json&rows=10"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            docs = data.get('response', {}).get('docs', [])

            for doc in docs:
                link = f"https://journals.plos.org/plosone/article?id={doc.get('id')}"

                
                if DeletedArticle.objects.filter(link=link).exists():
                    continue

                
                is_saved = SavedArticle.objects.filter(link=link).exists()

                
                content = ''
                try:
                    article_page = requests.get(link)
                    if article_page.status_code == 200:
                        soup = BeautifulSoup(article_page.content, 'html.parser')

                        
                        introduction_section = soup.find('section', {'class': 'intro'})
                        
                        if not introduction_section:
                            
                            introduction_section = soup.find('section', {'id': 'article-introduction'})
                            
                        if introduction_section:
                            
                            content = introduction_section.get_text(separator="\n", strip=True)
                        else:
                           
                            content = soup.get_text(separator="\n", strip=True)
                            
                except requests.exceptions.RequestException as e:
                    content = f"Erreur lors de la récupération du contenu : {str(e)}"

                
                articles.append({
                    'title': doc.get('title_display', 'No Title'),
                    'authors': doc.get('author_display', []),
                    'journal': doc.get('journal', 'Unknown Journal'),
                    'link': link,
                    'published': doc.get('publication_date', 'Unknown Date'),
                    'summary': doc.get('abstract', 'No Abstract'),
                    'content': content, 
                    'is_saved': is_saved, 
                })
        else:
            return render(request, 'error.html', {'error_message': f"Erreur lors de la requête. Statut : {response.status_code}"})

    return render(request, 'plosone_articles.html', {'form': form, 'articles': articles})
