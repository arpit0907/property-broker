"""Property_Renting_Application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
#from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns


urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#i18n_patterns used for multilanguage purpose

# urlpatterns += i18n_patterns(
#     path('admin/', admin.site.urls),
#     path('', include('property.urls', namespace='property')),
#     path('', include('users.urls', namespace='users')),
#     path('login/', LoginView.as_view(template_name='registration/login.html'), name="login"),
#     path('logout/', LogoutView.as_view(template_name= 'registration/login.html'), name="logout"),
#     path('change-password/',PasswordChangeView.as_view(template_name='registration/change-password.html',success_url = '/change-password/'),name='change_password'),
    
# # for social login    
#     path('oauth/', include('social_django.urls', namespace='social')),



# # for forget password
#     path('password_reset/',PasswordResetView.as_view(template_name='registration/password_rest.html'), name='password_reset'),
#     path('password_reset/done/',PasswordResetDoneView.as_view(template_name='registration/password_reset_message.html'), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
#     path('reset/done/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_complete'),
# )
urlpatterns +=[
    path('admin/', admin.site.urls),
    path('', include('property.urls', namespace='property')),
    path('', include('users.urls', namespace='users')),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name= 'registration/login.html'), name="logout"),
    path('change-password/',PasswordChangeView.as_view(template_name='registration/change-password.html',success_url = '/change-password/'),name='change_password'),
    
# for social login    
    path('oauth/', include('social_django.urls', namespace='social')),



# for forget password
    path('password_reset/',PasswordResetView.as_view(template_name='registration/password_rest.html'), name='password_reset'),
    path('password_reset/done/',PasswordResetDoneView.as_view(template_name='registration/password_reset_message.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_complete'),
]
