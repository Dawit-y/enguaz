from api.models import *
from django.contrib.auth import get_user_model
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username','password', 'email', 'first_name', 'last_name' ]
    
    def create(self, validated_data):
        return super().create(validated_data)

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class AdminstrationSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Adminstration
        fields = ['id', 'user', 'phone', 'photo', 'company_name']

class AddAdminstrationSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    class Meta:
        model = Adminstration
        fields = ['id', 'user', 'phone', 'photo', 'company_name']

    def create(self, validated_data):
        user = dict(validated_data.pop('user'))
        instance = get_user_model().objects.create(**user)      
        return Adminstration.objects.create(user=instance, **validated_data)

class WorkerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Worker
        fields= ['id','user','address','station','phone','photo']
        
class AddWorkerSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    class Meta:
        model = Worker
        fields= ['id','user','address','station','phone','photo']
    def create(self, validated_data):
        user = dict(validated_data.pop('user'))
        instance = get_user_model().objects.create(**user)      
        return Worker.objects.create(user=instance, **validated_data)
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','company_name','web_link','logo','description']
class BusSerializer(serializers.ModelSerializer):
    company  = CompanySerializer()
    class Meta:
        model = Bus
        fields =['id','license_plate','driver','num_of_seats','level','description','company']
class AddBusSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    class Meta:
        model = Bus
        fields =['id','license_plate','driver','num_of_seats','level','description', 'company']
    def create(self, validated_data):
        company_pk = self.context['company_id']
        company = Company.objects.get(pk=company_pk)
        return Bus.objects.create( **validated_data,company=company)

class AvailableBusSerializer(serializers.ModelSerializer):
    bus = BusSerializer()
    class Meta:
        model = AvailableBus
        fields =['id','date','source','destination','bus']

class AddAvailableBusSerializer(serializers.ModelSerializer):
    bus = BusSerializer(many=True)
    class Meta:
        model = AvailableBus
        fields =['id','date','source','destination','bus']
    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields =['id','source','destination','name','phone','price','seat_num']