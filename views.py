# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from extend.models import Book,Author
# Create your views here.
def show_homepage(request):
    book_list=Book.objects.all()
    author_list=Author.objects.all()
    return render_to_response('homepage.html',Context({"book_list":book_list,"author_list":author_list,}))
def add_book(request):
    global ids
    if request.POST:
        post = request.POST
        try: 
            Book.objects.get(ISBN = post["ISBN"])
            return HttpResponse("此图书已经存在！")
        except:
            new_book = Book(
            ISBN = post["ISBN"],
            Title = post["Title"],
            AuthorID = Author.objects.get(AuthorID=post["AuthorID"]),
            Publisher = post["Publisher"],
            PublishDate = post["PublishDate"],
            Price = post["Price"],)
            new_book.save()
    book_list=Book.objects.all()
    author_list=Author.objects.all()
    return render_to_response('add.html',Context({"book_list":book_list,"author_list":author_list,}))
def add_author(request):
    if request.POST:
        post = request.POST
        try: 
            Author.objects.get(AuthorID = post["AuthorID"])
            return HttpResponse("此作者已经存在！")
        except:
            new_author = Author(
            AuthorID = post["AuthorID"],
            Name = post["Name"],
            Age = post["Age"],
            Country = post["Country"],)
            new_author.save()
    author_list = Author.objects.all()
    return render_to_response('add_author.html',Context({"author_list":author_list,}))
def search_book(request):
    if request.POST :
        author_list = Author.objects.filter(Name = request.POST['search'])
        for author in author_list:
            book_list = Book.objects.filter(AuthorID = author.AuthorID)
            return render_to_response("search.html",Context({"book_list":book_list,}))
    return render_to_response("search.html")
        
def information(request):
    if request.GET:
        book = Book.objects.get(ISBN = request.GET['ISBN'])
        author = Author.objects.get(AuthorID = book.AuthorID)
        return render_to_response("information.html",Context({"book":book,"author":author,}))
    else:
        book = Book.objects.all()
        return render_to_response("information.html",Context({"book":book,}))
def delete_book(request):
    book = Book.objects.get(ISBN = request.GET['ISBN'])
    book.delete()
    return render_to_response("deletes.html")
def updata_book(request):
    book = Book.objects.get(ISBN = request.GET['ISBN'])
    author_list = Author.objects.all()
    if request.POST:
        book.delete()
        post = request.POST
        new_book = Book(
        ISBN = post["ISBN"],
        Title = post["Title"],
        AuthorID = Author.objects.get(AuthorID=post["AuthorID"]),
        Publisher = post["Publisher"],
        PublishDate = post["PublishDate"],
        Price = post["Price"],)
        new_book.save()
        return render_to_response("updatas.html")
    return render_to_response("updata.html",Context({"Book":book,"author_list":author_list,}))
def delete_author(request):
    author = Author.objects.get(AuthorID = request.GET['AuthorID'])
    author.delete()
    return render_to_response("deletes.html")
