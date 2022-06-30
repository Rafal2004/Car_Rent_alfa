from django.contrib import admin
from .models import Car, Car_Brand, Car_Model, Body_Type,Gearbox
# Register your models here.
class Car_Model_Admin(admin.ModelAdmin):
      list_display = ('name', 'brand')
      list_filter = ('brand',)

admin.site.register(Car_Brand)
admin.site.register(Car_Model, Car_Model_Admin)
admin.site.register(Body_Type)
admin.site.register(Gearbox)
admin.site.register(Car)
