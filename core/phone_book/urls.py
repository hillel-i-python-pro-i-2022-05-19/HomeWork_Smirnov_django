from xml.etree.ElementInclude import include
from django.urls import path, include
from phone_book.views.show_all import PhoneBookListView
from phone_book.views.create import PhoneBookCreateView
from phone_book.views.edit import PhoneBookEditView
from phone_book.views.delete import PhoneBookDeleteView

urlpatterns = [
    path('show_all/', PhoneBookListView.as_view(), name='show_all'),
    path('create/', PhoneBookCreateView.as_view(), name='create'),
    path('<pk>/', include([
        path('edit', PhoneBookEditView.as_view(), name='edit'),
        path('delete', PhoneBookDeleteView.as_view(), name='delete')]),
    )
]

