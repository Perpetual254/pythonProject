#lists in python
x=[1,2,3,4,5,6,7,8,9 ]
for i in range(0,len(x)):
   print(i+1)

students = list()
for i in range(3):
    student_name = input("enter student name")
    students.append(student_name)

print(students)

#tuples
#this are just like lists which can store mutiple variables but they are different
#they use normal brackets and are unchangable but there is around it
fruits = ("apple","banana","orange","grape")
print(fruits)
myfruits = list(fruits)#convert the tuple into lists
myfruits[1] = "mangoes" #do your modification
myfruits.append("pineapples")
fruits = tuple(myfruits)#convert back to a tuple
print(fruits)


#the set data structure in this it uses the carli brackets
#in sets they are unchangable and unodered
#unodered meaning elemets are not indexed
#thisset.add we add things to sets
#thisset.remove we remove things from the set

#dictionaries
#are ordered and cannot be duplicated and are changable
#they are stored in keys

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)







