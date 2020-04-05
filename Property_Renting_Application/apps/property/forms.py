from django import forms 
from property.models import Property,Profile
from phonenumber_field.formfields import PhoneNumberField

class PropertyForm(forms.ModelForm):
    
    
    class Meta:
        model = Property
        fields = ('name','city','property_img','prize','size','address')


    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user','')
    #     super(PropertyForm, self).__init__(*args, **kwargs)
    #     self.fields['user_defined_code']=forms.ModelChoiceField(queryset=Profile.objects.filter(phone=phone))


    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if Property.objects.filter(name=name).exists():
    #         raise forms.ValidationError("You have already have name with same name")
    #     return name         