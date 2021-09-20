# Generated by Django 3.2.7 on 2021-09-20 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0008_work_by_today'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, max_length=100, null=True, verbose_name='Ссылка на проект (Если есть)'),
        ),
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(to='cv.Skill', verbose_name='Стэк'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]