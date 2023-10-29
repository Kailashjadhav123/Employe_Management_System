# Generated by Django 4.2.2 on 2023-06-27 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_alter_employee_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.CharField(auto_created=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
