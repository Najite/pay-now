from django.contrib import admin
from.models import Service,Category
# Register your models here.

class TabularInline(admin.TabularInline):
    model = Service
    raw_fields = ['name', 'categories', 'image', 'slug']
    prepopulated_fields = {'slug':('name',)}
    

@admin.register(Category)
class AdminCatgory(admin.ModelAdmin):
    inlines = [TabularInline]
    fields = ['name','slug']
    prepopulated_fields = {'slug':('name',)}