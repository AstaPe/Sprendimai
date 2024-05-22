from namu_darbai.classes.teacher4 import Teacher, Classroom

teacher = Teacher("P. Asta", "Math")


classroom = Classroom(teacher)


classroom.add_student("Rima")
classroom.add_student("Rasa")
classroom.add_student("Sima")


classroom.remove_student("Antanas")
classroom.remove_student("Petras")
