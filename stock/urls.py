from . import views
from django.urls import path

urlpatterns=[
    path("", views.stock_page, name='stockpage'),
    path("motors_entrypage/", views.motors_entrypage, name='motorsentrypage'),
    path("other_entrypage/", views.other_entrypage, name='otherentrypage')
]