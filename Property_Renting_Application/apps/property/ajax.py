from django.http import  JsonResponse
from django.shortcuts import render, redirect
from property.models import *
from django.contrib.auth.models import User, Group, Permission
from django.conf import settings




def property_renter_intrested(request):
  
    property_id = request.POST.get('property_id')
    user_id = request.POST.get('user_id')
    interested,created = Interested.objects.get_or_create(properties_id=property_id,user_id=user_id)
    return JsonResponse({'created':created})

