from rest_framework import serializers

from course.models import Course, Contact, Branch


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('type',
                  'link')


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('latitude',
                  'longitude',
                  'address')


class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)

    class Meta:
        model = Course
        fields = ('category',
                  'name',
                  'description',
                  'logo',
                  'contacts',
                  'branches')

        # depth = 2

    def create(self, validated_data):
        contacts_list = []
        contacts = validated_data.pop('contacts')
        for i in contacts:
            contacts_list.append(Contact.objects.create(type=i['type'], link=i['link']))

        branches_list = []
        branches = validated_data.pop('branches')
        for i in branches:
            branches_list.append(Branch.objects.create(latitude=i['latitude'],
                                                       longitude=i['longitude'], address=i['address']))

        course = Course.objects.create(**validated_data)
        course.contacts.set(contacts_list)
        course.branches.set(branches_list)
        return course
