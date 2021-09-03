from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'tags', views.SkillTagsViewSet, basename='tags')
router.register(r'skills', views.SkillViewSet, basename='skills')
router.register(r'projects', views.SkillViewSet, basename='projects')
urlpatterns = router.urls
