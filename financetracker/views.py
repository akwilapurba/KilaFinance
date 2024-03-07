from django.shortcuts import render, redirect
from .forms import IncomeForm, ExpenseForm
from .models import Income, Expense

def index(request):
    return render(request, 'index.html')

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_income')
    else:
        form = IncomeForm()
    return render(request, 'add_income.html', {'form': form})


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_expense')
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form})

def wallet(request):
    incomes = Income.objects.all()
    expenses = Expense.objects.all()
    total_income = sum([income.amount for income in incomes])
    total_expense = sum([expense.amount for expense in expenses])
    balance = total_income - total_expense
    return render(request, 'wallet.html', {'incomes': incomes, 'expenses': expenses, 'total_income': total_income, 'total_expense': total_expense, 'balance': balance})

