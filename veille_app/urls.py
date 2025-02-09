# <<<<<<< HEAD
# from django.urls import path

# from django.contrib.auth import views as auth_views

# from veille_app.views import *

# urlpatterns = [
#     path('', index, name='index'),
#     path('accounts/login/', Login.as_view(), name='login'),
#     path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]
# =======
from django.urls import path

from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

from veille_app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('veilleur', veilleur_view, name='veilleur'),
    path('analyste', analyste_view, name='analyste'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('kanban/', kanban_view, name='kanban'),
    path('update_task_status/', update_task_status, name='update_task_status'),
    
    path('content/<int:task_id>/', task_content, name='task_content'),

    path('articles/', fetch_arxiv_articles, name='fetch_arxiv_articles'),
    path('save_article/', save_article, name='save_article'),
    path('delete_article/', delete_article, name='delete_article'),
    path('plosarticle/', fetch_plosone_articles, name='plos_article'),
    path('author-statistics/', author_statistics, name='author_statistics'),
    path('word-statistics/', word_statistics, name='word_statistics'),
    path('generate_report/', generate_report, name='generate_report'),


]
# >>>>>>> origin/main