from rest_framework import serializers

from .models import Project, Skill, SkillTag, Work


class SkillTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillTag
        fields = ('id', 'name', 'color')
        read_only_fields = fields


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('id', 'name', 'description', 'percentage', 'color')
        read_only_fields = fields


class SkillNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ('name',)
        read_only_fields = fields


class ProjectSerializer(serializers.ModelSerializer):

    skills = SkillNameSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = (
            'id', 'name', 'description',
            'link', 'skills', 'role'
        )
        read_only_fields = fields


class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        fields = (
            'id', 'name', 'date_start',
            'date_end', 'by_today', 'description'
        )
        read_only_fields = fields
