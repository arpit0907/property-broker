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
   path('intrested/renter',intrested_renter_list,name='intrested-renter-list'),

]
ajaxpatterns = [
   
    path('ajax/property/intrested/',property_renter_intrested,name='property-renter-intreted'),
]    

urlpatterns = urlpatterns + ajaxpatterns