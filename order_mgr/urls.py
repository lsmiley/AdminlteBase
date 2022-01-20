from django.urls import path, include, re_path
# from django.conf.urls import url, include, re_path
from . import views
from order.views import (OrderUpdateView)

from order import apiViews, views

from order.views import (HomepageView, OrderUpdateView, CreateOrderView, GboUpdateView, delete_order,
                         OrderListView, done_order_view, auto_create_order_view, DashboardMainView,
                         ajax_add_product, ajax_modify_order_item, ajax_search_products, ajax_calculate_results_view,
                         order_action_view, ajax_calculate_category_view, OrderItemUpdateView, sizing_ord_view,
                         )

app_name = 'order_mgr_app'


urlpatterns = [
    #  Code to swith beteen and update Orders
    path('order-id-<int:cid>/orderitem/', views.sizing_ord_view, name="view"),

    path('dashboard-main/', DashboardMainView.as_view(), name='dashboard_main'),
    path('order-list/', OrderListView.as_view(), name='order_list'),
    path('create/', CreateOrderView.as_view(), name='create-order'),
    path('create-auto/', auto_create_order_view, name='create_auto'),
    path('update/<int:pk>/', OrderUpdateView.as_view(), name='update_order'),
    path('updategbo/<int:pk>/', GboUpdateView.as_view(), name='update_gbo'),
    path('gbo/<int:pk>/', GboUpdateView.as_view(), name='gbo'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    # path('orderitem/edit', OrderItemUpdateView.as_view(), name='edit-orderitem'),
    # path('orderitem/orderitem/<pk>/edit', OrderItemUpdateView.as_view(), name='edit-orderitem'),
    path('orderitem/<pk>/edit', views.OrderItemUpdateView.as_view(), name='edit-orderitem'),

    path('done/<int:pk>/', done_order_view, name='done_order'),
    path('delete/<int:pk>/', delete_order, name='delete_order'),
    path('action/<int:pk>/<slug:action>/', order_action_view, name='order_action'),

    # path('edit_orderitem/<int:pk>/', OrderItemEditView.as_view(), name='edit_orderitem'),
    #
    # re_path(r'^ordertitem/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.OrderItemEditView.as_view(),
    #         name='orderitem'),

    # path('orderitem_update/<int:pk>/', OrderItemUpdateView.as_view(), name='orderitem_update'),

    #  ajax_calls
    path('ajax/search-products/<int:pk>/', ajax_search_products, name='ajax-search'),
    path('ajax/add-product/<int:pk>/<int:dk>/', ajax_add_product, name='ajax_add'),
    path('ajax/modify-product/<int:pk>/<slug:action>', ajax_modify_order_item, name='ajax_modify'),
    path('ajax/calculate-results/', ajax_calculate_results_view, name='ajax_calculate_result'),
    path('ajax/calculate-category-results/', ajax_calculate_category_view, name='ajax_category_result'),

    #  API_calls
    # path('saveorderitem', saveorderitem, name='saveorderitem'),
    path('saveorderitem', apiViews.saveorderitem, name='saveorderitem'),

    #  Redirect from OrderItem when adding Products
    path('order-id-<int:oid>/orderitem/', views.sizing_ord_view, name="view"),

]
