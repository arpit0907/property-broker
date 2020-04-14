from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User,Group




# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

Roles = (
    ('Owner', 'Owner'),
    ('Renter', 'Renter'),
)
PROPERTY_TYPE =(
    ('Rent','For Rent'),
    ('Sale','For Sale'),
    )

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)
    class Meta:
       abstract = True

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    phone = models.CharField(max_length=12)
    profile_image = models.ImageField(upload_to='pic_folder')
    #profile_pic = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    state = models.CharField(max_length=100,null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(null=True, blank=True )
    roles = models.CharField(max_length=6, choices=Roles)
    
    
    def __str__(self):
        return self.user.username

class Property(BaseModel):
    name = models.CharField(max_length=25)
    size = models.CharField(max_length=21)
    property_img = models.ImageField(null=True, blank=True)
    address = models.CharField(max_length=100,null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    prize = models.CharField(max_length=8)
    type_of_property = models.CharField(max_length=4, choices=PROPERTY_TYPE ,null=True ,blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='property_created_by')

    def __str__(self):
        return self.name


class Interested(BaseModel):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_intrested')
    properties = models.ForeignKey(Property,on_delete=models.CASCADE,related_name='property_owner') 
    
    approve = models.BooleanField(null=True)
    

    def __int__(self):
        return self.properties.id




