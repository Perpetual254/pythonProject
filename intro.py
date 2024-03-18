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

#how to check whether a number is doo or even
y=8
if y % 2 == 0:
   print("even")
else:
   print("odd")


#python casting concetenation
#in this we learn the conversion of integers to strings
first_name="Mercy"
last_name=12
full_name=first_name +"" +str(last_name)
print(full_name)

#strings to integer
pens_total=40
books_total="50"
grand_total=pens_total+int(books_total)

#stirngs to float
bucket=20.0
books="50.0"
total=bucket+float(books)
result="the total is:"+str(total)+"kenyan shillings"
print(result)


#LOOPING IN PYTHON
#the while loop---continue statement
#in this we skip the statement if it satisfies the condition
i=1
while i < 6:
   i+=1 #3
   if i==3: #is 3 equal to 3
     continue
   print("the answer is",i)

#the for loop statement
#in this it repeats depending on the items on the sequence
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

visitors=int(input("enter the number of visitors"))
ugno=0
kenyano=0
counter=1
while counter<=visitors:
    nationality=input("enter the nationality")
    if nationality=="kenyan":
       kenyano+=1
       print("allowed")
       counter+=1
    else:
        ugno+=1
        print("not allowed")
        counter+=1

print("the number of visitors is:",visitors)
print("the number of kenyans is:",kenyano)
print("the number of ugandans is:",ugno)

#funcions
#creating a function
def addition(x,y): #x and y are parameters
    return x+y #the return is used to show the result of wat am doing

#calling a function
print("the sum of 5 and 9 is:",addition(9, 4)) #the values that ive given to x and y are known as arguements









