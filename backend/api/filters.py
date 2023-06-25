import django_filters

from .models import *

class IncomeFilter(django_filters.FilterSet):

    o = django_filters.OrderingFilter(
        fields=(
            ('date', 'date')
        )
    )

    class Meta:
        model = Income
        fields = {
            'title': ['contains'],
            'category': ['exact'],
            'amount': ['lt', 'gt'],
            'date': ['exact', 'lt', 'gt']
        }


class ExpenseFilter(django_filters.FilterSet):

    o = django_filters.OrderingFilter(
        fields=(
            ('amount', 'amount')
        )
    )

    class Meta:
        model = Expense
        fields = {
            'title': ['contains'],
            'category': ['exact'],
            'amount': ['lt', 'gt'],
            'date': ['exact', 'lt', 'gt']
        }