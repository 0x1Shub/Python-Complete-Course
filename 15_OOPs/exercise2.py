# Student Grade Calculator
# Create a Student class:
# Attributes: name, marks (list of 5 subjects)
# Method:
# calculate_average() – Calculate the average marks.
# display_result() – Print "Pass" if average >= 40, else "Fail".

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        total_sum = sum(self.marks)
        average = total_sum / len(self.marks)
        # print("Average :", int(average))
        return average
    
    def calculate_result(self):
        average = self.calculate_average()
        if average >= 40 :
            print("Pass")
        else:
            print("Fail")

    
student1 = Student("Shubham", [100, 100, 90, 80, 90])
print("Average:",student1.calculate_average())
student1.calculate_result()

