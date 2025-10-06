from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Expense, Income, Budget, Category
from .forms import ExpenseForm, IncomeForm, BudgetForm, CategoryForm
from django.db.models import Sum
from django.contrib import messages
from datetime import date
import json

# Dashboard Views

@login_required
def dashboard(request):
    expenses = Expense.objects.filter(user=request.user)
    income = Income.objects.filter(user=request.user)
    total_expense = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    total_income = income.aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    # Category-wise Expense
    categories = Category.objects.filter(user=request.user)
    labels = []
    values = []
    for cat in categories:
        total = (
            Expense.objects.filter(user=request.user, category=cat)
            .aggregate(total=Sum('amount'))['total'] or 0
        )
        if total > 0:
            labels.append(cat.name)
            values.append(float(total))

    category_data = {
        'labels': labels,
        'values': values,
    }

    expenses = Expense.objects.filter(user=request.user).order_by('-date')[:5]
    
    context = {
        'total_expense': total_expense,
        'total_income': total_income,
        'balance': balance,
        'expenses': expenses,
        'category_data': json.dumps(category_data),
    }

    return render(request, 'expenses/dashboard.html', context)
    
# Expense Views

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expenses:dashboard')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})
    
@login_required
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense Updated!')
            return redirect('expenses:dashboard')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'expenses/edit_expense.html', {'form': form})
    
@login_required
def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk, user=request.user)
    expense.delete()
    messages.success(request, 'Expense Deleted!')
    return redirect('expenses:dashboard')

# Income Views

@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            messages.success(request, 'Income added successfully!')
            return redirect('expenses:dashboard')
    else:
        form = IncomeForm()
    return render(request, 'expenses/add_income.html', {'form': form})
    
@login_required
def edit_income(request, pk):
    income = get_object_or_404(Income, pk=pk, user=request.user)
    if request.method == 'POST':
        form = Income(request.POST, instance=income)
        if form.is_valid():
            form.save()
            messages.success(request, 'Income Updated!')
            return redirect('expenses:dashboard')
    else:
        form = ExpenseForm(instance=income)
    return render(request, 'expenses/edit_income.html', {'form': form})
    
@login_required
def delete_income(request, pk):
    income = get_object_or_404(Income, pk=pk, user=request.user)
    income.delete()
    messages.success(request, 'Income Deleted!')
    return redirect('expenses:dashboard')

# category Views

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'Category added successfully!')
            return redirect('expenses:dashboard')
    else:
        form = CategoryForm()
    return render(request, 'expenses/add_category.html', {'form': form})
    
# Budget Views

@login_required
def manage_budget(request):
    budget, created = Budget.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            messages.success(request, 'Budget Updated!')
            return redirect('expenses:dashboard')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'expenses/manage_budget.html', {'form': form})
    
# Reports Views

@login_required
def reports(request):
    today = date.today()
    monthly_expenses = Expense.objects.filter(user=request.user, date__month=today.month)
    monthly_income = Income.objects.filter(user=request.user, date__month=today.month)
    total_expense = monthly_expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    total_income = monthly_income.aggregate(Sum('amount'))['amount__sum'] or 0
    balance = total_income - total_expense

    context = {
        'monthly_expenses': monthly_expenses,
        'monthly_income': monthly_income,
        'total_expense': total_expense,
        'total_income': total_income,
        'balance': balance,
    }

    return render(request, 'expenses/reports.html', context)