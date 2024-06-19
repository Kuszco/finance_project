from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add_expenses/', views.add_expenses, name='add_expenses'),
    path('goals/', views.goals, name='goals'),
    path('add_goal/', views.add_goal, name='add_goal'),
    path('update_goal/<int:goal_id>/', views.update_goal, name='update_goal'),
]
