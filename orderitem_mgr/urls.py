from django.urls import path
# from django.conf.urls import url
from . import views
from order.views import (OrderUpdateView, OrderItemUpdateView, )


app_name = 'orderitem_mgr_app'


urlpatterns = [
    path('create/<int:oid>/', views.create, name="create"),  # I pass oid as for instance to show customer name when i click Add Order
    path('createnew/<int:oid>/', views.create, name="createnew"),  # I pass oid as for instance to show customer name when i click Add Order
    path('edit/order<int:cid>/orderitem-id-<int:oid>/', views.edit, name="edit"),




    # path('orderitem/<pk>/edit', views.OrderItemUpdateView.as_view(), name='edit-orderitem'),
]
