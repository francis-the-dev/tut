from django import forms
from .models import tutor_model

class tutor_form(forms.ModelForm):
    class Meta:
        model = tutor_model
        fields = ['number','expertise','unit','profile','price_per_hour','transcript']
        widgets = {'number':forms.TextInput(attrs={'maxlength':10,'id':'number','placeholder':'your number of contact'}),'expertise':forms.TextInput(attrs={'placeholder':'Course you are proficient in eg ELECTRICAL ENGEERING( in Capital)'}),'unit':forms.Textarea(attrs={'placeholder':'unit/units you can teach( in Capital)'}),'price_per_hour':forms.TextInput(attrs={'placeholder':'Enter price per hour (ksh) recommended ksh 50 and up'})}

    def save(self,current_user):
        data_obj = super().save(commit=False)
        data_obj.user = current_user
        return super().save(commit=True)
