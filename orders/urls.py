from django.urls import include, path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'orders',views.ViewOrders)
urlpatterns = [
     path('login',views.loginPage, name='login'),
     path('', include(router.urls)),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
     path('orders/<slug:pk>/', views.OrderDetials, name='order_details')

     # path('customers',views.getCustomers, name='customers')
]