from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense, Goal
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def add_expenses(request):
    if request.method == 'POST':
        category = request.POST['category']
        amount = request.POST['amount']
        date = request.POST['date']
        expense = Expense(user=request.user, category=category, amount=amount, date=date)
        expense.save()
        return JsonResponse({'success': True, 'category': expense.category, 'amount': expense.amount})
    return render(request, 'add_expenses.html')

@login_required
def goals(request):
    user_goals = Goal.objects.filter(user=request.user)
    return render(request, 'goals.html', {'goals': user_goals})

@login_required
def add_goal(request):
    if request.method == 'POST':
        name = request.POST['name']
        target_amount = request.POST['target_amount']
        goal = Goal(user=request.user, name=name, target_amount=target_amount)
        goal.save()
        return redirect('goals')
    return render(request, 'finance_app/add_goal.html')

@login_required
def update_goal(request, goal_id):
    goal = get_object_or_404(Goal, id=goal_id, user=request.user)
    if request.method == 'POST':
        amount = request.POST['amount']
        goal.current_amount += float(amount)
        goal.save()
        return redirect('goals')
    return render(request, 'finance_app/update_goal.html', {'goal': goal})