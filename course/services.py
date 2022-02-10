from course.models import Contact, Branch, Category


class CourseService:

    @classmethod
    def create_con_br(cls, contacts: list, branches: list):
        contacts_list = []
        branches_list = []

        for i in contacts:
            contacts_list.append(Contact.objects.create(type=i['type'], link=i['link']).id)
        for i in branches:
            branches_list.append(
                Branch.objects.create(latitude=i['latitude'],
                                      longitude=i['longitude'], address=i['address']).id
            )
        return {'con': contacts_list, 'br': branches_list}

    @classmethod
    def get_or_create(cls, category: dict):
        category_ob = Category.objects.filter(name=category['name']).first()  # category_object

        if category_ob is not None:
            return category_ob
        return Category.objects.create(name=category['name'], imgpath=category['imgpath'])
