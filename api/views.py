from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
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
    queryset = AvailableBus.objects.select_related('bus').all()
    serializer_class = AvailableBusSerializer
class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer