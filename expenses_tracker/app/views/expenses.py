from django.shortcuts import render, redirect

from app.common.profile import get_profile
from app.forms.expenses import ExpenseForm, DeleteExpenseForm
from app.models import Expense


def create_expense(request):
    if request.method == 'GET':
        context = {
            'form': ExpenseForm(),
        }

        return render(request, 'expense-create.html', context)
    else:
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.profile = get_profile()
            expense.save()
            return redirect('index')

        context = {
            'form': form,
        }

        return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': ExpenseForm(instance=expense),
        }

        return render(request, 'expense-edit.html', context)
    else:
        form = ExpenseForm(request.POST, instance=expense)

        if form.is_valid():
            form.save()
            return redirect('index')

        context = {
            'expense': expense,
            'form': form,
        }

        return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'expense': expense,
            'form': DeleteExpenseForm(instance=expense),
        }

        return render(request, 'expense-delete.html', context)
    else:
        expense.delete()
        return redirect('index')
