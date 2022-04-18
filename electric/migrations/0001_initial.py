# Generated by Django 3.2.9 on 2022-04-18 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_remove_customer_is_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectricCustomer',
            fields=[
                ('meter_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='users.customer')),
            ],
            options={
                'db_table': 'electric_customer',
            },
        ),
    ]
