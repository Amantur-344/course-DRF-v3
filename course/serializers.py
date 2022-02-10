from rest_framework import serializers

from course.models import Course, Contact, Branch


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('type',
                  'link')


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('latitude',
                  'longitude',
                  'address')


class CourseSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True, read_only=True)
    branches = BranchSerializer(many=True, read_only=True)

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
        contacts = validated_data.get('contacts')
        for i in contacts:
            contacts_list.append(Contact.objects.create(type=i['type'], link=i['link']))

        branches_list = []
        branches = validated_data.get('branches')
        for i in branches:
            branches_list.append(Branch.objectc.create(latitude=i['latitude'],
                                                       longitude=i['longitude'], address=i['address']))

        return Course.objects.create(contacts=contacts_list, branches=branches_list, **validated_data)
