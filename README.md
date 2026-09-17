# University-Management-System
A Python-based university management system built to demonstrate core Object-Oriented Programming (OOP) principles. This project models a real-world academic environment with a clean class hierarchy covering people, courses, departments, and a university structure.
---

# University Management System (OOP Assignment)

## Project Purpose
This project was developed as an assignment to demonstrate a deep understanding of Object-Oriented Programming (OOP) principles in Python. The primary purpose is to design and implement a structured, scalable, and maintainable system for managing the core entities of a university, such as people (students, professors, administrators), courses, and departments. The code serves as a practical example of how to model real-world relationships and hierarchies using OOP concepts.

## Problem Being Addressed
Managing a university's complex ecosystem requires a robust system to handle various interrelated entities. Without a structured approach, the code would become a tangled mess of functions and data structures, making it difficult to maintain, extend, or debug. This project addresses the problem of creating a clear, logical, and organized model to handle:
- Different types of people (students, employees) with shared and unique attributes.
- The relationship between professors and the courses they teach.
- The relationship between students and the courses they are enrolled in.
- The hierarchical structure of a university, containing multiple departments, each with its own set of courses and professors.
- Automated calculations like salaries and student averages based on predefined rules.

## Technologies / Programming Languages Used
- **Language:** Python 3
- **Core Libraries:** `abc` (Abstract Base Classes), `typing` (Type Hinting)

## Main Features
This system is built around several key classes, each representing a distinct entity within a university.

- **Person & Employee Hierarchy:**
    - A `Person` abstract base class (ABC) ensures all people entities have a name and ID.
    - An `Employee` ABC extends `Person` to include employee-specific attributes like salary and employee ID.

- **Role-Specific Classes:**
    - `Administrator`: Represents an employee with a specific position and a fixed salary.
    - `Professor`: Represents an employee with a specialization. Their salary is dynamically calculated with a bonus based on the number of courses they teach.
    - `Student`: Represents a person with a program, a list of grades, and enrolled courses. Their "student type" (Honors/Bachelors) is automatically determined based on their average grade.

- **Course Management:**
    - `Course`: Acts as a central hub. It holds a list of enrolled students, a list of assignments, and is assigned a professor. It can calculate the average grade for all students in the course.

- **Assignment Tracking:**
    - `Assignment`: Represents a single assignment with a title, due date, and marks.

- **Organizational Structure:**
    - `Department`: A collection of professors and courses. It can calculate the average grade of all students across all its courses.
    - `University`: The top-level entity that contains multiple departments and allows for their addition and removal.

- **Comprehensive `displayInfo` Methods:**
    - Nearly every class has a `displayInfo` method to provide a clear, human-readable summary of its state, making the system easy to inspect and debug.

## How to Run or Use the Project
This project is a Python script, not a standalone application. It can be run in any standard Python 3 environment.

1.  **Prerequisites:** Ensure you have Python 3 installed on your system.
2.  **Execution:** Save the code as a Python file (e.g., `university_system.py`) and run it from your terminal:
    ```bash
    python university_system.py
    ```
3.  **Usage Example:** The provided code includes the class definitions. To see the system in action, you would create instances of these classes in a script. Here is a simple example:

    ```python
    # --- Example Usage ---

    # 1. Create a University
    my_university = University("State Tech University")

    # 2. Create Departments
    cs_dept = Department("Computer Science")
    math_dept = Department("Mathematics")

    # 3. Add departments to the university
    my_university.addDepartment(cs_dept)
    my_university.addDepartment(math_dept)

    # 4. Create Professors
    prof_smith = Professor("Dr. Alan Smith", 101, 5001, 90000, "Artificial Intelligence")
    prof_jones = Professor("Dr. Evelyn Jones", 102, 5002, 95000, "Calculus")

    # 5. Add professors to departments
    cs_dept.addProfessor(prof_smith)
    math_dept.addProfessor(prof_jones)

    # 6. Create Courses
    cs_course = Course("CS101", "Intro to Programming")
    math_course = Course("MATH201", "Calculus I")

    # 7. Add courses to departments and assign professors
    cs_dept.addCourse(cs_course)
    cs_course.setProfessor(prof_smith)

    math_dept.addCourse(math_course)
    math_course.setProfessor(prof_jones)

    # 8. Create Students
    student_alice = Student("Alice", 201, 10001, "Computer Science")
    student_bob = Student("Bob", 202, 10002, "Mathematics")

    # 9. Enroll students in courses
    student_alice.enrollInCourse(cs_course)
    student_alice.enrollInCourse(math_course)
    student_bob.enrollInCourse(math_course)

    # 10. Add assignments and grades
    hw1 = Assignment("Coding Project 1", "2024-10-01")
    cs_course.addAssignment(hw1)
    student_alice.addGrade(92.5)
    student_bob.addGrade(88.0)

    # 11. Display Information
    my_university.displayInfo()
    cs_course.displayInfo()
    student_alice.displayInfo()
    ```

## What I Learned from the Project
This project was a valuable exercise in applying advanced OOP concepts to solve a practical problem. The key takeaways include:

- **Abstraction and Inheritance:** I learned how to design a class hierarchy using Abstract Base Classes (`ABC`) to define a common interface (`Person`, `Employee`) and enforce contracts (`displayInfo`, `calculateSalary`) for subclasses.
- **Polymorphism:** I implemented polymorphic behavior where different `Employee` subclasses (`Professor`, `Administrator`) provide their own specific implementation for `calculateSalary`, allowing for flexible and extensible code.
- **Encapsulation:** By using Python's property decorators (`@property`) and name-mangling (e.g., `_name`), I practiced hiding internal state and exposing it through controlled getters and setters, promoting data integrity.
- **Composition and Relationships:** I modeled complex, real-world "has-a" relationships (e.g., a `University` *has* `Departments`, a `Course` *has* `Students` and a `Professor`). This was crucial for building a cohesive system from smaller, independent objects.
- **Managing Complex Data Structures:** The project required careful management of lists of objects and handling bidirectional relationships (e.g., adding a student to a course also adds that course to the student's list) to maintain data consistency.
