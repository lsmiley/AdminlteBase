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

    #  ajax_calls

    path('ajax/load-products/', views.load_products, name='ajax_load_products'),  # AJAX

    #  API_calls
    # path('saveorderitem', saveorderitem, name='saveorderitem'),
    path('saveorderitem', apiViews.saveorderitem, name='saveorderitem'),

    #  Redirect from OrderItem when adding Products
    path('order-id-<int:oid>/orderitem/', views.sizing_ord_view, name="view"),

]
