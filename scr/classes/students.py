class Student:
    def __init__(self, name, student_class, grade):
        self.name = name
        self.student_class = student_class
        self.grade = grade

    def get_grade(self):
        return self.grade

    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.grade = new_grade
        else:
            print("Error: Grade must be between 0 and 100.")

    def print_student_info(self):
        return f'Student Name: {self.name}, Class: {self.student_class}, Grade: {self.grade}'
