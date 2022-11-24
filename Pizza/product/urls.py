from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('new/', views.ProductCreateView.as_view(), name='product_new'),
]
