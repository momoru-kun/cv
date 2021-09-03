# Generated by Django 3.2.7 on 2021-09-03 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название скила')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='SkillTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название тега')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название скила')),
                ('description', models.TextField(verbose_name='Описание')),
                ('percentage', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Процент знания')),
                ('color', models.CharField(max_length=7, verbose_name='Цвет')),
                ('tags', models.ManyToManyField(related_name='skills', to='cv.SkillTag')),
            ],
        ),
    ]
