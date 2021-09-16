from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Project, Skill, SkillTag, Work
from .serializers import (ProjectSerializer, SkillSerializer,
                          SkillTagSerializer, WorkSerializer)


class SkillTagsViewSet(ReadOnlyModelViewSet):

    serializer_class = SkillTagSerializer
    queryset = SkillTag.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, 200)

    def retrieve(self, request, pk=None):
        tag = get_object_or_404(self.queryset, pk=pk)

        queryset = tag.skills.all()
        serializer = SkillSerializer(queryset, many=True)
        return Response(serializer.data)


class SkillViewSet(ReadOnlyModelViewSet):

    serializer_class = SkillSerializer
    queryset = Skill.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, 200)


class ProjectViewSet(ReadOnlyModelViewSet):

    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, 200)


class WorkViewSet(ReadOnlyModelViewSet):

    serializer_class = WorkSerializer
    queryset = Work.objects.all().order_by('-date_start')

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, 200)
