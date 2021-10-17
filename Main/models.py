from django.db import models
from django.urls import reverse


# class Category(models.Model):
#     sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory',null=True, blank=True)
#     is_sub = models.BooleanField(default=False)
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(max_length=100, unique=True)

#     class Meta:
#         ordering = ('name',)
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('Main:category_filter', args=[self.slug])

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    # def slug(self):
    #     return f'{self.name.lower()}'

    def get_absolute_url(self):
        return reverse('Main:category_filter', args=[self.slug])

class BrandCategory(models.Model):
    sub_category = models.ForeignKey(Category,related_name='scategory', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Brand Category'
        verbose_name_plural = 'Brand Categories'

    def __str__(self):
        return f'{self.sub_category}/{self.name}'
    
    # def slug(self):
    #     return f'{self.sub_category.name.lower()}-{self.name.lower()}'

    def get_absolute_url(self):
        return reverse('Main:category_filter', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True, blank=True)
    brand_category = models.ForeignKey(BrandCategory, on_delete=models.CASCADE, related_name='products',null=True, blank=True)
    name = models.CharField(max_length=400)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to = 'products/%Y/%m/%d/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.brand_category.name} {self.name}'
    
    
    # def auto_slug(self,category,brand_category,name):
    #     slug_field = f'{self.category.name.lower()}-{self.brand_category.name.lower()}-{self.name.replace(" ","").lower()}'
    #     productt = self.model(slug = slug_field)
    #     productt.save(using=self._db)
    #     return slug_field

    def get_absolute_url(self):
        return self.category