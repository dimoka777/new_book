# Generated by Django 2.2.3 on 2019-07-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190722_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Are you driver'),
        ),
    ]
