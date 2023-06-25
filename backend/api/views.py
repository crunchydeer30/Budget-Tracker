from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.db.models.functions import ExtractWeekDay, ExtractWeek

from .utils import income_amount_year, expense_amount_year, income_amount_month, expense_amount_month, get_increase
from .filters import *
from .models import *
from .serializers import *


@api_view(['GET'])
def paths(request):
    api_urls = {
        '/admin': 'панель администратора',
        '/incomes': {
            'GET': 'список всех доходов',
            'params': {
                'title': 'фильтрация по названию (наличие подстроки)',
                'amount__lt': 'фильтрация по стоимости со значением меньше указанного',
                'amount__lt': 'фильтрация по стоимости со значением больше указанного',
                'date': 'фильтрация по указанной дате',
                'date__lt': 'фильтрация по дате со значением меньше указанного',
                'date__gt': 'фильтрация по стоимости со значением больше указанного',
                'page': 'вывод страницы результатов с указанным номером',
                'category': 'фильтрация по категории',
            },
            'POST': 'добавить доход'
        },
        '/incomes/<id>': {
            'GET': 'информация о доходе с указанным id',
            'DELETE': 'удаление дохода с указанным id;'
        },
        '/expenses': {
            'GET': 'список всех расходов',
            'params': {
                'title': 'фильтрация по названию (наличие подстроки)',
                'amount__lt': 'фильтрация по стоимости со значением меньше указанного',
                'amount__lt': 'фильтрация по стоимости со значением больше указанного',
                'date': 'фильтрация по указанной дате',
                'date__lt': 'фильтрация по дате со значением меньше указанного',
                'date__gt': 'фильтрация по стоимости со значением больше указанного',
                'page': 'вывод страницы результатов с указанным номером',
                'category': 'фильтрация по категории',
            },
            'POST': 'добавить расход',
        },
        '/expenses/id': {
            'GET': 'информация о расходе с указанным id',
            'DELETE': 'удаление расхода с указанным id'
        },
        '/income_categories': {
            'GET': 'список всех категорий доходов',
            'POST': 'добавить категорию доходов'
        },
        '/income_categories/<id>': {
            'GET': 'информация о категории доходов с указанным id',
            'DELETE': 'удаление категории доходов с указанным id'
        },
        '/expense_categories': {
            'GET': 'список всех категорий расходов',
            'POST': 'добавить категорию расходов',
        },
        '/expense_categories/<id>': {
            'GET': 'информация о категории расходов с указанным id',
            'DELETE': 'удаление категории расходов с указанным id'
        },
        '/year_stats': 'статистика о доходах и расходах за текущий год с группировкой по месяцам',
        '/category_stats': 'статистика о расходах с группировкой по наиболее популярным категориям',
        '/week_stats': 'статистика о расходах и доходах за текущую неделю с группировкой по дням недели',
        '/main_stats': 'статистика о расходах и доходах за текущий и прошедший год и месяц с указанием процентного прироста по сравнению с прошлым год и месяцем'
    }
    return Response(api_urls)


@api_view(['GET', 'POST'])
def incomes(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 20

        incomes = Income.objects.order_by('-date')
        filterset = IncomeFilter(request.GET, queryset=incomes)
        incomes = filterset.qs
        incomes = paginator.paginate_queryset(incomes, request)
        serializer = IncomeSerializer(incomes, many=True)

        result = paginator.get_paginated_response(serializer.data)
        return result

    elif request.method == 'POST':
        serializer = PostIncomeSerializer(data=request.data)
        date = None
        try:
            date = request.POST['date']
        except:
            pass
        if date and datetime.strptime(date, '%Y-%m-%d') > datetime.now():
            return Response({'Неверная дата'}, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def income(request, pk):

    income = None
    try:
        income = Income.objects.get(pk=pk)
    except Income.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IncomeSerializer(income, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        income.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def expenses(request):
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 20

        expenses = Expense.objects.order_by('-date')
        filterset = ExpenseFilter(request.GET, queryset=expenses)
        expenses = filterset.qs
        expenses = paginator.paginate_queryset(expenses, request)
        serializer = ExpenseSerializer(expenses, many=True)

        result = paginator.get_paginated_response(serializer.data)
        return result

    elif request.method == 'POST':
        serializer = PostExpenseSerializer(data=request.data)

        date = None
        try:
            date = request.POST['date']
        except:
            pass

        if date and datetime.strptime(date, '%Y-%m-%d') > datetime.now():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def expense(request, pk):

    expense = None

    try:
        expense = Expense.objects.get(pk=pk)
    except:
        return Response({"error_message": "Расхода с таким id не существует"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ExpenseSerializer(expense, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def expense_categories(request):
    if request.method == 'GET':
        categories = ExpenseCategory.objects.order_by('title')
        serializer = ExpenseCategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ExpenseCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def expense_category(request, pk):

    category = None
    try:
        category = ExpenseCategory.objects.get(pk=pk)
    except:
        return Response({"error_message": "Категории с таким id не существует"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ExpenseCategorySerializer(category, many=False)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def income_categories(request):
    if request.method == 'GET':
        categories = IncomeCategory.objects.order_by('title')
        serializer = IncomeCategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = IncomeCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
def income_category(request, pk):

    category = None

    try:
        category = IncomeCategory.objects.get(pk=int(pk))
    except:
        return Response({"error_message": "Категории с таким id не существует"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = IncomeCategorySerializer(category, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def year_stats(request):

    year = datetime.now().isocalendar().year

    incomes = Income.objects.filter(
        date__year=year
    ).values_list(
        'date__month'
    ).annotate(
        Sum('amount')
    ).order_by(
        'date__month'
    )

    expenses = Expense.objects.filter(
        date__year='2023'
    ).values_list(
        'date__month'
    ).annotate(
        Sum('amount')
    ).order_by(
        'date__month'
    )

    year_incomes = [0] * 12
    year_expenses = [0] * 12

    for month in incomes:
        year_incomes[month[0] - 1] = month[1]
    for month in expenses:
        year_expenses[month[0] - 1] = month[1]

    result = {
        'incomes': year_incomes,
        'expenses': year_expenses
    }

    return Response(result)


@api_view(['GET'])
def category_stats(request):

    expenses = Expense.objects.values_list(
        'category__title'
    ).annotate(
        total=Sum('amount')
    ).order_by(
        '-total'
    )

    result = dict()
    other = None

    if len(expenses) > 4:
        expenses = expenses[:4]
        sum_top_categories = Expense.objects.values_list(
            'category__title'
        ).annotate(
            total=Sum('amount')
        ).order_by(
            '-total'
        )[:4].aggregate(Sum('amount'))['amount__sum']

        sum_all_categories = Expense.objects.aggregate(
            Sum('amount')
        )['amount__sum']

        other = sum_all_categories - sum_top_categories

    for expense in expenses:
        result[expense[0]] = expense[1]

    if other:
        result['Остальные категории'] = other

    return Response(result)


@api_view(['GET'])
def last_transactions(request):
    expenses = Expense.objects.order_by('-date')[:5]
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def week_stats(request):

    week = datetime.now().isocalendar().week
    week_incomes = [0] * 7
    week_expenses = [0] * 7

    expenses = Expense.objects.filter(
        date__week=week
    ).annotate(
        weekday=(ExtractWeekDay('date') - 1),
    ).values_list(
        'weekday',
    ).annotate(
        total=Sum('amount')
    ).values_list(
        'weekday',
        'total'
    )

    incomes = Income.objects.filter(
        date__week=week
    ).annotate(
        week=ExtractWeek('date')
    ).annotate(
        weekday=(ExtractWeekDay('date') - 1),
    ).values_list(
        'weekday',
    ).annotate(
        total=Sum('amount')
    ).values_list(
        'weekday',
        'total'
    )

    for day in expenses:
        week_expenses[day[0] - 1] = day[1]

    for day in incomes:
        week_incomes[day[0] - 1] = day[1]

    result = {
        'incomes': week_incomes,
        'expenses': week_expenses
    }

    return Response(result)


@api_view(['GET'])
def main_stats(request):
    year = datetime.now().isocalendar().year
    month = datetime.now().month

    year_incomes = income_amount_year(year)
    last_year_incomes = income_amount_year(year - 1)
    year_incomes_increase = get_increase(year_incomes, last_year_incomes)

    year_expenses = expense_amount_year(year)
    last_year_expenses = expense_amount_year(year - 1)
    year_expenses_increase = get_increase(year_expenses, last_year_expenses)

    month_incomes = income_amount_month(month)
    last_month_incomes = income_amount_month(month - 1)
    month_incomes_increase = get_increase(month_incomes, last_month_incomes)

    month_expenses = expense_amount_month(month)
    last_month_expenses = expense_amount_month(month - 1)
    month_expenses_increase = get_increase(month_expenses, last_month_expenses)

    result = {
        'incomes': {
            'year': {
                'value': year_incomes,
                'increase': year_incomes_increase
            },
            'month': {
                'value': month_incomes,
                'increase': month_incomes_increase
            }
        },
        'expenses': {
            'year': {
                'value': year_expenses,
                'increase': year_expenses_increase
            },
            'month': {
                'value': month_expenses,
                'increase': month_expenses_increase
            }
        }
    }

    return Response(result)
