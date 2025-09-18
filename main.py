class Student():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display_info(self):
        print(f"Hi! I am {self.first_name} {self.last_name}")

class GraduateStudent(Student):
    def __init__(self, first_name, last_name, major):

        super().__init__(first_name, last_name)

        self.major = 'CS'





s = Student("John", "Cena")  # 
s.display_info()

gs = GraduateStudent("Preap", "Sovath", "Music")
gs.display_info()

