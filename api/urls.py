from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()

router.register('adminstrations', views.AdminstrationViewSet )
router.register('workers',views.WorkerViewSet)
router.register('companies',views.CompanyViewSet)
router.register('tickets',views.TicketViewSet)
router.register('customers', views.CustomerViewSet)
router.register('availables', views.AllAvailableBuses)

bus_router = routers.NestedDefaultRouter(router, 'companies', lookup='company')
bus_router.register('buses', views.BusViewSet, basename="company-bus")

seat_router = routers.NestedDefaultRouter(bus_router, 'buses', lookup = 'bus')
seat_router.register('seats', views.SeatViewSet, basename='bus-seats')

availaible_bus = routers.NestedDefaultRouter(router, 'workers', lookup='worker')
availaible_bus.register('availaibles', views.AvailableBusViewSet, basename="available-bus")

urlpatterns = router.urls + bus_router.urls + availaible_bus.urls + seat_router.urls