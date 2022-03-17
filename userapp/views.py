from django.shortcuts import render
from rest_framework import viewsets
from userapp.models import UserProfile
from userapp.serializers import UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins

# Create your views here.

###############################################################################

class UserProfileModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = 'user'
    permission_classes = [IsAuthenticated]
    def get_queryset(self):                                            # added string
        return super().get_queryset().filter(user=self.request.user)   # added st
                  

##############################################################################


