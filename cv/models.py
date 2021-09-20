from django.db import models
from django.utils import timezone


class SkillTag(models.Model):
    name = models.CharField(
        verbose_name="Название тега",
        max_length=60
    )
    color = models.CharField(
        verbose_name="Цвет",
        max_length=7
    )

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(
        verbose_name="Название скила",
        max_length=60
    )

    description = models.TextField(
        verbose_name="Описание",
        null=True,
        blank=True
    )

    percentage = models.DecimalField(
        verbose_name="Процент знания",
        max_digits=3,
        decimal_places=0
    )

    color = models.CharField(
        verbose_name="Цвет",
        max_length=7
    )

    tags = models.ManyToManyField(
        to=SkillTag,
        related_name='skills'
    )

    def __str__(self):
        return f"{self.name}"


class Work(models.Model):
    name = models.CharField(
        verbose_name="Место работы",
        max_length=120
    )

    date_start = models.DateField(
        verbose_name="Дата начала работы",
        default=timezone.now
    )
    date_end = models.DateField(
        verbose_name="Дата увольнения",
        default=timezone.now
    )

    by_today = models.BooleanField(
        verbose_name="По сегодняшний день",
        default=False
    )

    description = models.TextField(
        verbose_name="Чем занимался"
    )


class Project(models.Model):
    name = models.CharField(
        verbose_name="Название проекта",
        max_length=120
    )

    description = models.TextField(
        verbose_name="Описание"
    )

    skills = models.ManyToManyField(
        to=Skill,
        verbose_name="Стэк"
    )

    role = models.CharField(
        verbose_name="Роль",
        max_length=120,
        null=True
    )

    link = models.URLField(
        verbose_name="Ссылка на проект (Если есть)",
        max_length=100,
        null=True,
        blank=True
    )
