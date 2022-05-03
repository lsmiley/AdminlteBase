from django.urls import path
from . import views


app_name = 'sizing'

urlpatterns = [
        path('', views.HomepageView.as_view(), name='base_sizer'),
        # path('', views.SizingListView.as_view(), name='base_sizer'),
        path('sizing_detail/<int:pk>/', views.SizingDetailView.as_view(), name='sizing_detail'),
        path('create/', views.SizingCreate.as_view(), name='sizing_create'),
        path('update/<int:pk>/', views.SizingUpdate.as_view(), name='sizing_update'),
        path('delete/<int:pk>/', views.SizingDelete.as_view(), name='sizing_delete'),
        ]