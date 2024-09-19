from django.db import models # type: ignore

# Create your models here.
class Products(models.Model): 
    name = models.CharField(max_length=30, null=False)
    description = models.TextField(max_length=250, null=True)
    price = models.BigIntegerField()
    slug = models.SlugField(max_length=300)
    img = models.ImageField(upload_to='products/',)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self): 

        return self.name


    class Meta: 
        verbose_name = 'Products'
        verbose_name_plural = 'Products'

class Category(models.Model): 
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta: 
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
