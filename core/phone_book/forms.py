from django.forms import ModelForm
from .models import Phone_book

class Phone_book_Form(ModelForm):
    class Meta:
        model = Phone_book
        fields = ('name', 'value',)