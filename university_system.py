from abc import ABC, abstractmethod
from typing import List


# 1. PERSON (Abstract Base Class)

class Person(ABC):
    def __init__(self, name: str, id: int):
        self._name = name
        self._id = id

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @abstractmethod
    def displayInfo(self) -> None:
        pass


# 2. EMPLOYEE (Abstract Class inheriting Person)

class Employee(Person, ABC):
    def __init__(self, name: str, id: int, employee_id: int, salary: float):
        super().__init__(name, id)
        self._employee_id = employee_id
        self._salary = salary

    @property
    def employee_id(self):
        return self._employee_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value: float):
        self._salary = value

    @abstractmethod
    def calculateSalary(self) -> float:
        pass


# 3. ADMINISTRATOR (Inherits Employee)

class Administrator(Employee):
    def __init__(self, name: str, id: int, employee_id: int, salary: float, position: str):
        super().__init__(name, id, employee_id, salary)
        self._position = position

    @property
    def position(self):
        return self._position

    def calculateSalary(self) -> float:
        return self._salary

    def displayInfo(self) -> None:
        print(f"[Administrator] Name: {self._name}, ID: {self._id}, "
              f"EmpID: {self._employee_id}, Position: {self._position}, "
              f"Salary: ${self.calculateSalary():,.2f}")


# 4. PROFESSOR (Inherits Employee)

class Professor(Employee):
    def __init__(self, name: str, id: int, employee_id: int, salary: float, specialization: str):
        super().__init__(name, id, employee_id, salary)
        self._specialization = specialization
        self._courses: List['Course'] = []

    @property
    def specialization(self):
        return self._specialization

    @property
    def courses(self):
        return self._courses

    def addCourse(self, course: 'Course'):
        if course not in self._courses:
            self._courses.append(course)

    def calculateSalary(self) -> float:
        bonus_per_course = 1500.0
        return self._salary + (len(self._courses) * bonus_per_course)

    def displayInfo(self) -> None:
        print(f"[Professor] Name: {self._name}, ID: {self._id}, "
              f"EmpID: {self._employee_id}, Specialization: {self._specialization}, "
              f"Courses Taught: {len(self._courses)}, "
              f"Total Salary: ${self.calculateSalary():,.2f}")


# 5. STUDENT (Inherits Person)

class Student(Person):
    def __init__(self, name: str, id: int, student_id: int, program: str):
        super().__init__(name, id)
        self._student_id = student_id
        self._program = program
        self._grades: List[float] = []
        self._courses: List['Course'] = []

    @property
    def student_id(self):
        return self._student_id

    @property
    def program(self):
        return self._program

    @property
    def grades(self):
        return self._grades

    @property
    def courses(self):
        return self._courses

    def addGrade(self, grade: float):
        self._grades.append(grade)

    def enrollInCourse(self, course: 'Course'):
        if course not in self._courses:
            self._courses.append(course)
            course.addStudent(self)

    def calculateAverage(self) -> float:
        if not self._grades:
            return 0.0
        return sum(self._grades) / len(self._grades)

    def getStudentType(self) -> str:
        avg = self.calculateAverage()
        if avg >= 85.0:
            return "Honors"
        else:
            return "Bachelors"

    def displayInfo(self) -> None:
        print(f"[Student] Name: {self._name}, ID: {self._id}, "
              f"StudentID: {self._student_id}, Program: {self._program}, "
              f"Average: {self.calculateAverage():.2f}, "
              f"Type: {self.getStudentType()}")


# 6. ASSIGNMENT

class Assignment:
    def __init__(self, title: str, due_date: str, marks: float = 0.0):
        self._title = title
        self._due_date = due_date
        self._marks = marks

    @property
    def title(self):
        return self._title

    @property
    def marks(self):
        return self._marks

    @marks.setter
    def marks(self, value: float):
        self._marks = value

    def displayAssignment(self) -> None:
        print(f"    [Assignment] {self._title} (Due: {self._due_date}) - Marks: {self._marks}")


# 7. COURSE

class Course:
    def __init__(self, course_code: str, course_name: str):
        self._course_code = course_code
        self._course_name = course_name
        self._students: List[Student] = []
        self._assignments: List[Assignment] = []
        self._professor: Professor = None

    @property
    def course_code(self):
        return self._course_code

    @property
    def course_name(self):
        return self._course_name

    @property
    def students(self):
        return self._students

    @property
    def assignments(self):
        return self._assignments

    @property
    def professor(self):
        return self._professor

    def setProfessor(self, professor: Professor):
        self._professor = professor
        professor.addCourse(self)

    def addStudent(self, student: Student):
        if student not in self._students:
            self._students.append(student)
            if self not in student.courses:
                student.enrollInCourse(self)

    def addAssignment(self, assignment: Assignment):
        self._assignments.append(assignment)

    def deleteCourse(self):
        print(f"  >> Deleting Course '{self._course_name}'. All assignments removed.")
        self._assignments.clear()
        self._students.clear()

    def calculateAverage(self) -> float:
        if not self._students:
            return 0.0
        total = sum(s.calculateAverage() for s in self._students)
        return total / len(self._students)

    def displayInfo(self) -> None:
        prof_name = self._professor.name if self._professor else "Not Assigned"
        print(f"\n[Course] {self._course_code}: {self._course_name} | Professor: {prof_name}")
        print(f"  Enrolled Students: {len(self._students)}")
        print(f"  Assignments ({len(self._assignments)}):")
        for a in self._assignments:
            a.displayAssignment()


# 8. DEPARTMENT

class Department:
    def __init__(self, name: str):
        self._name = name
        self._professors: List[Professor] = []
        self._courses: List[Course] = []

    @property
    def name(self):
        return self._name

    @property
    def professors(self):
        return self._professors

    @property
    def courses(self):
        return self._courses

    def addProfessor(self, professor: Professor):
        if professor not in self._professors:
            self._professors.append(professor)

    def addCourse(self, course: Course):
        if course not in self._courses:
            self._courses.append(course)

    def calculateAverage(self) -> float:
        all_students = []
        for course in self._courses:
            all_students.extend(course.students)

        if not all_students:
            return 0.0

        total_avg = sum(s.calculateAverage() for s in all_students)
        return total_avg / len(all_students)

    def displayInfo(self) -> None:
        print(f"\n=== Department: {self._name} ===")
        print(f"Professors: {[p.name for p in self._professors]}")
        print(f"Courses: {[c.course_name for c in self._courses]}")


# 9. UNIVERSITY

class University:
    def __init__(self, name: str):
        self._name = name
        self._departments: List[Department] = []

    @property
    def name(self):
        return self._name

    @property
    def departments(self):
        return self._departments

    def addDepartment(self, department: Department):
        if department not in self._departments:
            self._departments.append(department)

    def removeDepartment(self, department: Department):
        if department in self._departments:
            self._departments.remove(department)
            print(f"  >> Department '{department.name}' removed from {self._name}.")

    def displayInfo(self) -> None:
        print(f"\n{'='*50}")
        print(f"UNIVERSITY: {self._name}")
        print(f"{'='*50}")
        for dept in self._departments:
            dept.displayInfo()
