from datetime import date
from django.db import models
from django.urls import reverse
import random
import string
from django.utils.text import slugify
from randomslugfield import RandomSlugField
from django.db.models import F, Func
from rest_framework.authtoken.admin import User


# from django.db.models.functions import Format

class Cars(models.Model):
    # modeli = models.CharField(verbose_name='Модель', max_length=50)
    marka = models.ForeignKey('Marka', on_delete=models.CASCADE, verbose_name='Марка:')
    model = models.ForeignKey('Model', on_delete=models.CASCADE, verbose_name='Модель:')
    # markis = models.CharField(verbose_name='Марка', max_length=50)
    cuzov = models.ForeignKey('Cuzov', on_delete=models.CASCADE, verbose_name='Тип кузова:')
    cvet = models.CharField(verbose_name='Цвет:', max_length=50)
    vin = models.CharField(verbose_name='VIN:', max_length=50)
    compl = models.CharField(verbose_name='Комплектация:', max_length=50, null=True, blank=True)
    data = models.ForeignKey('Data', on_delete=models.CASCADE, verbose_name='Год выпуска:')
    # date = models.DateField(verbose_name='Год', default=date(2023, 1, 1))       # как выводить формат даты date = models.DateField(verbose_name='Год', default=date(2023, 1, 1))
    nalli = models.BooleanField(verbose_name='В продаже', default=False)
    price = models.IntegerField(verbose_name='Желаемая цена:')
    probeg = models.IntegerField(verbose_name='Пробег:')
    email_mg = models.EmailField(verbose_name='e-mail Менеджера', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True, null=True)
    objects = models.Model
    trans = models.ForeignKey('Trans', on_delete=models.CASCADE, verbose_name='Трансмисия:')
    obem = models.ForeignKey('Obem', on_delete=models.CASCADE, verbose_name='Объём двигателя:')
    top = models.ForeignKey('Top', on_delete=models.CASCADE, verbose_name='Тип двигателя:')
    priv = models.ForeignKey('Priv', on_delete=models.CASCADE, verbose_name='Привод:')
    sost = models.ForeignKey('Sost', on_delete=models.CASCADE, verbose_name='Состояние:')
    ls = models.IntegerField(verbose_name='Л.С')
    pts = models.ForeignKey('Pts', on_delete=models.CASCADE, verbose_name='ПТС:')
    vlad = models.IntegerField(verbose_name='Кол-во владельцев:')
    uchet = models.ForeignKey('Uchet', on_delete=models.CASCADE, verbose_name='Стоит на учёте:')
    tel = models.CharField(verbose_name='Номер телефона для связи:', max_length=12, null=True, blank=True)
    photo1 = models.ImageField(verbose_name='Фото:', upload_to='photos/%Y/%m/%d')
    photo2 = models.ImageField(verbose_name='Фото:', upload_to='photos/%Y/%m/%d', null=True, blank=True)
    photo3 = models.ImageField(verbose_name='Фото:', upload_to='photos/%Y/%m/%d', null=True, blank=True)
    slug = models.SlugField(verbose_name="URL ОБЯЗАТЕЛЬНО! отображение на сайте", max_length=255, unique=True, db_index=True, null=True, blank=True)
    opis = models.CharField(verbose_name='Описание:', max_length=22211)
    # slug = RandomSlugField(length=7)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=True, blank=True)

    @property
    def formatted_number(self):
        return self.price

    class Meta:
        managed = True
        db_table = 'cars'



    def generate_random_slug(self, string_length=8):
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=string_length))
        return random_string

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_random_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.model}'
    # def __str__(self):
    #     formatted_number = '{:,}'.format(self.probeg)
    #     return str(formatted_number)
    #
    # # def get_formatted_probeg(self):
    # #     formatted_probeg = '{:,}'.format(self.probeg)
    # #     return formatted_probeg

    class Meta:
        verbose_name = 'Автомобили'                       # Названия страниц в админке
        verbose_name_plural = 'Автомобили'
        # ordering = ['id']                                   # Для сортировки в таблице админпанели

    # def __str__(self):
    #     return f'{self.probeg}'

    def get_absolute_url(self):
        return reverse('car', kwargs={'car_slug': self.slug})

    # def get_formatted_price(self):
    #     formatted_price = '{:,}'.format(self.price)
    #     return formatted_price

class Marka(models.Model):                                    #Country
    name = models.CharField(verbose_name='Марка:', max_length=40)

    class Meta:
        verbose_name = 'Марки'                       # Названия страниц в админке
        verbose_name_plural = 'Марки'

    def __str__(self):
        return self.name


class Model(models.Model):                                           #City
    marka = models.ForeignKey(Marka, on_delete=models.CASCADE, verbose_name='Марка:')
    name = models.CharField(verbose_name='Модель:', max_length=40)

    class Meta:
        verbose_name = 'Модели'  # Названия страниц в админке
        verbose_name_plural = 'Модели'

    def __str__(self):
        return self.name


class Person(models.Model):
    marka = models.ForeignKey(Marka, on_delete=models.SET_NULL, blank=True, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, blank=True, null=True)

class Cuzov(models.Model):                                           #City
    cuzov = models.CharField(verbose_name='Тип кузова:', max_length=40)

    class Meta:
        verbose_name = 'Тип кузова'  # Названия страниц в админке
        verbose_name_plural = 'Тип кузова'

    def __str__(self):
        return self.cuzov

class Data(models.Model):                                           #City
    data = models.CharField(verbose_name='Год выпуска:', max_length=40)

    class Meta:
        verbose_name = 'Год выпуска'  # Названия страниц в админке
        verbose_name_plural = 'Год выпуска'

    def __str__(self):
        return self.data

class Trans(models.Model):                                           #City
    trans = models.CharField(verbose_name='Трансмисия:', max_length=40)

    class Meta:
        verbose_name = 'Трансмисия'  # Названия страниц в админке
        verbose_name_plural = 'Трансмисия'

    def __str__(self):
        return self.trans

class Obem(models.Model):
    obem = models.CharField(verbose_name='Объём двигателя:', max_length=40)

    class Meta:
        verbose_name = 'Объём двигателя'  # Названия страниц в админке
        verbose_name_plural = 'Объём двигателя'

    def __str__(self):
        return self.obem

class Top(models.Model):
    top = models.CharField(verbose_name='Тип двигателя:', max_length=40)

    class Meta:
        verbose_name = 'Тип двигателя'  # Названия страниц в админке
        verbose_name_plural = 'Тип двигателя'

    def __str__(self):
        return self.top

class Priv(models.Model):
    priv = models.CharField(verbose_name='Привод:', max_length=40)

    class Meta:
        verbose_name = 'Привод'  # Названия страниц в админке
        verbose_name_plural = 'Привод'

    def __str__(self):
        return self.priv

class Sost(models.Model):
    sost = models.CharField(verbose_name='Состояние:', max_length=40)

    class Meta:
        verbose_name = 'Состояние'  # Названия страниц в админке
        verbose_name_plural = 'Состояние'

    def __str__(self):
        return self.sost

class Pts(models.Model):
    pts = models.CharField(verbose_name='ПТС:', max_length=40)

    class Meta:
        verbose_name = 'ПТС'  # Названия страниц в админке
        verbose_name_plural = 'ПТС'

    def __str__(self):
        return self.pts

class Uchet(models.Model):
    uchet = models.CharField(verbose_name='Учёт:', max_length=40)

    class Meta:
        verbose_name = 'Учёт'  # Названия страниц в админке
        verbose_name_plural = 'Учёт'

    def __str__(self):
        return self.uchet

# class Marki(models.Model):                                                              #Group
#     name = models.CharField(verbose_name='Марка', max_length=15, null=True, blank=True)
#     objects = models.Manager()
#
#     class Meta:
#         verbose_name = 'Марка'
#         verbose_name_plural = 'Марка'
#         ordering = ['name']
#
#     def __str__(self):
#         return (f'{self.name}')
#
#
# class Model(models.Model):                                                               #Subject
#     mod = models.CharField(verbose_name='Модель', max_length=20, null=True, blank=True)
#     name = models.ManyToManyField('Marki', verbose_name='Марка')
#     # cars = models.ManyToManyField(Cars, through='Gradebook', verbose_name='Авто')
#     objects = models.Manager()
#
#     class Meta:
#         verbose_name = 'Модель'
#         verbose_name_plural = 'Модель'
#
#     def __str__(self):
#         return self.mod
#
# class Gradebook(models.Model):
#     model = models.ForeignKey(Model, on_delete=models.CASCADE, verbose_name='Модель')
#     objects = models.Manager()
#
#     class Meta:
#         verbose_name = 'Авто'
#         verbose_name_plural = 'Авто'
#
#     def __str__(self):
#         return f'{self.model}'


