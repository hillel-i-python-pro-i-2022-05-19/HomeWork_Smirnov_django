from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

from phone_book.models import Phone_book

class PhoneBookDeleteView(DeleteView):
    model = Phone_book
    template_name = 'phone_book_confirm_delete.html'
    success_url = reverse_lazy('show_all')
