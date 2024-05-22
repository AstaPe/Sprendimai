from scr.classes.students import Student

student = Student('Asta', '10A', 85)

print(student.print_student_info())

print(f'Current Grade: {student.get_grade()}')

student.set_grade(92)
print(f'Updated Grade: {student.get_grade()}')

student.set_grade(105)
