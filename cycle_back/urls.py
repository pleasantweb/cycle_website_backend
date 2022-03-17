from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from userapp import views as userview
from cycleapp import views as cycleview

router = DefaultRouter()

router.register('userprofile', userview.UserProfileModelViewSet,basename='user_prfile')
router.register('cycle', cycleview.CycleModelViewSet,basename='cycle')
router.register('cartget', cycleview.CartGetModelViewSet,basename='cartget')
router.register('cartedit', cycleview.CartCreateModelViewSet,basename='cartedit')
router.register('orderprogress', cycleview.Order_In_Progress_ModelViewSet,basename='progress')
router.register('allorderprogress', cycleview.Order_In_Progress_Admin_ModelViewSet,basename='allprogress')
router.register('orderdone', cycleview.Order_Done_ModelViewSet,basename='order_done')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('auth/',include('djoser.urls')),
    path('auth/',include('djoser.urls.jwt')),
    path('auth/',include('djoser.social.urls')),

    path('shop/',include(router.urls)),
]
