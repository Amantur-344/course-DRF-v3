from django.urls import path

from course.views import CourseCreateListAPIView, CourseRetrieveUpdateDeleteView

urlpatterns = [
    path('courses/', CourseCreateListAPIView.as_view()),
    path('courses/<int:pk>/', CourseRetrieveUpdateDeleteView.as_view())
]
