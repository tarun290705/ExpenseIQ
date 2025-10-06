from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # Expense CRUD Operation URLs
    path('expenses/add/', views.add_expense, name='add_expense'),
    path('expenses/edit/<int:pk>/', views.edit_expense, name='edit_expense'),
    path('expenses/delete/<int:pk>/', views.delete_expense, name='delete_expense'),
    
    # Income CRUD Operation URLs
    path('income/add/', views.add_income, name='add_income'),
    path('income/edit/<int:pk>/', views.edit_income, name='edit_income'),
    path('income/delete/<int:pk>/', views.delete_income, name='delete_income'),

    # Category CRUD Operation URLs
    path('category/add/', views.add_category, name='add_category'),

    # Budget
    path('budget/', views.manage_budget, name='manage_budget'),

    # Reports
    path('reports/', views.reports, name='reports'),
]