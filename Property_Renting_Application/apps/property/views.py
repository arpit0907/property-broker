from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from property.models import *
from property.forms import PropertyForm

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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     property = Property.objects.filter(created_by=self.request.user,name=self.object)
    #     context['property_list '] = property
        
    #     return context

class RenterListView(ListView):
    queryset = Profile.objects.filter(roles='Renter')
    template_name = 'property/renter_list.html'
    context_object_name = 'renters_list'
    # paginate_by = 10



    # def get_context_data(self, **kwargs):
    #     context = super(PropertyUpdateView, self).get_context_data(**kwargs)
    #     import pdb; pdb.set_trace()
    #     context['object'] = Property.objects.get(pk=self.kwargs['pk']).profile #whatever you would like
    #     return context

    # def get_object(self, queryset=None):
    #     obj = Property.objects.get(pk=self.kwargs['pk'])
    #     return obj

    # # An empty dict or add an initial data to your form
    # initial = {}
    # # And don't forget your success URL
    # # or use reverse_lazy by URL's name
    # # Or better, override get_success_url() method
    # # And return your success URL using reverse_lazy

    # def get_initial(self):
    #     """initialize your's form values here"""

    #     base_initial = super().get_initial()
    #     # So here you're initiazing you're form's data
   
    #     base_initial['dataset_request'] = Property.objects.get(user=self.request.user)
    #     Property.objects.filter(
    #         creator=self.request.user
    #     )
    #     return base_initial
    #     