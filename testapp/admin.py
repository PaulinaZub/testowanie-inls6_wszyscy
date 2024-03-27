from django.contrib import admin
from .models import Bus
from .models import ListCars
from .models import Book
# Register your models here.

admin.site.register(Bus)
admin.site.register(ListCars)
admin.site.register(Book)
