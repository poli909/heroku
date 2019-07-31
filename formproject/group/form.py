from django import forms
from .models import Group

class GroupForm(forms.ModelForm) : 
    class Meta : 
        model = Group
        fields = ("name" , "leader", "create_date" , "location" , "introduce")