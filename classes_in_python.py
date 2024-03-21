#oop concepts
#classes and objects
#classes these are like plans or blueprints that you use to create a particular thing or object
class student:
   student_id=0
   student_name=""
   student_age=0

   def __init__(self,student_id,student_name,student_age):
        self.student_id=student_id
        self.student_name=student_name
        self.student_age=student_age

   def displaystudent(self):
        print("the student details are:Name:",self.student_name,"age",self.student_age)

student1=student(student_id=1,student_name="suzan",student_age=19)
student1.displaystudent()
student2=student(student_id=2,student_name="victor",student_age=26)
student2.displaystudent()
#the object carries the class like it carries the plan or the blueprints of the idea





