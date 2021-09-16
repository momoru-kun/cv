from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'tags', views.SkillTagsViewSet, basename='tags')
router.register(r'skills', views.SkillViewSet, basename='skills')
router.register(r'projects', views.ProjectViewSet, basename='projects')
router.register(r'workplaces', views.WorkViewSet, basename='workplaces')
urlpatterns = router.urls
