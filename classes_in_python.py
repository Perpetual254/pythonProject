#oop concepts
#classes and objects
#classes these are like plans or blueprints that you use to create a particular thing or object
class student:
   student_id=0
   student_name=""
   student_age=0

   def __init__(self,student_id,student_name,student_age):
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age

   def displaystudent(self):
        print("the student details are:Name:",self.student_name,"age",self.student_age)

student1 = student(student_id = 1 , student_name="suzan",student_age=19)
student1.displaystudent()
student2 = student(student_id=2,student_name="victor",student_age=26)
student2.displaystudent()

class schools:
     schools_name="my"
     schools_population=50
     def __init__(mywork,schools_name,schools_population):
         mywork.schools_name=schools_name
         mywork.schools_population=schools_population

     def mywork(mywork):
         print("the schools name is" +" "+ mywork.schools_name +" "+ "and population is" +"  " + str(mywork.schools_population))

schools1=schools("Immaculate Primary School" ,1000)
schools1.mywork()
schools2=schools("Kyeni girls high school" ,1500)
schools2.mywork()
#the object carries the class like it carries the plan or the blueprints of the idea you just have to call it after you are done

# learning inheritance
class person:
      person_name="<NAME>"
      person_residence="Springfield"


      def __init__(self,person_name,person_residence):
         self.person_name=person_name
         self.person_residence=person_residence


      def printperson(self):
          print("the person details are :",self.person_name, "and residence",self.person_residence)

class student(person):

      def __init__(self,name,residence):
          super().__init__(name,residence)

student1=student("maxwell","Springfield")
student1.printperson()

class teacher(person):
     pass

#Implementing Polymorphisim#this helps you to be able to code using different words but can have the same function
#we use the same functions in different classes which brings about overriding but brings out different implementation
class animals:
     limbs=4
     eyes=2
     def __init__(self,limbs,eyes):
      self.limbs=limbs
      self.eyes=eyes
      print("the limbs are:",self.limbs,"and eyes are:",self.eyes)

     def makesound(self):
        print("the animal makes the sound of")

class dog(animals):

     def makesound(self):
        print("the animal makes the sound of","barking","i am a dog" )

class goat(animals):

     def makesound(self):
         print("the animal makes the sound of","bleeting","i am a goat")

dog1=dog(4,2)
dog1.makesound()

goat1=goat(4,2)
goat1.makesound()
























