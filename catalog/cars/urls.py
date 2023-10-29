from rest_framework import routers
from django.urls import path, include
from .views import docs, about, contacts, ShowCar, AddCar, CarsHome, LoginUser, \
    RegisterUser, logout_user, infaclientu
from .viewsets import CarsViewSet

router = routers.DefaultRouter()
router.register(r'cars', CarsViewSet, basename='cars')

urlpatterns = [
    # path('', index, name='home'),
    # path('', AutoHome.as_view(), name='home'),
    # path('glav/', glav, name='glav'),
    path('docs/<slug:doc>/', docs, name='docs'),
    # path('auto/', auto, name='auto'),
    path('', CarsHome.as_view(), name='auto'),
    path('contacts/', contacts, name='contacts'),
    path('about/', about, name='about'),
    path('infa/', infaclientu, name='infa'),
    # path('car/<slug:car_slug>/', show_cars, name='car'),
    path('car/<slug:car_slug>/', ShowCar.as_view(), name='car'),
    # path('addcar/', addcar, name='addcar'),
    path('addcar/', AddCar.as_view(), name='addcar'),
    # path('addcar2/', AddCar2.as_view(), name='addcar2'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    # path('gradebook/', Gradebook.as_view(), name='gradebook'),
    # path('api/v1/students/', StudentAPIView.as_view()),
    # path('api/v1/groups/', GroupAPIView.as_view()),
    # path('api/v1/student/<int:pk>/', StudentAPIDetailView.as_view()),
    # path('api/v1/students/', StudentViewSet.as_view({'get': 'list'})),
    # path('api/v1/student/<int:pk>/', StudentViewSet.as_view({'put': 'update'})),
    path('api/v1/', include(router.urls)),
]