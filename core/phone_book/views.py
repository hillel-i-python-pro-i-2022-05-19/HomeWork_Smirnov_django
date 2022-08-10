from django.shortcuts import render, redirect, get_object_or_404
from .forms import Phone_book_Form
from .models import Phone_book


def show_all(request):
    phone_numbers = Phone_book.objects.all()
    return render(
        request,
        'show_all.html',
        {'phone_numbers': phone_numbers}
    )

def create(request):
    if request.POST:
        form = Phone_book_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(show_all)
    else:
        form = Phone_book_Form()

    return render(
        request,
        'create.html',
        {'form': form},
    )

def edit(request, pk):
    phone_book = get_object_or_404(Phone_book, pk=pk)

    if request.POST:
        form = Phone_book_Form(request.POST, instance=phone_book)
        if form.is_valid():
            form.save()
            return redirect(show_all)
    else:
        form = Phone_book_Form(instance=phone_book)

    return render(
        request,
        'create.html',
        {'form': form},
    )

def delete(request, pk):
    total_deleted, _ = Phone_book.objects.filter(pk=pk).delete()

    return redirect(show_all)
