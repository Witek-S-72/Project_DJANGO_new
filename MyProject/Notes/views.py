from django.shortcuts import render, get_object_or_404
from .models import Note, Category


# Create your views here.

def notes_list(request):
    lista = Note.objects.all()
    ctx = {'lista':lista}
    return render(request, 'notes/notes_lista.html', ctx)

def notes_detail(request, id):
    note = get_object_or_404(Note, id=id)
    ctx = {'note':note}
    return render(request, 'notes/notes_detail.html', ctx)

def category_list(request):
    cat_list = Category.objects.all()
    notes_count = Note.objects.all()
    counter = 0
    ctx = {'cat_list':cat_list, 'notes_count':notes_count, 'counter':counter}
    return render(request, 'notes/category_list.html', ctx)

def category_detail(request, id):
    cat_detail = get_object_or_404(Category, id=id)
    ctx = {'cat_detail':cat_detail}
    return render(request, 'notes/category_detail.html', ctx)


