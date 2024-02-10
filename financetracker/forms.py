from django import forms
from .models import Income, Expense


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('amount', 'description')

    def __init__(self , *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs['placeholder'] = 'Enter the amount'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter the description'
        self.fields['amount'].widget.attrs['class'] = ('form-control shadow appearance-none border rounded w-full py-2 '
                                                       'px-3 text-gray-700 leading-tight focus:outline-none '
                                                       'focus:shadow-outline')
        self.fields['description'].widget.attrs['class'] = ('form-control shadow appearance-none border rounded w-full '
                                                            'py-2 px-3 text-gray-700 leading-tight focus:outline-none'
                                                            ' focus:shadow-outline')


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('amount', 'description')

    def __init__(self , *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs['placeholder'] = 'Enter the amount'
        self.fields['description'].widget.attrs['placeholder'] = 'Enter the description'
        self.fields['amount'].widget.attrs['class'] = ('form-control shadow appearance-none border rounded w-full py-2 '
                                                       'px-3 text-gray-700 leading-tight focus:outline-none '
                                                       'focus:shadow-outline')
        self.fields['description'].widget.attrs['class'] = ('form-control shadow appearance-none border rounded '
                                                            'w-full py-2 px-3 text-gray-700 leading-tight '
                                                            'focus:outline-none focus:shadow-outline')
