from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView

# Create your views here.
@login_required
def index(request):
    # Fetch stats
    


    # Send the stats to the template
    context = {
        

    }
    return render(request, 'index.html', context)

class Login(LoginView):
    template_name = 'auth-login-basic.html'

    def form_valid(self, form):
        # Add any extra logic here if needed
        return super().form_valid(form)