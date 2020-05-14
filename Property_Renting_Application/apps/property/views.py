from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView,TemplateView
from property.models import *
from property.forms import PropertyForm





# for push notificaion
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from webpush import send_user_notification
import json

from django.http.response import HttpResponse
from django.views.decorators.http import require_GET


from django.shortcuts import render, get_object_or_404
from django.conf import settings




@require_GET
def ghar(request):
   webpush_settings = getattr(settings, 'WEBPUSH_SETTINGS', {})
   vapid_key = webpush_settings.get('VAPID_PUBLIC_KEY')
   user = request.user
   return render(request, 'ghar.html', {user: user, 'vapid_key': vapid_key})



@require_POST
@csrf_exempt
def send_push(request):
    try:
        body = request.body
        data = json.loads(body)

        if 'head' not in data or 'body' not in data or 'id' not in data:
            return JsonResponse(status=400, data={"message": "Invalid data format"})

        user_id = data['id']
        user = get_object_or_404(User, pk=user_id)
        payload = {'head': data['head'], 'body': data['body']}
        send_user_notification(user=user, payload=payload, ttl=1000)

        return JsonResponse(status=200, data={"message": "Web push successful"})
    except TypeError:
        return JsonResponse(status=500, data={"message": "An error occurred"})

####################################################

class PropertyCreateView(CreateView):

    model = Property
    form_class = PropertyForm   
    success_url = '/property/list/'

    def form_valid(self, form, **kwargs):
        
        property = form.save(commit=False)
        
        property.created_by = self.request.user
        property.save()
        return redirect(self.success_url)


class PropertyListView(ListView):
   
    model = Property
    template_name = 'property/property_list.html'
    

class PropertyUpdateView(UpdateView):
  
    model = Property
    form_class = PropertyForm
    template_name = 'property/property_form.html'
    success_url = '/property/list/'

class PropertyDeleteView(DeleteView):
   
    model = Property
    template_name = 'property/property_confirm_delete.html'
    success_url = '/property/list/'

class PropertyDetailView(DetailView):
   
    model = Property
    template_name = 'property/property_detail.html'


class RenterListView(ListView):
    
    queryset = Profile.objects.filter(roles='Renter')
    template_name = 'property/renter_list.html'
    context_object_name = 'renters_list'
    # paginate_by = 10
  
class TemplateAboutusView(TemplateView):    
    template_name  = 'property/about.html'  


def intrested_renter_list(request):
    intrested_renter = Interested.objects.filter(properties__created_by_id = request.user.id)
    context = {"intrested_renter":intrested_renter}
    return render(request,"property/intrested_renter.html",context)

def approve_renter_list(request):
    approve_renter = Interested.objects.filter(user = request.user.id,approve =True) 
     
    context = {"approve_renter":approve_renter}
    return render(request,"property/approve_renter.html",context)
