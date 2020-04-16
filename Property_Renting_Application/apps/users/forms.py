from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from bootstrap_datepicker_plus import DatePickerInput




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

    phone = forms.CharField(max_length=10)
    profile_image = forms.FileField()
    address = forms.CharField(max_length=20)
    city = forms.CharField()
    state = forms.CharField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    date_of_birth =forms.DateField()



    roles = forms.ChoiceField(choices=Roles)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','address','city','state','roles','gender','date_of_birth','phone','profile_image')
          
   
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        name = User.objects.filter(username=username)

        if name.count():
            raise  ValidationError("Username already exists")
        return username
 
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        mail = User.objects.filter(email=email)
        if mail.count():
            raise  ValidationError("Email already exists")
        return email
 

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if (phone.count != 10):  
            raise  ValidationError("Please enter 10 digit number")
        return phone



