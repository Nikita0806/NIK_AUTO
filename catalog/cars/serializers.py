from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io
from .models import Cars

# class GroupSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Group
#         fields = ('name', 'course', 'enrollment_year')

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cars

        fields = ('marka', 'model', 'cuzov', 'cvet', 'vin', 'data', 'price', 'probeg', 'trans', 'probeg', 'obem', \
                  'top', 'priv', 'sost', 'ls', 'sost', 'pts', 'vlad', 'uchet', 'tel', 'photo1', 'slug', 'opis')

    def get_user_name(self, obj):
        if hasattr(obj, 'user'):
            return f'{obj.user.username}'
        return None

class CarsSerializer(serializers.Serializer):
    marka = serializers.CharField(max_length=50)
    model = serializers.CharField(max_length=50)

def encode():
    model = CarsModel('Elon', 'Musk')
    model_sr = CarsSerializer(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json, type(json), sep='\n')

class CarsModel:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

def decode():
    stream = io.BytesIO(b'{"model":"Elon", "marka":"Musk"}')
    data = JSONParser().parse(stream)
    serializer = StudentSerializer(data=data)
    serializer.is_valid()
    print(serializer.validated_data)

class CarsDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # group_name = serializers.SerializerMethodField()
    # user_name = serializers.SerializerMethodField()

    class Meta:
        model = Cars
        fields = '__all__'

    # def get_group_name(self, obj):
    #     print(obj)
    #     return f'{obj.group.course}{obj.group.name}'
    # def get_group_name(self, obj):
    #     if hasattr(obj, 'group'):
    #         return f'{obj.group.name}'
    #     return None
    #     # return f{obj.group.course}{obj.group.name}''

# class GroupDetailSerializer(serializers.ModelSerializer):
#     # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     group_name = serializers.SerializerMethodField()
#     # user_name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Group
#         fields = '__all__'
#
#     def get_group_name(self, obj):
#         return f'{obj.course}-{obj.name}-{obj.enrollment_year}'