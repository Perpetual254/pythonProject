#for loops in python
students=["george","maria","vansh"]
for x in students :
    print(x)

#the range function
#this is the no, of times you want your items
for m in range(6):
    print("perpetual")

#nested loops
#this is putting a loop inside another loop
adj=["red","big","tasty"]
fruits=["apple","banana","orange"]
country=["kenya","france","germany"]
for x in adj:
 for y in fruits:
   for z in country:
    print(x,y,z)


#using the range version
adj=["red"]
fruits=["apple","banana","orange"]
for x in adj:
   for y in fruits:
     for z in range(3):
      print(x,y)


#using the while version
adj=["red"]
fruits=["apple","banana","orange"]
for x in adj:
   for y in fruits:
     while x<="3" and y<="3":
      print(x,y)








