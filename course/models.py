from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    imgpath = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.address


class Contact(models.Model):
    TYPE_CHOICES = (
        (1, 'PHONE'),
        (2, 'FACEBOOK'),
        (3, 'EMAIL'),
        (4, 'INSTAGRAM'),
        (5, 'WHATSAPP'),
        (6, 'TIKTOK'),
        (7, 'YOUTUBE'),
        (8, 'TELEGRAM')
    )
    type = models.IntegerField(choices=TYPE_CHOICES, blank=True, null=True)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='category_courses', blank=True)
    logo = models.CharField(max_length=255)
    contacts = models.ManyToManyField(Contact, related_name='contacts_courses')
    branches = models.ManyToManyField(Branch, related_name='branches_courses')

    def __str__(self):
        return self.name
