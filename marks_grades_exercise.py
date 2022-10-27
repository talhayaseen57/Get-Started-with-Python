"""
This exercise is to practice 
functions in Python
"""

class student:
    def __init__(self, marks):
        """
        Give a list of your marks obtained out of 100
        """
        self.marks = marks
    
    def average(self):
        sum_of_marks = sum(self.marks)
        num_of_courses = len(self.marks)
        avg = sum_of_marks / num_of_courses
        return avg
    
    def grade(self):
        avg_points = self.average()
        if avg_points >= 90:
            return 5
        elif avg_points >= 80:
            return 4
        elif avg_points >= 70:
            return 3
        elif avg_points >= 60:
            return 2
        else:
            return 1


student1 = student(marks=[89, 92, 85, 98, 96])
print("Average points = " + str(student1.average()))
print("Grade = " + str(student1.grade()))