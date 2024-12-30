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

from veille_app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('veilleur', veilleur_view, name='veilleur'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('kanban/', kanban_view, name='kanban'),
    path('update_task_status/', update_task_status, name='update_task_status'),
    
    path('content/<int:task_id>/', task_content, name='task_content'),


]
# >>>>>>> origin/main