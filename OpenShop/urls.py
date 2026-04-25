from django.urls import path
from .views import ProductListCreateView, ProductDetailView


urlpatterns = [
    # GET /products
    # POST /products
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),

    # PUT /products/{id}
    # DELETE /products/{id}
    path('products/<uuid:id>/', ProductDetailView.as_view(), name='product-detail'),
]