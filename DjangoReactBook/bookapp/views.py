from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.http import JsonResponse
#model imports
from bookapp.models import Books
#form imports
""" from bookapp import BooksForm"""
from .form import BooksForm



#======================================
# HOME VIEW
#======================================
def home_view(request, *args, **kwargs):
    return render(request, 'pages/home.html', context={}, status=200)

#======================================
# LIST VIEW  
#======================================
def books_list(request, *args, **kwargs):
    blist = Books.objects.all()
    books = [{"id":x.id, "name":x.name, "author":x.author, "description":x.description} for x in blist]
    data = {
            "response" : books
    }
    return JsonResponse(data)

#======================================
# DETAIL VIEW api
#======================================
#this creates a view that displays the book ID and thus the book details
def book_detail_view(request, book_id, *args, **kwargs):
    data = {
        "id" : book_id
    }
    status = 200
    try:
        obj = Books.objects.get(id=book_id)
        data['name'] = obj.name
        data['author'] = obj.author
        data['description'] = obj.description
    except:
        data['message'] = "Not Found"
        status = 404
    return JsonResponse(data,status=status)


#call via Http response
""" def book_detail_view(request, book_id, *args, **kwargs):
    obj = Books.objects.get(id=book_id)
    return HttpResponse(f"Kitap Adı: {obj.name} Yazarı: {obj.author}")

    try:
        obj = Books.objects.get(id=book_id)
    except:
        raise Http404 """

#======================================
# CREATE BOOKS VIEW
#======================================

def book_create_view(request, *args, **kwargs):
    form = BooksForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = BooksForm()
    return render(request, 'form.html', 
    context={'form':form})
    
    
