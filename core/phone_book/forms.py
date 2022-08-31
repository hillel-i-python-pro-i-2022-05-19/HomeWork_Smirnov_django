from django.forms import ModelForm
from .models import Phone_book

class PhoneBookCreationForm(ModelForm):
    class Meta:
        model = Phone_book
        fields = ['name', 'value', 'country_code', 'work_info', 'email']