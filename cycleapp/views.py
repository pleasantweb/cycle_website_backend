from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import BasePermission,IsAuthenticated,IsAdminUser,SAFE_METHODS
from cycleapp.models import Cycle,Cart,Order_in_Progress,Order_Done
from cycleapp.serializers import CycleSerializer,CartGetSerailizer,CartCreateSerializer,Order_Done_Serializer,Order_In_Progress_Serializer, Order_In_Progress_Admin_Serializer
from rest_framework import mixins
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

##############################################################################

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class CycleModelViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer
    permission_classes = [IsAdminUser|ReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']

###############################################################################

class CartGetModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartGetSerailizer
    def get_queryset(self):                                          
        return super().get_queryset().filter(user=self.request.user)
    permission_classes = [IsAuthenticated]

################################################################################

class CartCreateModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartCreateSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):                                          
        return super().get_queryset().filter(user=self.request.user)
    


################################################################################

class Order_In_Progress_ModelViewSet(viewsets.ModelViewSet):
    queryset = Order_in_Progress.objects.all()
    serializer_class = Order_In_Progress_Serializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):                                          
        return super().get_queryset().filter(user=self.request.user)

class Order_In_Progress_Admin_ModelViewSet(viewsets.ModelViewSet):
    queryset = Order_in_Progress.objects.all()
    serializer_class =  Order_In_Progress_Admin_Serializer
    permission_classes = [IsAdminUser]

##############################################################################

class Order_Done_ModelViewSet(viewsets.ModelViewSet):
    queryset = Order_Done.objects.all()
    serializer_class = Order_Done_Serializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):                                          
        return super().get_queryset().filter(user=self.request.user)

###############################################################################