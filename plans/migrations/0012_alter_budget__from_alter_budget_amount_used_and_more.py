# Generated by Django 4.0.2 on 2022-09-13 20:46

import datetime
from django.db import migrations, models
import expense_tracker.validators


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0011_alter_budget_amount_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='_from',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='from'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='amount_used',
            field=models.FloatField(default=0.0, validators=[expense_tracker.validators.number_lt_zero]),
        ),
        migrations.AlterField(
            model_name='budget',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='has_expired',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='budget',
            name='to',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='budget',
            name='total_amount',
            field=models.FloatField(validators=[expense_tracker.validators.number_lt_zero]),
        ),
        migrations.AlterField(
            model_name='goal',
            name='price',
            field=models.FloatField(validators=[expense_tracker.validators.number_lt_zero]),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('updated', 'Updated'), ('deleted', 'Deleted'), ('blank', 'Blank')], default='blank', max_length=10),
        ),
    ]
