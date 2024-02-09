from django.shortcuts import render, redirect
from .forms import IncomeForm, ExpenseForm

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

