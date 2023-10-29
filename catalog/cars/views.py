from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .filters import CarsFilter
from .utils import menu, DataMixin
from  django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .forms import AddCarForm, RegisterUserForm, LoginUserForm
from .models import Cars


# def index(request):
#     cars = Cars.objects.all()
#     context = {
#         'cars': cars,
#         'menu': menu,
#         'title': 'Лайт Авто Главная'
#     }
#     return render(request, 'cars/index.html', context=context)

# class AutoHome(DataMixin, ListView):
#     # model = Student
#     template_name = 'cars/index.html'
#     context_object_name = 'cars'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         auth = self.request.user.is_authenticated
#         c_def = self.get_user_context(title='Главная страница!', auth=auth)
#         return {**context, **c_def}
#
#     def get_queryset(self):
#         return Cars.objects.filter(nall=True)[:1]        # фильтр для вывода на страницу


# def auto(request):
#     cars = Cars.objects.all()
#     context = {
#         'cars': cars,
#         'menu': menu,
#         'title': 'Лайт Авто'
#     }
#     return render(request, 'cars/auto.html', context=context)

class CarsHome(DataMixin, ListView):
    model = Cars
    template_name = 'cars/auto.html'
    context_object_name = 'cars'
    paginate_by = 6

    def get_context_data(self,  *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        auth = self.request.user.is_authenticated
        queryset = self.get_queryset()
        st_filter = CarsFilter(self.request.GET, queryset)
        c_def = self.get_user_context( auth=auth, st_filter=st_filter)
        return {**context, **c_def}

    def get_queryset(self):
        queryset = super().get_queryset()
        st_filter = CarsFilter(self.request.GET, queryset)
        filtered_queryset = st_filter.qs

        # Применить фильтр Cars.objects.filter(nalli=True)
        additional_filter = Cars.objects.filter(nalli=True)
        queryset = filtered_queryset & additional_filter

        return queryset
    # def get_context_data(self,  **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     auth = self.request.user.is_authenticated
    #     c_def = self.get_user_context(title='Каталог автомобилей', auth=auth, form=FilterStudentForm(self.request.GET))
    #     return {**context, **c_def}

    # def get_queryset(self):
    #     filters = {}
    #     first_name = self.request.GET.get('first_name')
    #     last_name = self.request.GET.get('last_name')
    #     group = self.request.GET.get('group')
    #     if first_name:
    #         filters['first_name__contains'] = first_name
    #     if last_name:
    #         filters['last_name__contains'] = last_name
    #     if group:
    #         filters['group'] = group
    #     new_contest = Student.objects.filter(**filters)
    #     return new_contest

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     auth = self.request.user.is_authenticated
    #     c_def = self.get_user_context(title='Каталог автомобилей', auth=auth)
    #     return {**context, **c_def}
    #
    # def get_queryset(self):
    #     return Cars.objects.filter(nalli=True)
    #
         # фильтр для вывода на страницу (количество [:5])

def docs(reqeust, doc):
    if reqeust.GET:
        print(reqeust.GET)
        return HttpResponse(f'<h1>Авто по докам.\<h1><h2>{doc}<h2>')

def about(request):
    context = {
        'menu': menu,
        'title': 'О компании'
    }
    return render(request, 'cars/about.html', context=context)




def contacts(request):
    context = {
        'menu': menu,
        'title': 'Контакты'
    }
    return render(request, 'cars/contacts.html', context=context)

def infaclientu(request):
    context = {
        'menu': menu,
        'title': 'Отлично!'
    }
    return render(request, 'cars/infaclientu.html', context=context)

# def model(request):
#     return HttpResponse("Услуги")

# def marka(request):
#     return HttpResponse("Услуги")


def show_cars(request, car_slug):
    car = get_object_or_404(Cars, slug=car_slug)
    context = {
        'ca': car,
        'menu': menu,
    }
    return render(request, 'cars/car.html', context=context)

class ShowCar(DataMixin, DetailView):
    model = Cars
    template_name = 'cars/car.html'
    slug_url_kwarg = 'car_slug'
    context_object_name = 'ca'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Auto')
        # print(kwargs[object].marka)
        return {**context, **c_def}


class AddCar(LoginRequiredMixin,DataMixin, CreateView):
    form_class = AddCarForm
    template_name = 'cars/addcar.html'
    success_url = reverse_lazy('infa')
    
    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='ПРЕДЛОЖИТЬ АВТО')
        return {**context, **c_def}


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'cars/register.html'
    success_url = reverse_lazy('infa')

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return {**context, **c_def}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('auto')

class LoginUser(DataMixin, LoginView):
    from_class = LoginUserForm
    template_name = 'cars/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return {**context, **c_def}

    def get_success_url(self):
        return reverse_lazy('auto')

def logout_user(request):
    logout(request)
    return redirect('login')

# class Gradebook(DataMixin, ListView):
#     template_name = 'cars/gradebook.html'
#     context_object_name = 'cars'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         auth = self.request.user.is_authenticated
#         group = self.request.GET.get('group')
#         model = self.request.GET.get('model')
#         # dates = set()
#         # studs = []
#         # if group and subject:
#         #     selected_students = Student.objects.filter(group=group)
#         #     for st in selected_students:
#         #         for sub in st.gradebook_set.filter(subject=subject):
#         #             dates.add(sub.date)
#         #     dates = sorted(dates)
#         #     for st in selected_students:
#         #         marks = [''] * len(dates)
#         #         for sub in st.gradebook_set.filter(subject=subject):
#         #             marks[dates.index(sub.date)] = sub.mark
#         #         studs.append((st.pk, f'{st.last_name} {st.first_name[0]}.{st.middle_name[0]}.', marks))
#         c_def = self.get_user_context(title='Журнал успеваемости',
#                                       auth=auth,
#                                       group_form=ChooseMarkiForm(self.request.GET),
#                                       subj_form=ChooseModelForm(self.request.GET, group=group),
#                                       group=group, model=model)
#         return {**context, **c_def}
#
#     def get_queryset(self):
#         group = self.request.GET.get('group')
#         group = 0 if group == '' else group
#         return group