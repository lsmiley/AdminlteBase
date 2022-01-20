"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic.base import TemplateView
from order import apiViews, views

from order.views import (HomepageView, OrderUpdateView, CreateOrderView, GboUpdateView, delete_order,
                         OrderListView, done_order_view, auto_create_order_view, DashboardMainView,
                         ajax_add_product, ajax_modify_order_item, ajax_search_products, ajax_calculate_results_view,
                         order_action_view, ajax_calculate_category_view, OrderItemUpdateView, sizing_ord_view,
                         )




urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('category/', include('category.urls')),

    path('acctcust/', include('acctcust.urls')),
    path('labordeliverytype/', include('labordeliverytype.urls')),
    path('labordelivery/', include('labordelivery.urls')),
    path('tntworksheet/', include('tntworksheet.urls')),
    path('statusstate/', include('statusstate.urls')),
    path('prodvendor/', include('prodvendor.urls')),
    path('orderitem/', include('orderitem.urls')),
    path('orderitem_mgr/', include('orderitem_mgr.urls')),
    path('order_mgr/', include('order_mgr.urls')),

    path('product/', include('product.urls')),
    path('category/', include('category.urls')),

    # path('orders/', include('orders.urls', namespace="order_app")),
    path('order/', include('order.urls', namespace="order_app")),


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

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
