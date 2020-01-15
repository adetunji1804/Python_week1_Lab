class Student:
    def __init__(self, name, college_id, gpa):
        self.name = name
        self.college_id = college_id
        self.gpa = gpa

    def __str__(self):
        return f'Name: {self.name}, id: {self.college_id}, GPA: {self.gpa}'

student_one = Student("Kelly", "A10045", 3.08)
print(student_one)

student_one.gpa = 3.82
print(student_one.gpa)
print(student_one)
