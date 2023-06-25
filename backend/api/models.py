from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinValueValidator
from django.db.models import CheckConstraint, Q


class ExpenseCategory(models.Model):
    title = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.title

class IncomeCategory(models.Model):
    title = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.title


class Income(models.Model):
    title = models.CharField(max_length=25)
    category = models.ForeignKey(
    IncomeCategory, related_name='incomes', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        constraints = (
            CheckConstraint(
                check=Q(amount__gte=0.0),
                name='income_constaint'),
            )


class Expense(models.Model):
    title = models.CharField(max_length=25)
    category = models.ForeignKey(
        ExpenseCategory, related_name='expenses', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        constraints = (
            CheckConstraint(
                check=Q(amount__gte=0.0),
                name='expense_constaint'),
            )
