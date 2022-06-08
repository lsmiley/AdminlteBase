from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer, OrderItemSerializer, CategorySerializer, ProdvendorSerializer, ProductSerializer, LabordeliverySerializer, LabordeliverytypeSerializer, StatusstateSerializer, SizingtypeSerializer
from order.models import Order, OrderItem
from order.tables import OrderItemTable
from product.models import Category, Prodvendor, Product
from labordelivery.models import Labordelivery
from labordeliverytype.models import Labordeliverytype
from statusstate.models import Statusstate
from sizingtype.models import Sizingtype



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Order-List': '/order-list/',
        'Order-Detail View': '/order-detail/<str:pk>/',
        'Order-Create': '/order-create/',
        'Order-Update': '/order-update/<str:pk>/',
        'Order-Delete': '/order-delete/<str:pk>/',

        'OrderItem-List': '/orderitem-list/',
        'OrderItem-Detail View': '/orderitem-detail/<str:pk>/',
        'OrderItem-Create': '/orderitem-create/',
        'OrderItem-Update': '/orderitem-update/<str:pk>/',
        'OrderItem-Delete': '/orderitem-delete/<str:pk>/',

        'Category-List': '/category-list/',
        'Category-Detail View': '/category-detail/<str:pk>/',
        'Category-Create': '/category-create/',
        'Category-Update': '/category-update/<str:pk>/',
        'Category-Delete': '/category-delete/<str:pk>/',

        'Prodvendor-List': '/prodvendor-list/',
        'Prodvendor-Detail View': '/prodvendor-detail/<str:pk>/',
        'Prodvendor-Create': '/prodvendor-create/',
        'Prodvendor-Update': '/prodvendor-update/<str:pk>/',
        'Prodvendor-Delete': '/prodvendor-delete/<str:pk>/',

        'Product-List': '/product-list/',
        'Product-Detail View': '/product-detail/<str:pk>/',
        'Product-Create': '/product-create/',
        'Product-Update': '/product-update/<str:pk>/',
        'Product-Delete': '/product-delete/<str:pk>/',

        'Labordelivery-List': '/labordelivery-list/',
        'Labordelivery-Detail View': '/labordelivery-detail/<str:pk>/',
        'Labordelivery-Create': '/labordelivery-create/',
        'Labordelivery-Update': '/labordelivery-update/<str:pk>/',
        'Labordelivery-Delete': '/labordelivery-delete/<str:pk>/',

        'Labordeliverytype-List': '/labordeliverytype-list/',
        'Labordeliverytype-Detail View': '/labordeliverytype-detail/<str:pk>/',
        'Labordeliverytype-Create': '/labordeliverytype-create/',
        'Labordeliverytype-Update': '/labordeliverytype-update/<str:pk>/',
        'Labordeliverytype-Delete': '/labordeliverytype-delete/<str:pk>/',

        'Statusstate-List': '/statusstate-list/',
        'Statusstate-Detail View': '/statusstate-detail/<str:pk>/',
        'Statusstate-Create': '/statusstate-create/',
        'Statusstate-Update': '/statusstate-update/<str:pk>/',
        'Statusstate-Delete': '/statusstate-delete/<str:pk>/',

        'Sizingtype-List': '/sizingtype-list/',
        'Sizingtype-Detail View': '/sizingtype-detail/<str:pk>/',
        'Sizingtype-Create': '/sizingtype-create/',
        'Sizingtype-Update': '/sizingtype-update/<str:pk>/',
        'Sizingtype-Delete': '/sizingtype-delete/<str:pk>/'

    }

    return Response(api_urls)

# *******************  Category ******************

@api_view(['GET'])
def categoryList(request):
    categorys = Category.objects.all().order_by('-id')
    serializer = CategorySerializer(categorys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def categoryDetail(request, pk):
    categorys = Category.objects.get(id=pk)
    serializer = CategorySerializer(categorys, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def categoryCreate(request):
    serializer = CategorySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def categoryUpdate(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def categoryDelete(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()

    return Response('Item succsesfully delete!')


# *******************  ProdVendor ******************




@api_view(['GET'])
def prodvendorList(request):
    prodvendors = Prodvendor.objects.all().order_by('-id')
    serializer = ProdvendorSerializer(prodvendors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def prodvendorDetail(request, pk):
    prodvendors = Prodvendor.objects.get(id=pk)
    serializer = ProdvendorSerializer(prodvendors, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def prodvendorCreate(request):
    serializer = ProdvendorSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def prodvendorUpdate(request, pk):
    prodvendor = Prodvendor.objects.get(id=pk)
    serializer = ProdvendorSerializer(instance=prodvendor, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def prodvendorDelete(request, pk):
    prodvendor = Prodvendor.objects.get(id=pk)
    prodvendor.delete()

    return Response('Item succsesfully delete!')


# *******************  Product ******************


@api_view(['GET'])
def productList(request):
    products = Product.objects.all().order_by('-id')
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def productDetail(request, pk):
    products = Product.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def productCreate(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def productUpdate(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def productDelete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()

    return Response('Item succsesfully delete!')


# ************** Labordelivery  *****************

@api_view(['GET'])
def labordeliveryList(request):
    labordeliverys = Labordelivery.objects.all().order_by('-id')
    serializer = LabordeliverySerializer(labordeliverys, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def labordeliveryDetail(request, pk):
    labordeliverys = Labordelivery.objects.get(id=pk)
    serializer = LabordeliverySerializer(labordeliverys, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def labordeliveryCreate(request):
    serializer = LabordeliverySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def labordeliveryUpdate(request, pk):
    labordelivery = Labordelivery.objects.get(id=pk)
    serializer = LabordeliverySerializer(instance=labordelivery, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def labordeliveryDelete(request, pk):
    labordelivery = Labordelivery.objects.get(id=pk)
    labordelivery.delete()

    return Response('Item succsesfully delete!')

# ******************  LaborDeliveryType  *********************


@api_view(['GET'])
def labordeliverytypeList(request):
    labordeliverytypes = Labordeliverytype.objects.all().order_by('-id')
    serializer = LabordeliverytypeSerializer(labordeliverytypes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def labordeliverytypeDetail(request, pk):
    labordeliverytypes = Labordeliverytype.objects.get(id=pk)
    serializer = LabordeliverytypeSerializer(labordeliverytypes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def labordeliverytypeCreate(request):
    serializer = LabordeliverytypeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def labordeliverytypeUpdate(request, pk):
    labordeliverytype = Labordeliverytype.objects.get(id=pk)
    serializer = LabordeliverytypeSerializer(instance=labordeliverytype, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def labordeliverytypeDelete(request, pk):
    labordeliverytype = Labordeliverytype.objects.get(id=pk)
    labordeliverytype.delete()

    return Response('Item succsesfully delete!')


#
# @api_view(['GET'])
# def taskList(request):
#     tasks = Task.objects.all().order_by('-id')
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def taskDetail(request, pk):
#     tasks = Task.objects.get(id=pk)
#     serializer = TaskSerializer(tasks, many=False)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def taskCreate(request):
#     serializer = TaskSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def taskUpdate(request, pk):
#     task = Task.objects.get(id=pk)
#     serializer = TaskSerializer(instance=task, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def taskDelete(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#
#     return Response('Item succsesfully delete!')




# *******************  Order ******************

@api_view(['GET'])
def orderList(request):
    orders = Order.objects.all().order_by('-id')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def orderDetail(request, pk):
    orders = Order.objects.get(id=pk)
    serializer = OrderSerializer(orders, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def orderCreate(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def orderUpdate(request, pk):
    order = Order.objects.get(id=pk)
    serializer = OrderSerializer(instance=order, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def orderDelete(request, pk):
    order = Order.objects.get(id=pk)
    order.delete()

    return Response('Item succsesfully delete!')


# *******************  OrderItem ******************

@api_view(['GET'])
def orderitemList(request):
    orderitems = OrderItem.objects.all().order_by('-id')
    orderitems = OrderItem.objects.all().order_by('-id')
    serializer = OrderItemSerializer(orderitems, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def orderitemDetail(request, pk):
    orderitems = OrderItem.objects.get(id=pk)
    serializer = OrderItemSerializer(orderitems, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def orderitemCreate(request):
    serializer = OrderItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def orderitemUpdate(request, pk):
    orderitem = OrderItem.objects.get(id=pk)
    serializer = OrderItemSerializer(instance=orderitem, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def orderitemDelete(request, pk):
    orderitem = OrderItem.objects.get(id=pk)
    orderitem.delete()

    return Response('Item succsesfully delete!')


# *****************  Statusstate  *****************

@api_view(['GET'])
def statusstateList(request):
    statusstates = Statusstate.objects.all().order_by('-id')
    serializer = StatusstateSerializer(statusstates, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def statusstateDetail(request, pk):
    statusstates = Statusstate.objects.get(id=pk)
    serializer = StatusstateSerializer(statusstates, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def statusstateCreate(request):
    serializer = StatusstateSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def statusstateUpdate(request, pk):
    statusstate = Statusstate.objects.get(id=pk)
    serializer = StatusstateSerializer(instance=statusstate, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def statusstateDelete(request, pk):
    statusstate = Statusstate.objects.get(id=pk)
    statusstate.delete()

    return Response('Item succsesfully delete!')


# *****************  Sizingtype  *****************

@api_view(['GET'])
def sizingtypeList(request):
    sizingtypes = Sizingtype.objects.all().order_by('-id')
    serializer = SizingtypeSerializer(sizingtypes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sizingtypeDetail(request, pk):
    sizingtypes = Sizingtype.objects.get(id=pk)
    serializer = SizingtypeSerializer(sizingtypes, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def sizingtypeCreate(request):
    serializer = SizingtypeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def sizingtypeUpdate(request, pk):
    sizingtype = Sizingtype.objects.get(id=pk)
    serializer = SizingtypeSerializer(instance=sizingtype, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def sizingtypeDelete(request, pk):
    sizingtype = Sizingtype.objects.get(id=pk)
    sizingtype.delete()

    return Response('Item succsesfully delete!')
# *********** Template to build out other API "Get, Post, Update, Etc" ****************
# **************** Just replace "Task" with your Model Name *****************
# ****************** Just Copy and Pate ..., then Un-Comment Section **********
#
# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List': '/task-list/',
#         'Detail View': '/task-detail/<str:pk>/',
#         'Create': '/task-create/',
#         'Update': '/task-update/<str:pk>/',
#         'Delete': '/task-delete/<str:pk>/',
#     }
#
#     return Response(api_urls)
#
#
# @api_view(['GET'])
# def taskList(request):
#     tasks = Task.objects.all().order_by('-id')
#     serializer = TaskSerializer(tasks, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def taskDetail(request, pk):
#     tasks = Task.objects.get(id=pk)
#     serializer = TaskSerializer(tasks, many=False)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def taskCreate(request):
#     serializer = TaskSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def taskUpdate(request, pk):
#     task = Task.objects.get(id=pk)
#     serializer = TaskSerializer(instance=task, data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def taskDelete(request, pk):
#     task = Task.objects.get(id=pk)
#     task.delete()
#
#     return Response('Item succsesfully delete!')

