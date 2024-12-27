from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
@login_required
def index(request):
    # Fetch stats
    context = {
        # You can add stats to the context here
    }
    return render(request, 'index.html', context)

class Login(LoginView):
    template_name = 'auth-login-basic.html'

    def form_valid(self, form):
        # After login, redirect to the admin page
        return super().form_valid(form)

    def get_success_url(self):
        # You can customize the success URL here
        return reverse_lazy('admin:index')  # Redirect to Django Admin
