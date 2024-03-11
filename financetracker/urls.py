from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_income/', views.add_income, name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('wallet/', views.wallet, name='wallet'),
    path('delete-income/<int:income_id>/', views.delete_income, name='delete_income'),
    path('delete-expense/<int:expense_id>/', views.delete_expense, name='delete_expense'),
]