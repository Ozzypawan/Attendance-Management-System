from django.urls import path
from .views import UserAuthListCreateView, UserAuthDetailView, html_list_view

urlpatterns =[
    path('', html_list_view, name = 'html-list'),
    path('api/list', UserAuthListCreateView.as_view(), name = 'list-create'),
    path('api/list/detail/<int:pk>', UserAuthDetailView.as_view(), name = 'detail')
]