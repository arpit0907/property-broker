from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from users.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView,View
from property.models import Profile,Property
from django.contrib.auth.models import User

import logging
from django.http import HttpResponse

# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger('django')
 


class SignupView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    success_url = '/login'

    def form_valid(self, form):
        user = form.save()

        profile,created = Profile.objects.get_or_create(user=user,address=form.data.get('address'),city=form.data.get('city'),state=form.data.get('state'),roles=form.data.get('roles'),profile_image=form.files.get('profile_image'),gender=form.data.get('gender'),phone=form.data.get('phone'),date_of_birth=form.cleaned_data.get('date_of_birth'))
        
        return super(SignupView, self).form_valid(form)

class Dashboard(View):
    def get(self,request):
        return render(request,'dashboard.html')


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect('users:dashboard')

def loggers(request):
    # Send the Test!! log message to standard out
    logger.error("Test!!")
    return HttpResponse("Hello logging world.")
