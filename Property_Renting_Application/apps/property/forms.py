from django import forms 
from property.models import Property,Profile


class PropertyForm(forms.ModelForm):
    
    
    class Meta:
        model = Property
        fields = ('name','city','size','prize','address','property_img')


    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user','')
    #     super(PropertyForm, self).__init__(*args, **kwargs)
    #     self.fields['user_defined_code']=forms.ModelChoiceField(queryset=Profile.objects.filter(phone=phone))


    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if Property.objects.filter(name=name).exists():
    #         raise forms.ValidationError("Name already loaded")
    #     return name         