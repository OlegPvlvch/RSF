from django.urls import path, include
from myapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'jobs', views.JobViewSet)
router.register(r'workers', views.WorkerViewSet)
router.register(r'workplaces', views.WorkPlaceViewSet)
router.register(r'worktimes', views.WorkTimeViewSet)

urlpatterns = [
    path('', include(router.urls))
]