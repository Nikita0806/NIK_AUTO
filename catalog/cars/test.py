from unittest import TestCase

from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase, APISimpleTestCase
# from django.test import TestCase
from cars.models import Cars
from django.contrib.auth.models import User

from cars.serializers import CarsSerializer
from cars.views import CarsHome, ShowCar


# class StudentsApiTestCase(APITestCase):#
#     def setUp(self):
#         # self.client = Client()
#         self.user1 = User.objects.create_superuser(username='admin', password='12345')
#         self.user2 = User.objects.create_user(username='admin2', password='123451')
#         # self.group1 = Group.objects.create(name='43', course='1', enrollment_year='2023')
#         self.student1 = Cars.objects.create(first_name='Иван', last_name='Зернов', middle_name='Иванович',
#                                           email='ivan22@mail.ru', slug='zernov', user=self.user1)
#         self.student2 = Cars.objects.create(first_name='Екатерина', last_name='Белова', middle_name='Николаевна',
#                                           email='ecaterina22@mail.ru', slug='smirnova', user=self.user1)
#         self.students_url = reverse('students-list')
#         self.student_url = reverse('students-detail', kwargs={'pk': self.student1.pk})
#         # self.groups_url = reverse('groups-list')
#         # self.group_url = reverse('groups-detail', kwargs={'pk': self.group1.pk})
#
#
#     def test_get(self):
#         response = self.client.get(self.students_url)
#         serializer_data = StudentSerializer([self.student2, self.student1], many=True).data
#         self.assertEqual(status.HTTP_200_OK, response.status_code)
#         self.assertEqual(serializer_data, response.data['results'])
#         print(f'{response.data=}')
#
#     def test_delete_superuser(self):
#         self.client.force_login(self.user1)
#         response = self.client.delete(self.student_url)
#         self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)      # выводт код ошибки который ожидаешь
#         print(f'{response=}')
#
#     def test_delete_user(self):
#         self.client.force_login(self.user2)
#         response = self.client.delete(self.student_url)
#         self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)      # выводт код ошибки который ожидаешь
#         print(f'{response=}')
#
#     def test_delete_no_auth(self):
#         # self.client.force_login(self.user1)
#         response = self.client.delete(self.student_url)
#         self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)      # выводт код ошибки который ожидаешь
#         print(f'{response=}')
#
#     def test_post_student_superuser(self):
#         self.client.force_login(self.user1)
#         with open("students/Basket.jpg", 'rb') as pict:
#             data = {
#                 'first_name': 'Екатерина',
#                 'last_name': 'Смирнова',
#                 'middle_name': 'Николаевна',
#                 'email': 'smir@mail.ru',
#                 'group': self.group1.id,
#                 'slug': 'smirnova1',
#                 'photo': pict,
#                 'user': self.user1.id
#             }
#             response = self.client.post(self.students_url, data)
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#
#     def test_post_student_user(self):
#         self.client.force_login(self.user2)
#         with open("students/Basket.jpg", 'rb') as pict:
#             data = {
#                 'first_name': 'Екатерина',
#                 'last_name': 'Смирнова',
#                 'middle_name': 'Николаевна',
#                 'email': 'smir@mail.ru',
#                 'group': self.group1.id,
#                 'slug': 'smirnova1',
#                 'photo': pict,
#                 'user': self.user1.id
#             }
#             response = self.client.post(self.students_url, data)
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#
#     def test_post_student_no_auth(self):
#         # self.client.force_login(self.user1)
#         with open("students/Basket.jpg", 'rb') as pict:
#             data = {
#                 'first_name': 'Екатерина',
#                 'last_name': 'Смирнова',
#                 'middle_name': 'Николаевна',
#                 'email': 'smir@mail.ru',
#                 'group': self.group1.id,
#                 'slug': 'smirnova1',
#                 'photo': pict,
#                 'user': self.user1.id
#             }
#             response = self.client.post(self.students_url, data)
#         self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
#
#     def test_post_group_superuser(self):
#         self.client.force_login(self.user1)
#         data = {
#             'name': '43',
#             'course': '1',
#             'enrollment_year': '2023',
#         }
#         response = self.client.post(self.groups_url, data)
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#
#     def test_post_group_user(self):
#         self.client.force_login(self.user2)
#         data = {
#             'name': '43',
#             'course': '1',
#             'enrollment_year': '2023',
#         }
#         response = self.client.post(self.groups_url, data)
#         self.assertEqual(status.HTTP_201_CREATED, response.status_code)
#
#     def test_post_group_ni_auth(self):
#         # self.client.force_login(self.user1)
#         data = {
#             'name': '43',
#             'course': '1',
#             'enrollment_year': '2023',
#         }
#         response = self.client.post(self.groups_url, data)
#         self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)
#
#     def test_updata_student(self):
#
#
# class StudentSerializerTestCase(TestCase):
#     def setUp(self):
#         self.user1 = User.objects.create_superuser(username='admin44', password='1234445')
#         self.user2 = User.objects.create_user(username='admin2', password='123451')
#         self.group1 = Group.objects.create(name='43', course='1', enrollment_year='2023')
#         self.student1 = Student.objects.create(first_name='Никита', last_name='Волков', middle_name='Александрович',
#                                           email='iv@mail.ru', group_id=self.group1.id, slug='nikita11', user=self.user1)
#         self.student2 = Student.objects.create(first_name='Диана', last_name='Курбанова', middle_name='Александровна',
#                                           email='bewww@mail.ru', group_id=self.group1.id, slug='kurb11', user=self.user1)
#         self.students_url = reverse('students-list')
#         self.student_url = reverse('students-detail', kwargs={'pk': self.student1.pk})
#         self.groups_url = reverse('groups-list')
#         self.group_url = reverse('groups-detail', kwargs={'pk': self.group1.pk})
#
#     def test_student_serializer(self):
#         serializer_data = StudentSerializer([self.student1], many=True).data
#         expected_data = [
#             {
#                 'first_name': 'Никита',
#                 'last_name': 'Волков',
#                 'middle_name': 'Александрович',
#                 'email': 'iv@mail.ru',
#                 'group': self.student1.group_id,
#                 'slug': 'nikita11',
#                 'photo': None,
#                 'user': self.user1.id
#             },
#              {
#                  'first_name': 'Диана',
#                  'last_name': 'Курабанова',
#                  'middle_name': 'Александровна',
#                  'email': 'bewww@mail.ru',
#                  'group': self.student2.group_id,
#                  'slug': 'kurb11',
#                  'photo': None,
#                  'user_name': 'admin'
#              },
#              {
#                  "last_name": "ooo1",
#                  "first_name": "o1oo",
#                  "middle_name": "oo1o",
#                  "email": "c1vo@mail.ru",
#                  "group": self.student1.group_id,
#                  "slug": "sdg1fsodg3546",
#                  "photo": None,
#                  "user": self.user1,
#                  "user_name": "di123"
#              }
#          ]
#          self.assertEqual(expected_data, serializer_data)

# class StudentSerializerTestCase(TestCase):
#     def setUp(self):
#         # self.client = Client()
#         self.user1 = User.objects.create_superuser(username='admin', password='12345')
#         # self.group1 = Group.objects.create(name='43', course='1', enrollment_year='2023')
#         self.student1 = Cars.objects.create(first_name='Иван', last_name='Зернов', middle_name='Иванович', email='ivan@mail.ru', slug='zernov', user=self.user1)
#         self.student2 = Cars.objects.create(first_name='Аркадий', last_name='Белов', middle_name='Акакиевич', email='belov@mail.ru',  slug='belov', user=self.user1)
#         self.students_url = reverse('students-list')
#         self.student_url = reverse('students-detail', kwargs={'pk': self.student1.pk})
#
#     def test_student_serializer(self):
#
#         serializer_data = CarsSerializer([self.student1, self.student2], many=True).data
#         expected_data = [
#             {
#                 'last_name': 'Зернов',
#                 'first_name': 'Иван',
#                 'middle_name': 'Иванович',
#                 'email': 'ivan@mail.ru',
#                 'group': self.student1.group_id,
#                 'slug': 'zernov',
#                 'photo': None
#             },
#             {
#                 'last_name': 'Белов',
#                 'first_name': 'Аркадий',
#                 'middle_name': 'Акакиевич',
#                 'email': 'belov@mail.ru',
#                 'group': self.student2.group_id,
#                 'slug': 'belov',
#                 'photo': None
#             },
#         ]
#         self.assertEqual(expected_data, serializer_data)
#
# class TestUrls(SimpleTestCase):
#
#     def test_list_url_home(self):
#         url = reverse('home')
#         self.assertEqual(resolve(url).func.view_class, CarsHome)
#
#     def test_list_url_student(self):
#         url = reverse('student', args=['smirnov'])
#         self.assertEqual(resolve(url).func.view_class, ShowCar)
#
# class BasicTests(TestCase):
#
#     def setUp(self):
#         self.user1 = get_user_model().objects.create_user(
#             username='testuser',
#             email='test@mail.ru',
#             password='secret' )
#
#
#         self.student1 = Cars.objects.create(
#             first_name='Иван',
#             last_name='Зернов',
#             middle_name='Иванович',
#             email='ivan@mail.ru',
#             slug='zernov1',
#             user=self.user1 )
#
#         self.updatestudent_url = reverse('update_student', args=['1'])
#         self.addstudent_url = reverse('addstudent')
#
#     # def test_string_representation(self):
#     #     group = Group(
#     #         name='44',
#     #         course='2',
#     #         enrollment_year='2022'
#     #     )
#     #     self.assertEqual(str(group), f'{group.course}-{group.name}')
#
#     def test_string_representation1(self):
#         student = Cars(
#             first_name='Иван',
#             last_name='Зернов',
#             middle_name='Иванович',
#             email='ivan@mail.ru',
#             group_id=self.group1.id,
#             slug='zernov1',
#             user=self.user1
#         )
#         self.assertEqual(str(student), f'{student.last_name}')
#
#     # def test_group_content(self):
#     #     self.assertEqual(f'{self.group1.name}', '43')
#     #     self.assertEqual(f'{self.group1.course}', '1')
#     #     self.assertEqual(f'{self.group1.enrollment_year}', '2023')
#
#     def test_student_content(self):
#         self.assertEqual(f'{self.student1.first_name}', 'Иван')
#         self.assertEqual(f'{self.student1.last_name}', 'Зернов')
#         self.assertEqual(f'{self.student1.middle_name}', 'Иванович')
#         self.assertEqual(f'{self.student1.email}', 'ivan@mail.ru')
#         self.assertEqual(f'{self.student1.group_id}', '1')
#         self.assertEqual(f'{self.student1.slug}', 'zernov1')
#         self.assertEqual(f'{self.student1.user}', 'testuser')
#
#     def test_students_list_view(self):
#         response = self.client.get(reverse('home'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Иван')
#         self.assertContains(response, 'ЗЕРНОВ')
#         # print(response.rendered_content) # TemplateResponse
#         self.assertTemplateUsed(response, 'students/index.html')











# def calc(a, b, c):
#     if c == '+':
#         return a + b
#     if c == '-':
#         return a - b
#     if c == '*':
#         return a * b
#
# class LogicTestCase(TestCase):
#     def test_plus(self):
#         result = calc(5,7, '+')
#         self.assertEqual(12, result)
#
#     def test_minus(self):
#         result = calc(5,7, '-')
#         self.assertEqual(-2, result)
#
#     def test_umnojenie(self):
#         result = calc(5,7, '*')
#         self.assertEqual(35, result)
