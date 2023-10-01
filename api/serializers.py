from api.models import *
from django.contrib.auth import get_user_model
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer
from django.core.exceptions import ValidationError

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
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['place']
class WorkerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    station = StationSerializer()
    class Meta:
        model = Worker
        fields= ['id','user','address','station','phone','photo', 'company']
        
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
    station = StationSerializer()
    class Meta:
        model = Bus
        fields =['id','license_plate','driver','num_of_seats','level','description','station','is_availaible', 'is_listed','company']

class SimpleBusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'license_plate']
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
        fields =['id','date','source','price','destination','bus']
    

class AddAvailableBusSerializer(serializers.ModelSerializer):
    bus = BusSerializer(read_only=True, many=True)
    class Meta:
        model = AvailableBus
        fields =['id','date','source','price','destination','bus']
    def save(self, **kwargs):
        worker_id = self.context['worker_id']
        added_by = Worker.objects.get(pk= worker_id)
        bus_list = Bus.objects.filter(is_listed=True, company=added_by.company, is_availaible = True)
        if bus_list.count() == 0:
            raise serializers.ValidationError({'message' : 'No bus selected'})
        else:
            selected_bus_list = [
                    AvailableBus(
                        **self.validated_data,
                        bus = bus,
                        added_by = added_by
                    ) for bus in bus_list 
                ]
            for available_bus in selected_bus_list:
                available_bus.save()
            return selected_bus_list

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'phone']
class TicketSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    class Meta:
        model = Ticket
        fields =['id','source','destination','customer','price','seat_num']
class SeatSerializer(serializers.ModelSerializer):
    bus = SimpleBusSerializer()
    customer = CustomerSerializer()
    # maximum_seats = serializers.SerializerMethodField(method_name='max_num_of_seats')
    class Meta:
        model = Seat
        fields = ['id', 'seat_number','is_occupied', 'bus', 'customer']
 