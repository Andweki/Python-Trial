i = 3
while i != 0:
    print("meow")
    i = i - 1

a = 0
while a < 3:
    print("hey")
    a = a + 1

for a in range(3):
    print("hi") 



#students = ["Peter", "Paul", "Mary"]

#for i in range(len(students)):
    #print(i+1,students[i])

#Looping in dictionary with the use of keys
students = [
    {"Name": "Peter", "house":"kiboko","colour":"Blue" }, 
    {"Name": "Paul", "house":"kiboko","colour":"Green"},
    {"Name": "Mary", "house":"Nyati","colour":"Red"}
      ]

#houses = ["simba","Nyati","kiboko",]

for student in students:
    print(student["Name"], student["house"], student["colour"], sep=", ")

       
