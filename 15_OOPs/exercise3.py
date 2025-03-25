# Exercise on Combining Objects

# Question 1: Student and Course
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    
    def show_students(self):
        print(f"Students in {self.course_name}:")
        for student in self.students:
            print(f"Student Name: {student.name}, ID: {student.student_id}")


student1 = Student('Shubham', 1)

course1 = Course("Python")
course1.add_student(student1)
course1.show_students()


# Question 2: Author and Book

class Author:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Book:
    def __init__(self, title):
        self.title = title
        self.author = None

    def add_author(self, author):
        self.author = author

    def display_info(self):
        print(f"Book Title: {self.title}")
        if self.author:
            print(f"Author Name: {self.author.name}")
            print(f"Author Age: {self.author.age}")
        else:
            print("No author assign")



author1 = Author("Shubham", 22)
book1 = Book("ABC")
book1.add_author(author1)
book1.display_info()
