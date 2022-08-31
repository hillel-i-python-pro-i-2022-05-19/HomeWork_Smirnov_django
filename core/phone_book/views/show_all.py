from phone_book.models import Phone_book
from django.views.generic import ListView

class PhoneBookListView(ListView):
    model = Phone_book
    template_name = 'show_all.html'
    context_object_name = 'phone_numbers'
