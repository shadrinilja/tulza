from .models import Bb
from django.views.generic import ListView, TemplateView
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'home.html'

class SearchResultsView(ListView):
    model = Bb
    template_name = 'search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Bb.objects.filter(
            Q(inn__icontains=query) | Q(name__icontains=query) | Q(url_doc__icontains=query))
        return object_list

