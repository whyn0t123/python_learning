class Student:
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_average(self):
        total = 0

        for score in self.scores:
            total += int(score)
            average = total / len(self.scores)

        return average
        
    def describe_student(self):
        contents = f"Name: {self.name.title()}\n"
        contents += f"Age: {self.age}\n"
        contents += f"Average score: {self.get_average():.1f}\n"
        print(contents)
        print()

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_students(self):
        if not self.students:
            print("No students found.")
            return

        for student in self.students:
            student.describe_student()

    def find_best_student(self):
        if not self.students:
                    print("No students found.")
                    return

        best_student = None
        highest_average = 0

        for student in self.students:
           
            average = student.get_average()
        
            if average > highest_average:
                 best_student = student
                 highest_average = average

        print(
            f"The best student is {best_student.name.title()}"
            f"with average score {highest_average:.1f}."
              )

manager = StudentManager()

prompt = "1.Add student\n"
prompt += "2.Show students\n"
prompt += "3.Find best student\n"
prompt += "4.Quit\n"
prompt += "Choose an option(1/2/3/4): "

while True:
    option = input(prompt)

    if option == '1':
        name = input("Enter a student's name: ")
        age = input("Enter the student's age: ")
        score_1 = input("Enter the student's first score: ")
        score_2 = input("Enter the student's second score: ")
        score_3 = input("Enter the student's third score: ")
        scores = [score_1, score_2, score_3]
        student = Student(name, age, scores)

        manager.add_student(student)

        print("Student added successfully.")

    elif option == '2':
        manager.show_students()

    elif option == '3':
        manager.find_best_student()

    elif option == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-4.")