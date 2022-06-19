from django.contrib import admin
from .models import Product, Company, Supplier, Sales,Contact, Patient, Employee, SupplierInvoice
from django.contrib.admin import register
# Register your models here.

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Company)
admin.site.register(Contact)
# admin.site.register(Stock)
admin.site.register(Sales)
admin.site.register(Employee)
admin.site.register(Patient)
admin.site.register(SupplierInvoice)