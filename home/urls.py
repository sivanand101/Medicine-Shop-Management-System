from django.contrib import admin
from django.urls import path, include
from . import views

from .views import *
app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='homes'),
    path('about/', HomeView.as_view(template_name='home/about_us.html'), name='about'),
    path('logout/', logoutuser, name='logout'),
    path('search/', search, name='search'),
    path('login/', handleLogin, name='login'),
    path('create/', product_create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
    path('add/<int:pk>/', addqty, name='add'),
    path('edit/<int:pk>/',EditProdView.as_view(), name='edit'),
    path('supedit/<int:pk>/',EditSupplierView.as_view(), name='supedit'),
    path('createsupplier/',CreateSupplierView.as_view(), name='create-supplier'),
    path('contact/',CreateContactView.as_view(), name='contact'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('company/', CompanyListView.as_view(), name='company-list'),
    path('suppliers/', SupplierListView.as_view(), name='supplier-list'),
    path('sales/', SalesListView.as_view(), name='sales-list'),
    path('makebill/', views.makebill, name='makebill'),
    # path('create/', ProductCreate.as_view(), name='create'),
    path('createemployee/', views.CreateEmployeeView, name='create-employee'),
    path('createpatient/', views.CreatePatientView, name='create-patient'),
    path('empedit/<int:pk>/',EditEmployeeView.as_view(), name='empedit'),
    path('patedit/<int:pk>/',EditPatientView.as_view(), name='patedit'),
    path('employee/', views.employees, name='employee-list'),
    path('patient/', views.patients, name='patient-list'),
    path('invoice/', views.invoice, name='invoice'),
    path('supplier_invoice/', views.supplier_invoice, name='supplier-invoice'),
    path('add_supplier_invoice/', views.add_supplier_invoice, name='add-supplier-invoice'),

]