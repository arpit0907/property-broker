from django import forms 
from property.models import Property,Profile
<<<<<<< HEAD

=======
from django.core.exceptions import ValidationError
>>>>>>> 3673c9c91c38dedfcda61ad57b684c92ebc756ec

class PropertyForm(forms.ModelForm):
    
    
    class Meta:
        model = Property
        fields = ('name','city','size','prize','address','property_img')


    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user','')
    #     super(PropertyForm, self).__init__(*args, **kwargs)
    #     self.fields['user_defined_code']=forms.ModelChoiceField(queryset=Profile.objects.filter(phone=phone))


    # def clean_address(self):
    #     address = self.cleaned_data['address']
        
    #     if address != ' ': 
    #         raise forms.ValidationError("Please fill address")
    #     return address         


    # def clean_property_img(self):
    #     property_img = self.cleaned_data['property_img']
    #     if property_img != '': 
    #         raise forms.ValidationError("Please select the image of property")
    #     return property_img       