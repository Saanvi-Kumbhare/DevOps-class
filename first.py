# student={
#     "name":"Saanvi",
#     "age":21,
#     "marks":85
# }

# print(student["name"])
# print(student.get("age"))

# student["marks"]=90
# print(student["marks"])

# student["grade"] = 'A'
# print(student["grade"])

# student.pop("age")

# print(student)

# t1 = (1,2,3)
# t2 = ("apple","banana","mango")
# print(t1)
# print(t2)

# print(t1[0])

# a,b,c=t1
# print(a,b,c)

# t3=t1+(4,5)
# print(t3)


# text = "Data Structure" 
# # Length
# print(len(text)) 
# # Concatenation 
# print(text + " Notes") 
# # Upper and Lower 
# print(text.upper()) 
# print(text.lower()) 
# # Replace 
# print(text.replace("Data", "Info")) 
# # Splitting 
# print(text.split(" ")) 
# # Check substring 
# print("Data" in text)
 
# word = "madam" 
# if word == word[::-1]: 
#     print("Palindrome") 
# else: 
#     print("Not Palindrome")

age = int(input("Enter your age: "))
if age>=18 :
    print("Eligible")
else :
    print("Not eligible")