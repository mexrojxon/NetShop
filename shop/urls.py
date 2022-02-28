from django.urls import path
from .views import ShopView, ProductDetailView, ShopCardView

app_name = 'shops'

urlpatterns = [
    path('', ShopView.as_view(), name='shop'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('<int:pk>/shopcard/', ShopCardView.as_view(), name='shopcard'),
]