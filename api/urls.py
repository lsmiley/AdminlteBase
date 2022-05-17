from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	# path('task-list/', views.taskList, name="task-list"),
	# path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	# path('task-create/', views.taskCreate, name="task-create"),
	# path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	# path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),

	path('order-list/', views.orderList, name="order-list"),
	path('order-detail/<str:pk>/', views.orderDetail, name="order-detail"),
	path('order-create/', views.orderCreate, name="order-create"),
	path('order-update/<str:pk>/', views.orderUpdate, name="order-update"),
	path('order-delete/<str:pk>/', views.orderDelete, name="order-delete"),

	path('orderitem-list/', views.orderitemList, name="orderitem-list"),
	path('orderitem-detail/<str:pk>/', views.orderitemDetail, name="orderitem-detail"),
	path('orderitem-create/', views.orderitemCreate, name="orderitem-create"),
	path('orderitem-update/<str:pk>/', views.orderitemUpdate, name="orderitem-update"),
	path('orderitem-delete/<str:pk>/', views.orderitemDelete, name="orderitem-delete"),

	path('category-list/', views.categoryList, name="category-list"),
	path('category-detail/<str:pk>/', views.categoryDetail, name="category-detail"),
	path('category-create/', views.categoryCreate, name="category-create"),
	path('category-update/<str:pk>/', views.categoryUpdate, name="category-update"),
	path('category-delete/<str:pk>/', views.categoryDelete, name="category-delete"),

	path('prodvendor-list/', views.prodvendorList, name="prodvendor-list"),
	path('prodvendor-detail/<str:pk>/', views.prodvendorDetail, name="prodvendor-detail"),
	path('prodvendor-create/', views.prodvendorCreate, name="prodvendor-create"),
	path('prodvendor-update/<str:pk>/', views.prodvendorUpdate, name="prodvendor-update"),
	path('prodvendor-delete/<str:pk>/', views.prodvendorDelete, name="prodvendor-delete"),

	path('product-list/', views.productList, name="product-list"),
	path('product-detail/<str:pk>/', views.productDetail, name="product-detail"),
	path('product-create/', views.productCreate, name="product-create"),
	path('product-update/<str:pk>/', views.productUpdate, name="product-update"),
	path('product-delete/<str:pk>/', views.productDelete, name="product-delete"),

	path('labordelivery-list/', views.labordeliveryList, name="labordelivery-list"),
	path('labordelivery-detail/<str:pk>/', views.labordeliveryDetail, name="labordelivery-detail"),
	path('labordelivery-create/', views.labordeliveryCreate, name="labordelivery-create"),
	path('labordelivery-update/<str:pk>/', views.labordeliveryUpdate, name="labordelivery-update"),
	path('labordelivery-delete/<str:pk>/', views.labordeliveryDelete, name="labordelivery-delete"),

	path('labordeliverytype-list/', views.labordeliverytypeList, name="labordeliverytype-list"),
	path('labordeliverytype-detail/<str:pk>/', views.labordeliverytypeDetail, name="labordeliverytype-detail"),
	path('labordeliverytype-create/', views.labordeliverytypeCreate, name="labordeliverytype-create"),
	path('labordeliverytype-update/<str:pk>/', views.labordeliverytypeUpdate, name="labordeliverytype-update"),
	path('labordeliverytype-delete/<str:pk>/', views.labordeliverytypeDelete, name="labordeliverytype-delete"),

	path('statusstate-list/', views.statusstateList, name="statusstate-list"),
	path('statusstate-detail/<str:pk>/', views.statusstateDetail, name="statusstate-detail"),
	path('statusstate-create/', views.statusstateCreate, name="statusstate-create"),
	path('statusstate-update/<str:pk>/', views.statusstateUpdate, name="statusstate-update"),
	path('statusstate-delete/<str:pk>/', views.statusstateDelete, name="statusstate-delete"),

	path('sizingtype-list/', views.sizingtypeList, name="sizingtype-list"),
	path('sizingtype-detail/<str:pk>/', views.sizingtypeDetail, name="sizingtype-detail"),
	path('sizingtype-create/', views.sizingtypeCreate, name="sizingtype-create"),
	path('sizingtype-update/<str:pk>/', views.sizingtypeUpdate, name="sizingtype-update"),
	path('sizingtype-delete/<str:pk>/', views.sizingtypeDelete, name="sizingtype-delete"),

]
