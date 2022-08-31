from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from phone_book.models import Phone_book

class PhoneBookCreateView(CreateView):
    model = Phone_book
    fields = ['name', 'value', 'country_code', 'work_info', 'email']
    template_name = 'create.html'

    success_url = reverse_lazy('show_all')
