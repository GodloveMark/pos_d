# Generated by Django 5.1.3 on 2025-07-16 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posApp', '0010_alter_category_description_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='sales',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posApp.customer'),
        ),
        migrations.AddField(
            model_name='sales',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='sales',
            name='is_credit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='sales',
            name='payment_status',
            field=models.CharField(choices=[('paid', 'Paid'), ('partial', 'Partially Paid'), ('unpaid', 'Unpaid')], default='paid', max_length=20),
        ),
    ]
