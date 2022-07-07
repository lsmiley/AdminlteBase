from django.urls import path

from . import views

urlpatterns = [
    path('', views.SizerList.as_view(), name='sizer-list'),
    path('sizer/sizer-dashboard/', views.SizerList.as_view(), name='sizer-dashboard'),
    path('sizer/add/', views.SizerSizerItemCreate.as_view(), name='sizer-add'),
    path('sizer/<int:pk>', views.SizerSizerItemUpdate.as_view(), name='sizer-update'),
    path('sizer/<int:pk>', views.SizerDelete.as_view(), name='sizer-delete'),
]
