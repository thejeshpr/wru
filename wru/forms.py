import datetime

from django import forms
from django.forms import ModelForm

from .models import Entry, Feeling, Place

class PlaceForm(ModelForm):    
    class Meta:
        model = Place
        fields = [
            'name',
            'icon',
            'desc',
            'url',
            'image'
        ]


class FeelingForm(ModelForm):    
    class Meta:
        model = Feeling
        fields = [
            'name', 
            'icon'
        ]


class EntryForm(ModelForm):    
    class Meta:
        model = Entry
        fields = [
            'place', 
            'date',
            'feeling',
            'why',
            'tags',
            'desc'
        ]
    date = forms.DateField(
        # input_formats=['%d-%m-%Y'],
        initial=datetime.date.today
    )