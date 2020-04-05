from django.contrib import admin
# Register your models here.
from .models import Profile,Property,Interested

admin.site.register(Profile)
admin.site.register(Property)
admin.site.register(Interested)


