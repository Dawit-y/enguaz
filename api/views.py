from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from .serializers import *
from .models import *

class AdminstrationViewSet(ModelViewSet):
    queryset = Adminstration.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddAdminstrationSerializer
        return AdminstrationSerializer

class WorkerViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddWorkerSerializer
        return WorkerSerializer
class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class BusViewSet(ModelViewSet):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddBusSerializer
        return BusSerializer
    def get_queryset(self, **kwargs):
        return Bus.objects.filter(company__id = self.kwargs['company_pk'])
    def get_serializer_context(self):
        return {'company_id' : self.kwargs['company_pk']}
    
class AvailableBusViewSet(ModelViewSet):
    queryset = AvailableBus.objects.select_related('bus').filter()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddAvailableBusSerializer
        return AvailableBusSerializer
    def get_serializer_context(self):
        return {'worker_id' : self.kwargs['worker_pk']}
    
class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.select_related('customer').all()
    serializer_class = TicketSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class SeatViewSet(ModelViewSet):
    def get_queryset(self, **kwargs):
        bus = Bus.objects.get(id = self.kwargs['bus_pk'])
        return bus.seat_set.all()
    serializer_class = SeatSerializer