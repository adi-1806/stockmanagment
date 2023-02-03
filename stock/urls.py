from . import views
from django.urls import path

urlpatterns=[
    path("",views.login, name="loginpage"),
    path("stock_page/", views.stock_page, name='stockpage'),
    path("motors_entrypage/", views.motors_entrypage, name='motorsentrypage'),
    path("other_entrypage/", views.other_entrypage, name='otherentrypage'),
    path('delete_motor/<str:pk>/',views.delete_motor, name='delete-motor'),
    path('delete_other/<str:pk>/',views.delete_other, name='delete-other'),
    path('edit_motor/<str:pk>/', views.edit_motors, name="editmotor")
]