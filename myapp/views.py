from rest_framework import viewsets
from .models import (
    Company, Job, Worker,
    WorkPlace, WorkTime)
from .serializers import (
    CompaniesListSerializer,
    CompanyDetailsSerializer, 
    JobCreateSerializer,
    WorkerListSerializer,
    WorkPlaceListSerializer,
    WorkPlaceSerializer,
    WorkTimeSerializer)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CompanyDetailsSerializer
        return CompaniesListSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerListSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobCreateSerializer


class WorkPlaceViewSet(viewsets.ModelViewSet):

    def get_serializer_class(self):
        if self.action == 'list':
            return WorkPlaceListSerializer
        return WorkPlaceSerializer

    queryset = WorkPlace.objects.all()
    serializer_class = WorkPlaceSerializer


class WorkTimeViewSet(viewsets.ModelViewSet):
    queryset = WorkTime.objects.all()
    serializer_class = WorkTimeSerializer