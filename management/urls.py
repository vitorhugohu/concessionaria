from django.urls import path
from management.views import RegisterVehicleView, ListAllVehiclesView, ListOneVehicleView, UpdateVehicleView, DeleteVehicleView

urlpatterns = [
    path('resgisterVehicle/', RegisterVehicleView.as_view(), name="registerVehicle"),
    path('listAllVehicles/', ListAllVehiclesView.as_view(), name="listAllVehicles"),
    path('listOneVehicle/<int:pk>/', ListOneVehicleView.as_view(), name="listOneVehicle"),
    path('updateVehicle/<int:pk>/', UpdateVehicleView.as_view(), name="updateVehicle"),
    path('deleteVehicle/<int:pk>/', DeleteVehicleView.as_view(), name="deleteVehicle")
]