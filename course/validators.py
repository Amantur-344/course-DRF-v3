class CourseValidator:

    @classmethod
    def validator_br_con(cls, contacts, branches):
        try:
            for i in contacts:
                if type(i) != dict: return False
            for i in branches:
                if type(i) != dict: return False
        except TypeError:
            return False
        return True
