from django.db import models
from userapp.models import UserAccounts
from django.core.validators import RegexValidator
# Create your models here.

CATEGORY_CHOICES = (
    ('mtb','Mtb'),
    ('road','Road'),
    ('hybrid','Hybrid'),
    ('fatbike','Fatbike'),
    ('electric_bike','Electric'),
    ('other','Other')
)
class Cycle(models.Model):
    sellor = models.ForeignKey(UserAccounts, on_delete=models.CASCADE,limit_choices_to={'is_staff':True})
    bike_name = models.CharField(max_length=100)
    bike_image = models.CharField(max_length=250)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,default='mtb')
    description = models.TextField()
    stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    date_sell = models.DateField(auto_now=True)
    delivery_time = models.PositiveIntegerField()
    total_sold = models.PositiveIntegerField()
    def __str__(self):
        return self.bike_name
    
#################################################################################

class Cart(models.Model):
    user = models.ForeignKey(UserAccounts, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, related_name='cycles', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

###############################################################################
PAYMENT_CHOICES = (
    ('paypal', 'PayPal'),
    ('upipay', 'UpiPay'),
    ('cashpay','CashPay')
)

class Order_in_Progress(models.Model):
    user = models.ForeignKey(UserAccounts, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, related_name='in_progress_cycles', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_payment = models.PositiveIntegerField(blank=True,null=True)
    user_phone =models.CharField(max_length=10,validators=[RegexValidator(r'^\d{0,10}$')],blank=True,null=True)
    shipping_address = models.TextField(blank=True,null=True)
    payment_method = models.CharField(max_length=100,choices=PAYMENT_CHOICES,default='cashpay')
    order_date = models.DateField(auto_now_add=True,blank=True,null=True)   #CharField(max_length=250,blank=True,null=True)
    delivery_date = models.DateField(blank=True,null=True)
    

###############################################################################

class Order_Done(models.Model):
    user = models.ForeignKey(UserAccounts, on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycle, related_name='bought_cycles', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_payment = models.PositiveIntegerField(blank=True,null=True)
    user_phone =models.CharField(max_length=10,validators=[RegexValidator(r'^\d{0,10}$')],blank=True,null=True)
    shipping_address = models.TextField(blank=True,null=True)
    payment_method = models.CharField(max_length=100,choices=PAYMENT_CHOICES,default='cashpay')
    order_date = models.CharField(max_length=250,blank=True,null=True)
    delivery_date = models.CharField(max_length=250,blank=True,null=True)

###############################################################################