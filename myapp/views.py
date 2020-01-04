from rest_framework import viewsets
from .models import (
    Company, Job, Worker,
    WorkPlace, WorkTime)
from .serializers import (
    CompaniesListSerializer, CompanyDetailsSerializer, 
    JobCreateSerializer, JobListSerializer,
    WorkerListSerializer, WorkPlaceListSerializer,
    WorkPlaceSerializer, WorkTimeSerializer)
from rest_framework.permissions import IsAuthenticated 


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CompanyDetailsSerializer
        return CompaniesListSerializer


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerListSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return JobCreateSerializer
        return JobListSerializer


class WorkPlaceViewSet(viewsets.ModelViewSet):
    queryset = WorkPlace.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return WorkPlaceListSerializer
        return WorkPlaceSerializer


class WorkTimeViewSet(viewsets.ModelViewSet):
    queryset = WorkTime.objects.all()
    serializer_class = WorkTimeSerializer