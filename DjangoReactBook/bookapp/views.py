from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.http import is_safe_url
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
#model imports
from bookapp.models import Books
from .serializer import BooksSerializer
#form imports
""" from bookapp import BooksForm"""
from .form import BooksForm

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

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
    books = [x.serialize() for x in blist]
    data = {
        'response' : books
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
#use incoming next value as page to be redirected to


@api_view(['POST'])
def book_create_view(request, *args, **kwargs):
    serializer = BooksSerializer(data=request.POST or None)
    if serializer.is_valid(raise_exception = True):
        serializer.save()
        return Response(serializer.data)
    return Response({}, status=400)

#book_create_view_pure
def book_create_view_serializer(request, *args, **kwargs):
    form = BooksForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)	   
        obj.save()
        if next_url != None and is_safe_url(next_url,ALLOWED_HOSTS):
            return redirect(next_url)
        form = BooksForm()	        
    return render(request, 'components/form.html', context={'form': form}) 	


""" def book_create_view(request, *args, **kwargs):
    form = BooksForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if next_url != None and is_safe_url(next_url):
            return redirect(next_url) 
        form = BooksForm()
    return render(request, 'components/form.html', context={'form': form}) """
#======================================
# DELETE BOOKS VIEW
#======================================

""" def delete_book(request, *args, **kwargs):
    form = BooksForm(request.POST or None)
    next_url = request.POST.get('next') or None
    if form.is_valid():
        Books.objects.filter(id=book_id).delete()
        obj = form.save(commit=False)	   
        obj.save()
        if next_url != None and is_safe_url(next_url,ALLOWED_HOSTS):
            return redirect(next_url)
        form = BooksForm()	        
    return render(request, 'components/form.html', context={'form': form})



Books.objects.filter(id=book_id).delete()"""



#======================================
# UPDATE BOOKS VIEW
#======================================

""" def update_book(request, *args, **kwargs):
    book = Books.objects.get(id=1)
    book.name = "Yeni isim"
    book.save()
    return render(request, 'components/form.html') """