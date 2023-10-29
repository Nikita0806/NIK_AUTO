from rest_framework.decorators import action
# from rest_framework.generics import ListAPIView, ListCreateAPIView, \
#     RetrieveUpdateAPIView
from rest_framework.response import Response
# from rest_framework.views import APIView
from .models import Cars
# from django.forms import model_to_dict

# from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .permissions import UserPermission
from .serializers import CarsSerializer, CarsDetailSerializer
from rest_framework import viewsets

from .utils import CarsAPIPagination


class CarsViewSet(viewsets.ModelViewSet):
    pagination_class = CarsAPIPagination
    permission_classes = (UserPermission, )

    def get_queryset(self):
        group = self.request.GET.get('group', '')
        if group:
            return Cars.objects.filter(group_id=group)
        else:
            return Cars.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve' or self.action == 'create':
            return CarsDetailSerializer
        return CarsSerializer

    # @action(methods=['get'], detail=False)
    # def groups(self, request):
    #     groups = Group.objects.all()
    #     return Response({'groups': [f'{gr.course}{gr.name}' for gr in groups]})

    # @action(methods=['get'], detail=True)
    # def group(self, request, pk=None):
    #     group = Group.objects.filter(pk=pk).first()
    #     if group:
    #         return Response({'group': f'{group.course}{group.name}'})
    #     else:
    #         return Response({'group': 'Группа не найдена'})


# class GroupViewSet(viewsets.ModelViewSet):
#     pagination_class = GroupAPIPagination
#     permission_classes = (UserPermission, )
#
#     def get_queryset(self):
#         course = self.request.GET.get('course', '')
#         if course:
#             return Group.objects.filter(course=course)
#         else:
#             return Group.objects.all()
#
#     def get_serializer_class(self):
#         if self.action == 'retrieve' or self.action == 'create':
#             return GroupDetailSerializer
#         return GroupSerializer
#
#     @action(methods=['get'], detail=True)
#     def student(self, request, pk=None):
#         students = Student.objects.filter(grup_id=pk)
#         return Response({'students': [f'{st.first_name}-'
#                                       f'{st.last_name}'for st in students]})
