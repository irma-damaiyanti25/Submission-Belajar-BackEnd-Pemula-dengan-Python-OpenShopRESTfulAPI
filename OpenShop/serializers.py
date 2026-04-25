from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    # Tambahan field _links
    _links = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'sku',
            'description',
            'shop',
            'location',
            'price',
            'discount',
            'category',
            'stock',
            'is_available',
            'picture',
            '_links'
        ]

    # Generate _links otomatis
    def get__links(self, obj):
        return [
            {
                "rel": "self",
                "href": "/products/",
                "action": "POST",
                "types": [
                    "application/json"
                ]
            },
            {
                "rel": "self",
                "href": f"/products/{obj.id}/",
                "action": "GET",
                "types": [
                    "application/json"
                ]
            },
            {
                "rel": "self",
                "href": f"/products/{obj.id}/",
                "action": "PUT",
                "types": [
                    "application/json"
                ]
            },
            {
                "rel": "self",
                "href": f"/products/{obj.id}/",
                "action": "DELETE",
                "types": [
                    "application/json"
                ]
            }
        ]