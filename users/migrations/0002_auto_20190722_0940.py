# Generated by Django 2.2.3 on 2019-07-22 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_avatar',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_phone',
            field=models.CharField(default=1, max_length=50, verbose_name='+996 555 55-55-55'),
            preserve_default=False,
        ),
    ]
