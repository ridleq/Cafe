from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
     path('', views.IndexListView.as_view(), name='index'),
     path('order/add/', views.OrderCreateView.as_view(), name='add_order'),
     path('order/<int:pk>/update/', views.OrderUpdateView.as_view(),
          name='update_order'),
     path('order/<int:pk>/delete/', views.OrderDeleteView.as_view(),
          name='delete_order'),
     path('order/<int:pk>/status/', views.StatusUpdateView.as_view(),
          name='status'),
     path('search/', views.SerachView.as_view(), name='search'),
]
