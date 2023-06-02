from django.urls import path
from .views import CatalogListView, CatalogDetailView


urlpatterns = [
    path('', CatalogListView.as_view(), name='catalog_list'),
    path('<pk>', CatalogDetailView.as_view(), name='catalog_detail')
]
