from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from course.models import Course, Category, Contact, Branch
from course.serializers import CourseSerializer


class CourseApiTestCase(APITestCase):
    def test_get(self):
        category = Category.objects.create(name='test category', imgpath='img')
        contacts = Contact.objects.create(type=1, link='+996 784 834 374')
        branches_1 = Branch.object.create(latitude='65.879374', longitude='78.7826387', address='branch address')
        branches_2 = Branch.object.create(latitude='63.873567', longitude='78.7836537', address='branch address 2')

        course_1 = Course.objects.create(name='Course_1', description='course description', category=category,
                                         logo='url logo', contacts=[contacts], branches=[branches_1, branches_2])
        course_2 = Course.objects.create(name='Course_2', description='course description', category=category,
                                         logo='url logo', contacts=[contacts], branches=[branches_1, branches_2])

        url = reverse('course-list')
        response = self.client.get(url)
        serializer_data = CourseSerializer([course_1, course_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
