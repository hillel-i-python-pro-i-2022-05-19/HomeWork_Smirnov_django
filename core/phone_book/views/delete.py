from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from phone_book.models import Phone_book

class PhoneBookDeleteView(DeleteView):
    model = Phone_book
    template_name = 'phone_book_confirm_delete.html'
    success_url = reverse_lazy('show_all')




# def delete(request, pk):
#     total_deleted, _ = Phone_book.objects.filter(pk=pk).delete()

#     return reverse_lazy('show_all')
