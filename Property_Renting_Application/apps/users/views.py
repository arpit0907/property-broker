from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from users.forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView,View
from property.models import Profile,Property
from django.contrib.auth.models import User


class SignupView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = 'registration/signup.html'

    success_url = '/login'

    def form_valid(self, form):

        user = form.save()
        profile,created = Profile.objects.get_or_create(user=user,address=form.data.get('address'),city=form.data.get('city'),state=form.data.get('state'),roles=form.data.get('roles'),profile_image=form.files.get('profile_image'),gender=form.data.get('gender'),phone=form.data.get('phone'),date_of_birth=form.data.get('date_of_birth'))
        
        return super(SignupView, self).form_valid(form)

    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         import pdb; pdb.set_trace()
    #         user =form.save()

    #         user.profile.gender = form.cleaned_data.get('gender')
    #         user.profile.save()
    #         username = form.cleaned_data.get('username')
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return redirect('login')
    # else:
    #     form = SignUpForm()
    # return render(request, 'signup.html', {'form': form})

class Dashboard(View):
    def get(self,request):
        return render(request,'dashboard.html')
#         if request.user.profile.roles == "Owner":
#             profile_owner = request.user.profile.roles
#             context = {'profile_owner' : profile_owner}

#         elif request.user.profile.roles == "Renter":
#             profile_renter = request.user.profile.roles
#             context = {'profile_renter' :profile_renter}
#             return render(request,'dashboard/dash.html',context)   

        # property_role = Profile.objects.filter(roles=request.user.profile.roles)
        # #for objects in property_role
        # context = {'property_role':property_role}

        # import pdb; pdb.set_trace()
        # return render(request,'dashboard.html',context)




def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect('users:dashboard')
