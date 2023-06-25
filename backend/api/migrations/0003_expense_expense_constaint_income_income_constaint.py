# Generated by Django 4.1.6 on 2023-06-25 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_income_test_alter_income_date'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='expense',
            constraint=models.CheckConstraint(check=models.Q(('amount__gte', 0.0)), name='expense_constaint'),
        ),
        migrations.AddConstraint(
            model_name='income',
            constraint=models.CheckConstraint(check=models.Q(('amount__gte', 0.0)), name='income_constaint'),
        ),
    ]
