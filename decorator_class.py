from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: str
    gpa: float

def main():
    student_one = Student("James","A70012", 3.78)
    student_two = Student("Allan", "K34008", 1.89)
    student_two.gpa = 2.89

    print(student_one)
    print(student_two)

main()