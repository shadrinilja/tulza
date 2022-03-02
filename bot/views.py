from .models import Bb
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render
import requests
def search_form(request):
    return render('home.html')

# def search(request):
#     if 'q' in request.GET:
#         message = 'You searched for: %r' % request.GET['q']
#     else:
#         message = 'You submitted an empty form.'
#     return HttpResponse(message)

# def search(request):
#     if request.method == 'GET':
#         book_name = request.GET.get('q')
#         try:
#             status = Bb.objects.filter(inn=book_name)
#             return render(request, "search_results.html", {"tro": status})
#         except:
#             return render(request, "search_results.html", {'tro': status})
#     else:
#         return render(request, "search_results.html", {})


class HomePageView(TemplateView):
    template_name = 'home.html'

def get_queryset(request):  # новый
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Bb.objects.filter(inn__icontains=q)
        context = {'books': books, 'query': q}
        return render(request, 'search_results.html', context)
    else:
        return HttpResponse('Пустая форма.')



