from django.contrib import admin
from .models import Cars, Marka, Model, Person, Cuzov, Data, Trans, Obem, Top, Priv, Sost, Pts, Uchet


class CarsAdmin(admin.ModelAdmin):
    list_display = ('id', 'marka', 'model', 'data', 'probeg', 'nalli', 'cuzov', 'cvet', 'compl', 'price', 'photo1', 'photo2', 'photo3', 'trans','obem','top','priv','ls','pts','vlad','tel')# Что выводиться в админке(фильтр)
    list_display_links = ('id', 'marka', 'model',)         #Те которые будут кликабельны
    search_fields = ('marka', 'model',)                           # Те по которым можно делать поиск (для поиска по названию)
    list_editable = ('nalli',)                               # галочки в админ таблице
    list_filter = ('nalli', 'marka', 'model',)                    # фильтер на странице адмики в правом верхнем углу
    prepopulated_fields = {'slug': ('price',)}

admin.site.register(Cars, CarsAdmin)

# class ModeliAdmin(admin.ModelAdmin):
#     list_display = ('model',)
#     list_display_links = ('model',)
#     search_fields = ('model',)
#
# admin.site.register(Modeli, ModeliAdmin)
#
# @admin.register(Marki)
# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ('id', 'marki', )
#     list_display_links = ('id', 'marki',)
#     search_fields = ('marki',)
#
# @admin.register(Gradebook)
# class GradebookAdmin(admin.ModelAdmin):
#     list_display = ('id', 'marki', 'model',)
#     list_display_links = ('id', 'marki',)
#     search_fields = ('marki', 'model',)
#     list_filter = ('marki', 'model',)
#
#     def get_form(self, request, obj=None, **kwargs):
#         form = super(GradebookAdmin, self).get_form(request, obj, **kwargs)
#         if obj:
#             form.base_fields['model'].queryset = Cars.objects.filter(model_id__in=obj.marki.model.all())
#         return form

class MarkaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')                             # Те которые будут кликабельны
    search_fields = ('name', )                                      # Те по которым можно делать поиск (для поиска по названию)

admin.site.register(Marka, MarkaAdmin)

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'marka',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', )

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'marka',)
    list_display_links = ('id', 'model',)
    search_fields = ('model', )

@admin.register(Cuzov)
class CuzovAdmin(admin.ModelAdmin):
    list_display = ('id', 'cuzov',)
    list_display_links = ('id', 'cuzov',)
    search_fields = ('cuzov', )

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('id', 'data',)
    list_display_links = ('id', 'data',)
    search_fields = ('data', )

@admin.register(Trans)
class TransAdmin(admin.ModelAdmin):
    list_display = ('id', 'trans',)
    list_display_links = ('id', 'trans',)
    search_fields = ('trans', )

@admin.register(Obem)
class ObemAdmin(admin.ModelAdmin):
    list_display = ('id', 'obem',)
    list_display_links = ('id', 'obem',)
    search_fields = ('obem', )

@admin.register(Top)
class TopAdmin(admin.ModelAdmin):
    list_display = ('id', 'top',)
    list_display_links = ('id', 'top',)
    search_fields = ('top', )

@admin.register(Priv)
class PrivAdmin(admin.ModelAdmin):
    list_display = ('id', 'priv',)
    list_display_links = ('id', 'priv',)
    search_fields = ('priv', )

@admin.register(Sost)
class SostAdmin(admin.ModelAdmin):
    list_display = ('id', 'sost',)
    list_display_links = ('id', 'sost',)
    search_fields = ('sost', )

@admin.register(Pts)
class PtsAdmin(admin.ModelAdmin):
    list_display = ('id', 'pts',)
    list_display_links = ('id', 'pts',)
    search_fields = ('pts', )

@admin.register(Uchet)
class UchetAdmin(admin.ModelAdmin):
    list_display = ('id', 'uchet',)
    list_display_links = ('id', 'uchet',)
    search_fields = ('uchet', )

# @admin.register(Gradebook)
# class GradebookAdmin(admin.ModelAdmin):
#     list_display = ('id', 'model')
#     list_display_links = ('id', 'model',)
#     search_fields = ('model',)
#     list_filter = ('model',)

    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(GradebookAdmin, self).get_form(request, obj, **kwargs)
    #     if obj:
    #         form.base_fields['car'].queryset = Cars.objects.filter(group_id__in=obj.subject.groups.all())
    #     return form

