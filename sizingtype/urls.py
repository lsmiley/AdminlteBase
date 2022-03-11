from django.urls import path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.SizingtypeListView.as_view(), name='sizingtype'),
    path('new', views.SizingtypeCreateView.as_view(), name='new-sizingtype'),
    path('sizingtype/<pk>/edit', views.SizingtypeUpdateView.as_view(), name='edit-sizingtype'),
    path('sizingtype/<pk>/delete', views.SizingtypeDeleteView.as_view(), name='delete-sizingtype'),
]
