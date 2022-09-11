from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from phone_book.models import Phone_book

class PhoneBookEditView(UpdateView):
    model = Phone_book
    fields = ['name', 'value', 'country_code', 'work_info', 'email']
    template_name = 'phone_book_form.html'
    success_url = reverse_lazy('show_all')
