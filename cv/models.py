from django.db import models


class SkillTag(models.Model):
    name = models.CharField(
        verbose_name="Название тега",
        max_length=60
    )
    color = models.CharField(
        verbose_name="Цвет",
        max_length=7
    )


class Skill(models.Model):
    name = models.CharField(
        verbose_name="Название скила",
        max_length=60
    )

    description = models.TextField(
        verbose_name="Описание"
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


class Work(models.Model):
    name = models.CharField(
        verbose_name="Место работы",
        max_length=120
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
