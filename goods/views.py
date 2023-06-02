from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView

from .models import Good


class CatalogListView(ListView):
    model = Good
    template_name='catalog_list.html'
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        return qs.filter(is_active=True).order_by('-price')


class CatalogDetailView(DetailView):
    model = Good
    template_name='catalog_detail.html'
