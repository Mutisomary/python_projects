class University:
    def __init__(self, uni_name):
        self.uni_name = uni_name

    def showDetails(self):
        print(f"This is {self.uni_name}")


class Course:
    def __init__(self, courses):
        self.courses = courses

    def showDetailsC(self):
        print(f"Courses offered: {self.courses}")


class Branch(University):
    def __init__(self, uni_name, branch_name):
        super().__init__(uni_name)
        self.branch_name = branch_name

    def showDetailsB(self):
        super().showDetails()
        print(f"Branch name: {self.branch_name}")


class Student(Branch, Course):
    def __init__(self, uni_name, branch_name, student_name, courses):
        Branch.__init__(self, uni_name, branch_name)
        Course.__init__(self, courses)
        self.student_name = student_name

    def showDetailsS(self):
        super().showDetails()
        print(f"Student name: {self.student_name}")
        super().showDetailsC()


class Faculty(Branch):
    def __init__(self, uni_name, branch_name, faculty_name):
        super().__init__(uni_name, branch_name)
        self.faculty_name = faculty_name

    def showDetailsF(self):
        super().showDetails()
        print(f"Faculty name: {self.faculty_name}")


student_1 = Student("Chuka", "Main", "MaryM", "Biochemistry")
student_1.showDetailsS()
facultyy = Faculty("Chuka", "Main", "Sciences")
facultyy.showDetailsF()