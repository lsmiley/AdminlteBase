from django.urls import path
# from django.conf.urls import url
from . import views
from order.views import (OrderUpdateView, OrderItemUpdateView, )


# app_name = 'orderitem_mgr_app'


urlpatterns = [
    path('', views.OrderItemListView.as_view(), name='orderitem'),
    path('orderitem/new', views.OrderItemCreateView.as_view(), name='new-orderitem'),
    path('orderitem/<pk>/edit', views.OrderItemUpdateView.as_view(), name='edit-orderitem'),
    path('orderitem/<pk>/delete', views.OrderItemDeleteView.as_view(), name='delete-orderitem'),


    # path('updateitem/<int:pk>/', OrderItemUpdateView.as_view(), name='update_orderitem'),

    path('create/<int:oid>/', views.create, name="create"),  # I pass oid as for instance to show customer name when i click Add Order
    path('edit/order<int:cid>/orderitem-id-<int:oid>/', views.edit, name="edit"),
    # path('edit/customer-id-<int:cid>/order-id-<int:oid>/', views.edit, name="edit"),
    path('new', views.OrderItemCreateView.as_view(), name='new-orderitem'),

    # Added to re-route back to Order
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update_order')


    # path('orderitem/<pk>/edit', views.OrderItemUpdateView.as_view(), name='edit-orderitem'),
]
