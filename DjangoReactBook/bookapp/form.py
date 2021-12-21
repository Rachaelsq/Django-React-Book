from django.forms import forms
from django import forms
from .models import Books

#add image in to the fields
class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['name', 'author', 'description',]
    def clean_description(self):
        description = self.cleaned_data.get('description')
        
        #raise an error if description is too long
        if len(description) > 300:
            raise forms.ValidationError('This is too long')
        return description
    
