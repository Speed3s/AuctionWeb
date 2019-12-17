from django import forms
from datetime import datetime
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from .models import UserModel, Items
from django.views.decorators.csrf import csrf_exempt
User_model = UserModel
    #specify date from 1960 to 2019
NUM_YEARS = [x for x in range(1960, 2019)]

class UserLogin(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'password')
        widgets = {
                    'username': forms.TextInput(attrs={
                    'placeholder':"Please enter your username...",
                    'class': 'form-control',
                }),
            'password' : forms.TextInput(attrs={
                'placeholder': 'Enter Your Password',
                'type': 'password',
                'class': 'form-control',
            })
        }
class ExtendedRegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'email', 'password','location','date_of_birth')
        widgets = {
            'date_of_birth': forms.TextInput(attrs = {
                'placeholder': "dd-mm-yyyy",
                'type': "date",
                'class': "form_control",

            }),
            'password' : forms.TextInput(attrs={
                'placeholder': 'Password',
                'type': 'password',
                
            })
        }
class ItemForm(forms.ModelForm):
    class Meta: 
        model = Items
        fields = ('itemName', 'itemDescription', 'itemPrice', 'itemAuctonEnd', 'itemImage')
        description = forms.CharField(widget = forms.Textarea(attrs={"rows": 1, "cols": 10, "class":"form-control"}))
        widgets = {
            'itemName': forms.TextInput(attrs={
                'placeholder': 'Title of item...',
                'class': 'form-control',
            }),
            'itemDescription': forms.Textarea(attrs={
                'placeholder': 'Description of item...',
                'class': 'form-control',
            }),
            'itemPrice': forms.TextInput(attrs={
                'placeholder': 'Item Price...',
                'type': 'number',
                'class': 'form-control',
            }),
            'itemAuctonEnd': forms.TextInput(attrs={
                'placeholder': 'End date...',
                'type': "date",
                'class':'form-control',
            }),
        }
