from rest_framework import serializers
from cycleapp.models import Cycle,Cart,Order_in_Progress,Order_Done
from userapp.serializers import UserSerializer,UserProfileSerializer

#################################################################################

class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cycle
        fields = ('id','sellor','bike_name','brand','category','description','bike_image','stock','price','discount','date_sell','total_sold','delivery_time')

#################################################################################

class CartGetSerailizer(serializers.ModelSerializer):
    cycle = CycleSerializer(read_only=True)
    class Meta:
        model = Cart
        fields = ('id','user','quantity','cycle') 

################################################################################

class CartCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('id','user','quantity','cycle') 


###############################################################################

class Order_In_Progress_Serializer(serializers.ModelSerializer):
    # cycle = CycleSerializer(read_only=True)
    class Meta:
        model = Order_in_Progress
        fields = ('id','user','cycle','quantity','total_payment','user_phone','shipping_address','payment_method','order_date','delivery_date')
    def to_representation(self, instance):
        self.fields['cycle'] = CycleSerializer(read_only=True)
        return super(Order_In_Progress_Serializer, self).to_representation(instance)
################################################################################
class Order_In_Progress_Admin_Serializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    cycle = CycleSerializer(read_only=True)
    class Meta:
        model = Order_in_Progress
        fields = ('id','user','cycle','quantity','total_payment','user_phone','shipping_address','payment_method','order_date','delivery_date')


###############################################################################

class Order_Done_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Done
        fields = ('id','user','cycle','quantity','total_payment','user_phone','shipping_address','payment_method','order_date','delivery_date')

###############################################################################