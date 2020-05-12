from property.views import *
from django.urls import path
from users.views import *
from django.views.generic import TemplateView


app_name = 'users'


urlpatterns = [
   # path('',Dashboard.as_view(), name='dashboard'),
   path('', index, name='index'),
   path('dashboard',login_required(Dashboard.as_view()), name='dashboard' ),

   path('board',TemplateView.as_view(template_name="dashboard/dash.html"),name="board"),
  
   path('signup/',SignupView.as_view(), name='signup'),

   path('logger', loggers, name='index'),


]


