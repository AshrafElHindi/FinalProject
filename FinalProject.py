class Course:
    def __init__(self, course_name, course_level):
        self.course_id = None  # Generated incrementally
        self.course_name = course_name
        self.course_level = course_level


class Student:
    def __init__(self, student_name, student_level):
        self.student_name = student_name
        self.student_id = None  # Generated incrementally
        self.student_level = student_level
        self.student_courses = []

    def add_course(self, course):
        if course.course_level == self.student_level:
            self.student_courses.append(course)
            print(f"Course {course.course_name} added to student {self.student_name}'s courses.")
        else:
            print("Cannot add course due to class mismatch.")

    def display_details(self):
        print(f"Student Name: {self.student_name}")
        print(f"Student Level: {self.student_level}")
        print("Courses Enrolled:")
        for course in self.student_courses:
            print(f"  Course ID: {course.course_id}, Course Name: {course.course_name}")


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.student_id_counter = 1
        self.course_id_counter = 1

    def add_new_student(self):
        student_name = input("Enter student name: ")
        student_level = input("Enter student level (A-B-C): ").upper()
        while student_level not in ['A', 'B', 'C']:
            student_level = input("Invalid input. Enter student level (A-B-C): ").upper()
        new_student = Student(student_name, student_level)
        new_student.student_id = self.student_id_counter
        self.student_id_counter += 1
        self.students.append(new_student)
        print("Student saved successfully.")

    def remove_student(self):
        student_id = int(input("Enter student ID: "))
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Delete done successfully.")
                return
        print("User does not exist.")

    def edit_student(self):
        student_id = int(input("Enter student ID: "))
        for student in self.students:
            if student.student_id == student_id:
                new_name = input("Enter new name: ")
                new_level = input("Enter new level (A-B-C): ").upper()
                while new_level not in ['A', 'B', 'C']:
                    new_level = input("Invalid input. Enter new level (A-B-C): ").upper()
                student.student_name = new_name
                student.student_level = new_level
                print("Edit done successfully.")
                return
        print("User does not exist.")

    def display_all_students(self):
        for student in self.students:
            student.display_details()

    def create_new_course(self):
        course_name = input("Enter course name: ")
        course_level = input("Enter course level (A-B-C): ").upper()
        while course_level not in ['A', 'B', 'C']:
            course_level = input("Invalid input. Enter course level (A-B-C): ").upper()
        new_course = Course(course_name, course_level)
        new_course.course_id = self.course_id_counter
        self.course_id_counter += 1
        self.courses.append(new_course)
        print("Course created successfully.")

    def add_course_to_student(self):
        student_id = int(input("Enter student ID: "))
        course_id = int(input("Enter course ID: "))
        student_found = False
        course_found = False
        for student in self.students:
            if student.student_id == student_id:
                student_found = True
                for course in self.courses:
                    if course.course_id == course_id:
                        course_found = True
                        student.add_course(course)
                        break
                break
        if not student_found:
            print("Student does not exist.")
        elif not course_found:
            print("Course does not exist.")


# Main program
school_system = SchoolSystem()

while True:
    print("\nMenu:")
    print("1. Add New Student")
    print("2. Remove Student")
    print("3. Edit Student")
    print("4. Display All Students")
    print("5. Create New Course")
    print("6. Add Course to Student")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        school_system.add_new_student()
    elif choice == '2':
        school_system.remove_student()
    elif choice == '3':
        school_system.edit_student()
    elif choice == '4':
        school_system.display_all_students()
    elif choice == '5':
        school_system.create_new_course()
    elif choice == '6':
        school_system.add_course_to_student()
    elif choice == '0':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select again.")
