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


def property_approve_intrested(request):
    object_id = request.POST.get('object_id')
    user_id = request.POST.get('user_id')
    interested_user = Interested.objects.get(properties=object_id,user=user_id)
    if interested_user.approve == False: 
        interested_user.approve = True
        interested_user.save()
        status = False

    else:
        status = True

    return JsonResponse({'status':status})



