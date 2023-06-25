from rest_framework import serializers
from .models import *


class IncomeSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = Income
        fields = ('id', 'title', 'amount', 'category', 'date')

class PostIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title', read_only=True)
    class Meta:
        model = Expense
        fields = ('id', 'title', 'amount', 'category', 'date')



class PostExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'





