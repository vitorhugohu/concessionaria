from management.serializers import RegisterVehicleSerializer, ListAllVehiclesSerializer, ListOneVehicleSerializer, UpdateVehicleSerializer
from rest_framework.generics import UpdateAPIView
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Vehicle

#, ListOneVehicleSerializer

# Create your views here.
class RegisterVehicleView(generics.GenericAPIView):
    serializer_class = RegisterVehicleSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vehicle = serializer.save()

        return Response(None, status=status.HTTP_201_CREATED)

class ListAllVehiclesView(generics.ListAPIView):
        queryset = Vehicle.objects.all() # Busca todos os itens do banco
        serializer_class = ListAllVehiclesSerializer # Define o serializer usado

class ListOneVehicleView(generics.RetrieveAPIView): # Para retornar apenas um objeto específico pelo ID, você deve usar a classe generics.RetrieveAPIView
    queryset = Vehicle.objects.all()
    serializer_class = ListOneVehicleSerializer

class UpdateVehicleView(UpdateAPIView):
     queryset = Vehicle.objects.all()
     serializer_class = UpdateVehicleSerializer

class DeleteVehicleView(generics.DestroyAPIView):
     queryset = Vehicle.objects.all()
     serializer_class = ListOneVehicleSerializer