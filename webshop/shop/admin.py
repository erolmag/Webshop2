from django.contrib import admin

from .models import Product
from .models import DetailedProductImage

admin.site.register(Product)
admin.site.register(DetailedProductImage)
