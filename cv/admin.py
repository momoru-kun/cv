from django.contrib import admin
from django.utils.html import format_html

from .models import Project, Skill, SkillTag, Work


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "percentage", "view_color")

    @admin.display(empty_value='-empty-')
    def view_color(self, obj):
        return format_html(
            f'<span style="color: #{obj.color};">{obj.color}</span>'
        )


@admin.register(SkillTag)
class SkillTagAdmin(admin.ModelAdmin):
    list_display = ("name", "view_color")

    @admin.display(empty_value='-empty-')
    def view_color(self, obj):
        return format_html(
            f'<span style="color: #{obj.color};">{obj.color}</span>'
        )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("name",)
