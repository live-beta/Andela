class Student:
    def __init__(self, first_name, surname, number, student=None, teacher=None):
        self.first_name = first_name
        self.number = number
        self.surname = surname

        self.student = student
        self.teacher = teacher

    def enrol(self, course):
        if not hasattr(self, "student"):
            raise NotImplementedError()

        self.student.enrol(course)

    def assign_teaching(self, course):
        if not hasattr(self, "teacher"):
            raise NotImplementedError()

        self.teacher.assign_teaching(course)
