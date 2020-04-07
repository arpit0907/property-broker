from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

Roles = (
    ('Owner', 'Owner'),
    ('Renter', 'Renter'),
)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254)

    phone = forms.CharField()
    profile_image = forms.FileField()
    address = forms.CharField(max_length=20)
    city = forms.CharField()
    state = forms.CharField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    date_of_birth = forms.DateField()
    roles = forms.ChoiceField(choices=Roles)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','address','city','state','roles','gender','date_of_birth','phone','profile_image')
          
