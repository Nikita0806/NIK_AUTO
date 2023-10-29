from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from cars.models import Cars, Marka, Model


class AddCarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['group'].empty_label = 'Не выбрана'

    class Meta:
        model = Cars
        fields = ['marka', 'model', 'cuzov', 'cvet', 'vin', 'compl', 'data', 'price', 'probeg', 'trans',
                  'obem','top','priv','sost','ls','pts','vlad','uchet','tel','photo1','photo2','photo3','opis']

    # def clean_marka(self):
    #     cvet = self.cleaned_data['cvet']
    #     if not cvet.isalpha():
    #         raise ValidationError('Недопустимые символы')
    #     return cvet

# class AddCarForm2(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # self.fields['har'].empty_label = 'Не выбрана'
#
#     class Meta:
#         model = Har
#         fields = ['trans', 'obem', 'top', 'priv', 'ls']
#
#     def clean_trans(self):
#         trans = self.cleaned_data['trans']
#         if not trans.isalpha():
#             raise ValidationError('Недопустимые символы')
#         return trans

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя')
    # email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

# class FilterCarsForm(forms.Form):
#     group = forms.ModelChoiceField(label='Модель', queryset=Marki.objects.all(), empty_label='', required=False)
#     cuzov = forms.CharField(label='Кузов', max_length=50, required=False)
#
# class ChooseMarkiForm(forms.Form):
#     group = forms.ModelChoiceField(label='Марка', queryset=Marki.objects.all(), empty_label='Не выбрана', required=False)
#
# class ChooseModelForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         self.group = kwargs.pop('group', None)
#         super(ChooseModelForm, self).__init__(*args, **kwargs)
#         if self.group:
#             group = Marki.objects.filter(id=self.group)[0]
#             self.fields['model'].queryset = group.model_set.all()
#
#     model = forms.ModelChoiceField(label='Модель', queryset=Model.objects.none(), empty_label='Не выбрана', required=False)
