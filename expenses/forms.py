# expenses/forms.py
from django import forms
from .models import Expense, Budget

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'date']

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount']
