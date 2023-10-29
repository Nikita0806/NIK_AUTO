from django.forms import forms
from django_filters import FilterSet, DateFilter, CharFilter


from .models import Cars, Model


class CarsFilter(FilterSet):
    # start_date = CharFilter(field_name='data', lookup_expr='gte', label='Год от:')
    # end_date = CharFilter(field_name='data', lookup_expr='lte', label='Год до:')
    start_price = CharFilter(field_name='price', lookup_expr='gte', label='Цена от:')
    end_price = CharFilter(field_name='price', lookup_expr='lte', label='Цена до:')
    start_probeg = CharFilter(field_name='probeg', lookup_expr='gte', label='Пробег от:')
    end_probeg = CharFilter(field_name='probeg', lookup_expr='lte', label='Пробег до:')
    # marki = CharFilter(field_name='name', lookup_expr='contains', label='Марка')
    # cuzov = CharFilter(field_name='cuzov', lookup_expr='contains', label='Кузов')
    # marki__name = CharFilter(field_name='marki__name', lookup_expr='contains', label='Производитель')


    class Meta:
        model = Cars
        fields = ['marka','model','cuzov','data']