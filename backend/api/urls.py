from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.paths, name='api'),
    path('incomes', views.incomes, name='incomes'),
    path('incomes/<int:pk>', views.income, name='income'),
    path('expenses', views.expenses, name='expenses'),
    path('expenses/<int:pk>', views.expense, name='expense'),
    path('expense_categories', views.expense_categories, name='expense_categories'),
    path('expense_categories/<int:pk>', views.expense_category, name='expense_category'),
    path('income_categories', views.income_categories, name='income_categories'),
    path('income_categories/<int:pk>', views.income_category, name='income_category'),
    path('year_stats', views.year_stats, name='year_stats'),
    path('category_stats', views.category_stats, name='category_stats'),
    path('week_stats', views.week_stats, name='week_stats'),
    path('last_transactions', views.last_transactions, name='last_transactions'),
    path('main_stats', views.main_stats, name='main_stats')
]
