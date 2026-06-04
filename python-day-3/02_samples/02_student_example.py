class Student:

    def __init__(self, name, score, group):
        self.name = name
        self.score = score
        self.group = group

    def introduce(self):
        print(f"My name is {self.name} from {self.group} (with score {self.score})")

    def greet(self, other_student):
        print(f"Hello {other_student.name}, I'm {self.name}. Nice to meet you.")

student1 = Student("Juan", 10, 'a')
student2 = Student("Maria", 20, 'b')
student3 = Student("Joseph", 30, 'c')

student1.greet(student2)