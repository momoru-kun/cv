# Generated by Django 3.2.7 on 2021-09-03 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='skilltag',
            name='color',
            field=models.CharField(default=999999, max_length=7, verbose_name='Цвет'),
            preserve_default=False,
        ),
    ]
