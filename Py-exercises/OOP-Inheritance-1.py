class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying for Grade {self.grade}.")

class Teacher(Person):
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

student = Student("Liam", 16, 10)
student.study()