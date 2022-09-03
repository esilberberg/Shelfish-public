from django import forms
from django.forms import ModelForm
from .models import *

class AddBook(ModelForm):

       class Meta:
              model = Book
              #author field is not shown to avoid drop down menu
              fields = '__all__'
              exclude = ('author',)
              labels = {
                     'pub_year': 'Publication Year',
                     'cover_url': 'Cover Image URL',
                     'location': 'Current Location',
                     }
              help_texts = {
                     'language': 'Ctrl+click to add more than one.',
                     'classification': 'Ctrl+click to add more than one.',
                     }

class AddAuthor(ModelForm):
       class Meta:
              model = Author
              fields = ('first_name', 'surname', 'birth_year', 'death_year',)       

       # author_options = forms.ModelChoiceField(
       #        queryset=Author.objects.all(),
       #        to_field_name='surname',
       #        required=True,  
       #        widget=forms.Select(attrs={'class': 'form-control'})
       # )