class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, grade_level, age=0):
        super().__init__(name, age)
        self.grade_level = grade_level

    def study(self):
        print(f"{self.name} is studying for {self.grade_level}.")

class Teacher(Person):
    def __init__(self, name, subject, age=0):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

class Principal(Person):
    def __init__(self, name, age=0, years_of_experience = 0):
        super().__init__(name, age)
        self.years_of_experience = years_of_experience

    def manage(self):
        print(f"{self.name} is managing the school.")


student = Student("Rudy", "Grade 2")
teacher = Teacher("Badabong", "Math")
principal = Principal("Mr. Ben")

student.study()
teacher.teach()
principal.manage()