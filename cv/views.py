from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Project, SkillTag, Skill
from .serializers import (
    SkillTagSerializer,
    SkillSerializer,
    ProjectSerializer
)


class SkillTagsViewSet(ReadOnlyModelViewSet):

    serializer_class = SkillTagSerializer
    queryset = SkillTag.objects.all()

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data, 200)

    def retrieve(self, request, pk=None):
        tag = get_object_or_404(self.queryset, pk=pk)

        queryset = tag.skills.all()
        print(queryset)
        serializer = SkillSerializer(queryset, many=True)
        print(serializer.data)
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
