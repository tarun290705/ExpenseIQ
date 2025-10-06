from django.contrib import admin
from .models import Category, Expense, Income, Budget

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name',)
    list_filter = ('user',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'amount', 'date')
    search_fields = ('title', 'category_name')
    list_filter = ('category', 'date')

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('source', 'user', 'amount', 'date')
    search_fields = ('source',)
    list_filter = ('date',)

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'limit')
    list_filter = ('month',)