#learning about variables



x=5
y="gerald"
price=55.0


#variable naming in python


#operators
x=5
x+=3 #this is like saying x=x+3
x=x+3
x*=4
print("my answer is:",x)

#!=means not equal to
p=5
q=3

print(p!=q)

#conditional statements
age =50

#the if statement-code executes when the condition is only true
#and nothing happens when the condition is false
if age>=18:
   print("you are an adult")

#the if...elif statement
if age >18:
   print("Adult")
elif age<18:
   print("child")

#the if...elif...else statement
a=200
b=33
if a > b:
   print("a is greater then b")
elif a==b:
   print("a and b are equal")
else:
   print("a is less than b")

#using the AND statement
president_age=20
nationality="ugandan"

if president_age>=18 and  nationality=="kenyan":
   print("you are a successful candidate ")
else:
   print("you are not a successful candidate")


#checking the or statement
if nationality=="kenya" or nationality=="uganda" or nationality=="tanzania":
   print("you qualify foe cecafa") #in or if u meet either of the conditions it executes
else:
   print("you qualify")


   


