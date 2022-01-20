from django.urls import path
# from django.conf.urls import url
from . import views
from order.views import (OrderUpdateView)


app_name = 'order_app'


urlpatterns = [

    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update_order'),

]
