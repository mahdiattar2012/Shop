from django.contrib import admin
from .models import Category, Product, BrandCategory

# admin.site.register(Category)
# admin.site.register(Product)
# admin.site.register(BrandCategory)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ('name',)}

class BrandCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_category', 'slug')
    prepopulated_fields = {"slug": ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand_category', 'slug')
    prepopulated_fields = {"slug": ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(BrandCategory, BrandCategoryAdmin)
admin.site.register(Product, ProductAdmin)
