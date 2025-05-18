from django.contrib import admin
from discounts.models import Category, Discount, Partner

# Register your models here.

admin.site.register(Category)
admin.site.register(Discount)
admin.site.register(Partner)