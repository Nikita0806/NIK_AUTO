from rest_framework.pagination import PageNumberPagination

menu = [{'title': "КАТАЛОГ", 'url_name': 'auto'},
        {'title': "КОНТАКТЫ", 'url_name': 'contacts'},
        {'title': "О КОМПАНИИ", 'url_name': 'about'},
        ]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context

class CarsAPIPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5