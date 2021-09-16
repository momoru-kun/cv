# Generated by Django 3.2.7 on 2021-09-04 01:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_auto_20210904_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='date_end',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата увольнения'),
        ),
        migrations.AlterField(
            model_name='work',
            name='date_start',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата начала работы'),
        ),
    ]