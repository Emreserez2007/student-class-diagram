# main.py
from student import Student
from course import Course

s1 = Student(1, "Ali Yılmaz", "ali@mail.com")
c1 = Course("CS101", "Software Engineering")

s1.enroll(c1)

print(s1, "->", [str(c) for c in s1.courses])
print(c1, "->", [str(s) for s in c1.students])
