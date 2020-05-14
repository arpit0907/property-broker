from django.urls import path
from property.views import *
from .ajax import *


from .views import ghar, send_push
from django.views.generic import TemplateView
app_name = 'property'




urlpatterns = [
   path('ghar', ghar),
   path('send_push', send_push),
   path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/x-javascript')),


   path('add/property/',PropertyCreateView.as_view(),name='add-property'),
   path('property/list/',PropertyListView.as_view(),name='property-list'),
   path('property/update/<int:pk>', PropertyUpdateView.as_view(), name='property-update'),
   path('property/delete/<int:pk>', PropertyDeleteView.as_view(), name='property-delete'), 
   path('property/detail/<int:pk>', PropertyDetailView.as_view(), name='property-detail'),

   path('renter/list',RenterListView.as_view(),name='renter-list'),
   path('about/property',TemplateAboutusView.as_view(),name='about-us'),
   
   path('intrested/renter',intrested_renter_list,name='intrested-renter-list'),
   path('approve/renter',approve_renter_list,name='approve-renter-list'),

]
ajaxpatterns = [
   
    path('ajax/property/intrested/',property_renter_intrested,name='property-renter-intreted'),
    path('ajax/property/approve/',property_approve_intrested,name='property-approve-renter'),
]    

urlpatterns = urlpatterns + ajaxpatterns