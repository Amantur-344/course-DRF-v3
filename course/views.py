from django.http import JsonResponse
from rest_framework import generics
from rest_framework.response import Response

from course.models import Course
from course.serializers import CourseSerializer
from course.services import CourseService
from course.validators import CourseValidator


class CourseCreateListAPIView(generics.ListCreateAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # validator_class = CourseValidator
    # service_class = CourseService

    # def create(self, request, *args, **kwargs):
    #     data = request.data
    #
    #     if self.validator_class.validator_br_con(contacts=data['contacts'], branches=data['branches']):
    #         con_br_id = self.service_class.create_con_br(contacts=data['contacts'], branches=data['branches'])
    #
    #         data['contacts'] = con_br_id['con']
    #         data['branches'] = con_br_id['br']
    #
    #         serializer = CourseSerializer(data=data)
    #
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, status=201)
    #         return JsonResponse(serializer.errors, status=400)
    #     return Response('Error: You wrote the data incorrectly or you do not have enough amount')

    # def create(self, request, *args, **kwargs):
    #
    #     data = request.data
    #     data['category'] = self.service_class.get_or_create(data['category'])
    #
    #     serializer = CourseSerializer(data=data)
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)


class CourseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

