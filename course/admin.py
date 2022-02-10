from django.contrib import admin

from course.models import Course, Category, Branch, Contact

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(Branch)
