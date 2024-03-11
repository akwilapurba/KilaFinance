from django.shortcuts import render, redirect
from .forms import IncomeForm, ExpenseForm
from .models import Income, Expense
from django.http import JsonResponse

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

def delete_income(request, income_id):
    if request.method == 'DELETE':
        try:
            income = Income.objects.get(pk=income_id)
            income.delete()
            return JsonResponse({'success': True})
        except Income.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Income not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
    
def delete_expense(request, expense_id):
    if request.method == 'DELETE':
        try:
            expense = Expense.objects.get(pk=expense_id)
            expense.delete()
            return JsonResponse({'success': True})
        except Expense.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Expense not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})