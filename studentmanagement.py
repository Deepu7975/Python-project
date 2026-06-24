class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.marks = {}
        self.attendance = 0

    def add_marks(self, subject, marks):
        self.marks[subject] = marks
        print(f"{subject} marks added.")

    def update_attendance(self, days):
        self.attendance += days
        print("Attendance Updated")

    def calculate_average(self):
        if len(self.marks) == 0:
            return 0
        return sum(self.marks.values()) / len(self.marks)

    def grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        else:
            return "F"

    def result(self):
        return "Pass" if self.calculate_average() >= 40 else "Fail"

    def display(self):
        print("\n----- Student Details -----")
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Attendance:", self.attendance)
        print("Average:", round(self.calculate_average(), 2))
        print("Grade:", self.grade())
        print("Result:", self.result())


class GraduateStudent(Student):
    def __init__(self, student_id, name, course, project):
        super().__init__(student_id, name, course)
        self.project = project

    def display(self):
        super().display()
        print("Project:", self.project)


# Driver Code
s1 = Student(101, "Dhanush", "Computer Science")

s1.add_marks("Python", 85)
s1.add_marks("SQL", 90)
s1.add_marks("Java", 80)
s1.update_attendance(45)

s1.display()

s2 = GraduateStudent(
    102,
    "Rahul",
    "AI & ML",
    "Student Management System"
)

s2.add_marks("Machine Learning", 95)
s2.add_marks("Python", 92)
