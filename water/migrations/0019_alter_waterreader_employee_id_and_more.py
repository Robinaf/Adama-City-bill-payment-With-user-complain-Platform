# Generated by Django 4.0.3 on 2022-05-11 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0018_alter_waterreader_employee_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterreader',
            name='employee_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='watertechnician',
            name='employee_id',
            field=models.IntegerField(),
        ),
    ]
