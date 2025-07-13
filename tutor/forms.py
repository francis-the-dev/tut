from django import forms
from .models import tutor_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 


# tutor model form
class tutor_form(forms.ModelForm):
    class Meta:
        model = tutor_model
        fields = ['number','expertise','unit','profile','price_per_hour','transcript']
        widgets = {'number':forms.TextInput(attrs={'maxlength':10,'id':'number','placeholder':'your number of contact'}),'expertise':forms.TextInput(attrs={'placeholder':'Course you are proficient in eg ELECTRICAL ENGEERING( in Capital)'}),'unit':forms.Textarea(attrs={'placeholder':'unit/units you can teach( in Capital)'}),'price_per_hour':forms.TextInput(attrs={'placeholder':'Enter price per hour (ksh) recommended ksh 50 and up'})}

    def save(self,current_user):
        data_obj = super().save(commit=False)
        data_obj.user = current_user
        return super().save(commit=True)



# login form
class CustomLoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'Username',
            'class': 'form-control',
            'id': 'user',
            
           
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
            'id': 'log'
        })
    )


# register
class customuserform(UserCreationForm):
    
    email = forms.EmailField( widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control',
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control',
        'id' : 'user'
    }))

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'form-control ib',
        'id': 'pass',
    }))
    
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'form-control',
        'id': 'id_password2',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
class search(forms.Form):
    query = forms.CharField( max_length=100, required=False ,widget=forms.TextInput(attrs={
        'class':'form-control search mt-5',
        'placeholder':'search for course or unit',
        'id':'search'

    }))
    
