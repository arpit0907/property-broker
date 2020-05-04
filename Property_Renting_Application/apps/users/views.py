from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from users.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView,View
from property.models import Profile,Property
from django.contrib.auth.models import User
import requests
from django.conf import settings
from social_django.models import UserSocialAuth

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


def instagram(request):

    data = {'client_id':settings.SOCIAL_AUTH_INSTAGRAM_KEY, "client_secret":settings.SOCIAL_AUTH_INSTAGRAM_SECRET, "grant_type":"authorization_code", "redirect_uri":'https://92a0c747.ngrok.io/insta', "code": request.GET['code']}
    res = requests.post('https://api.instagram.com/oauth/access_token', data=data)
    result = requests.get("https://graph.instagram.com/"+str(res.json()['user_id'])+"?fields=id,username&access_token=" + str(res.json()['access_token']))
    import pdb; pdb.set_trace()



#     response = requests.get("https://graph.instagram.com)/#{@result["user_id"]}?fields=id,username&access_token=#{@result["access_token"]}")

# def instagram_callback(request):
#     import pdb; pdb.set_trace()
#     return render(request, 'registration/test.html', {'access_token' : 'access_token'})

