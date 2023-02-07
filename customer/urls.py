from . import views
from django.urls import path

urlpatterns=[
    path('stock-list/', views.stock_list, name='stocklist'),
    path('billing-page/<str:pk>/', views.billing, name='billingpage'),
    path('customer-home/', views.customer_home, name='customer_home')
]