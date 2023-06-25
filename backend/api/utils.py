from django.db.models import Count
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.db.models.functions import ExtractWeekDay, ExtractWeek

from .models import *


def get_increase(current, previous):
    if current == previous:
        return 0
    try:
        return ((current - previous) / previous) * 100
    except ZeroDivisionError:
        return 0
  

def income_amount_year(year):

  result = Income.objects.filter(
        date__year=year
        ).annotate(
            total=Sum('amount')
        ).order_by(
            '-total'
        ).aggregate(Sum('amount'))['amount__sum']

  if not result:
    return 0
  return result


def expense_amount_year(year):

  result = Expense.objects.filter(
        date__year=year
        ).annotate(
            total=Sum('amount')
        ).order_by(
            '-total'
        ).aggregate(Sum('amount'))['amount__sum']

  if not result:
    return 0
  return result


def income_amount_month(month):
  result = Income.objects.filter(
        date__month=month
        ).annotate(
            total=Sum('amount')
        ).order_by(
            '-total'
        ).aggregate(Sum('amount'))['amount__sum']

  if not result:
    return 0
  return result


def expense_amount_month(month):
  result = Expense.objects.filter(
        date__month=month
        ).annotate(
            total=Sum('amount')
        ).order_by(
            '-total'
        ).aggregate(Sum('amount'))['amount__sum']

  if not result:
    return 0
  return result
