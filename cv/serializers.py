from rest_framework import serializers
from .models import SkillTag, Skill, Project, Work


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


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'description')
        read_only_fields = fields


class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        fields = ('id', 'name', 'description')
        read_only_fields = fields
