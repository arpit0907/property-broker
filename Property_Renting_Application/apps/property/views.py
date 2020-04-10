from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from property.models import *
from property.forms import PropertyForm

from django.contrib.auth.mixins import PermissionRequiredMixin


class PropertyCreateView(PermissionRequiredMixin,CreateView):
    permission_required = ('property.add_property',)
    raise_exception = True

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

