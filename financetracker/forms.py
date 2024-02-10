from django import forms
from .models import Income, Expense


class IncomeAndExpenseForm(forms.ModelForm):
    amount = forms.CharField(widget=forms.TextInput(attrs={
        'id': 'amount',
        'name': 'amount',
        'type': 'number',
        'class': 'block w-full rounded-md border-0 py-1.5 pl-12 pr-12 text-gray-700 ring-1 ring-inset ring-gray-300',
        'placeholder': '0.00',
        'aria-describedby': 'amount-currency',
    }))

    description = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'block w-full rounded-md border-0 py-1.5 pl-7 pr-12 text-gray-700 ring-1 ring-inset ring-gray-300',
        'placeholder': 'Enter the description',
    }))

    class Meta:
        abstract = True


class IncomeForm(IncomeAndExpenseForm):
    class Meta(IncomeAndExpenseForm.Meta):
        model = Income
        fields = ('amount', 'description')


class ExpenseForm(IncomeAndExpenseForm):
    class Meta(IncomeAndExpenseForm.Meta):
        model = Expense
        fields = ('amount', 'description')
