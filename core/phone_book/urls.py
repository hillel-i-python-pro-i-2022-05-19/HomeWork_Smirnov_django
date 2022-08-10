from xml.etree.ElementInclude import include
from django.urls import path, include
from phone_book.views import show_all, create, edit, delete

urlpatterns = [
    path('show_all/', view=show_all),
    path('create/', view=create),
    path('<pk>/', include([
        path('edit', view=edit),
        path('delete', view=delete),
    ])),
]
