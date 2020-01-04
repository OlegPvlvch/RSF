from rest_framework import serializers

from .models import (
    Company, Job, Worker, WorkPlace,
    WorkTime, Manager)


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ('id', 'name')


class CompaniesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name')

class CompanyDetailsSerializer(serializers.ModelSerializer):
    managers = ManagerSerializer(many=True)
    jobs = serializers.StringRelatedField(many=True)
    class Meta:
        model = Company
        fields = ('id', 'name', 'managers', 'jobs')


class WorkerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('id', 'name')


class JobListSerializer(serializers.ModelSerializer):
    company = CompaniesListSerializer()
    class Meta:
        model = Job
        fields = ('id', 'name', 'company')

class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id', 'name', 'company')


class WorkPlaceListSerializer(serializers.ModelSerializer):
    job = serializers.StringRelatedField()
    worker = serializers.StringRelatedField()
    company = serializers.ReadOnlyField(source='job.company.name')
    class Meta:
        model = WorkPlace
        fields = ('id', 'company', 'job', 'worker', 'status')

class WorkPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPlace
        fields = ('id', 'job', 'worker', 'status')


class WorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTime
        fields = ('id', 'date_start', 'date_end', 
                'worker', 'workplace', 'status')