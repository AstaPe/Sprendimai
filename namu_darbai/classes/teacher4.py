class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class Classroom:
    def __init__(self, teacher):
        self.teacher = teacher
        self.students = []

    def add_student(self, student_name):
        self.students.append(student_name)
        print(f'Studentas {student_name} pridėtas į klasę.')

    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f'Studentas {student_name} pašalintas iš klasės.')
        else:
            print(f'Studentas {student_name} nerastas klasėje.')