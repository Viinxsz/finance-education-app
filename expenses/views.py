# expenses/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Expense, Budget
from .forms import ExpenseForm, BudgetForm

@login_required
def home(request):
    expenses = Expense.objects.filter(user=request.user)
    budget = Budget.objects.filter(user=request.user).first()
    total_expenses = sum(expense.amount for expense in expenses)
    context = {
        'expenses': expenses,
        'total_expenses': total_expenses,
        'budget': budget
    }
    return render(request, 'expenses/home.html', context)

@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

@login_required
def set_budget(request):
    budget = Budget.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('home')
    else:
        form = BudgetForm(instance=budget)
    return render(request, 'expenses/set_budget.html', {'form': form})
