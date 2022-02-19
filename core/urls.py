from django.contrib import admin
from django.urls import path, include

from course.views import CourseCreateListAPIView
from .yasg import urlpatterns as doc_urls

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'course', CourseCreateListAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('', include('course.urls'))
    ]))
]

urlpatterns += doc_urls
