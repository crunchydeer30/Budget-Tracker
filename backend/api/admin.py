from django.contrib import admin
from .models import *

admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
admin.site.register(Income)
admin.site.register(Expense)
