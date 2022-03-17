from rest_framework import serializers
from djoser.serializers import UserCreateSerializer,UserSerializer
from django.contrib.auth import get_user_model
from userapp.models import UserProfile

User = get_user_model()

###########################################################################

class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields =('id','email','first_name','last_name','is_staff')
   
#############################################################################

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id','email','first_name','last_name','password')

#############################################################################
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','user','phone','street_address','city','state','country','pin')

############################################################################