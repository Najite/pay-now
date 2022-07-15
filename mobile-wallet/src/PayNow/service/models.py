from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=False, unique=True)
    
    class Meta:
        verbose_name_plural ='Service Categories'
    
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse ('service:category', kwargs={'slug':self.slug})



class Service(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/services')
    slug = models.SlugField(null=False, unique=True)
    

    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse("service:service", kwargs={"slug": self.slug})
    