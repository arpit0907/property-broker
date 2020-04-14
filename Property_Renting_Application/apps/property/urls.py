from django.urls import path
from property.views import *
from .ajax import *

app_name = 'property'


urlpatterns = [
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