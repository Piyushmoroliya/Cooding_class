#while loop

#initialization
#while condition:
#   statement
#   inc/dec

# i = 1 #i=1
# while i<=5:
#     print(i)
#     i = i + 1

# username = " "
# passward = " "
# while username != "admin" and  passward != "hello":
#     username = input("Enter username :")
#     passward = input("Enter passward :")
# print("login successfully ")
#==================================

# mycart=[10,20,200,300,800,60,700]
# for i in mycart:
#     if i > 400:
#         print("this my purchesd card item")
#         continue
#     print(i)

# mydict = {
#     101: "piyush",
#     102: "abhijeet",
#     "103": "mohini",
#     "104": "trivdi",
#     101: "ashish",
#     104: "ashish"
# }
# print(mydict)

#whith the help of key we have to print values
# a = mydict[102]
# print(a)

# mydict[102]='robin'
# print(mydict)

# only print key x = 0,1
# for x in mydict:
#     print(x)


#only print values
# for x in mydict.values():
#     print(x)

#printing key and values both
# for x,y in mydict.items():
#     print(x, y)


# mydict['mobile_no']= 7558228212
# print(mydict)

# mydict.pop(101)
# ============================================

#Palindrome
# name = input("Enter the name :-")

# if name == name[::-1]:
#     print("Plaindrom string")
# else:
#     print("not a palindorm")

# ============================================
#nested for loop

# 111
# 222
# 333

# for i in range(1,4):#outer loop ==> row's
#     for j in range(1,4):#inner loop ==> col's
#         print(i, end=" ")
#     print()
# ============================================

# n = int(input("Enter the num of rows:-"))
# for i in range(1, n + 1):
#     for j in range(1,n+1):
#         print(chr(64+i),end='')
#     print()

# ============================================
# n = int(input("Enter the number of rows:-"))
# for i in range(1, n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()
# ============================================

# n = int(input("Enter the number of rows:-"))
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(i,end=" ")
#     print()
# ============================================

n = int(input("Enter the number of student: "))
d = {}
for i in range(n):
    name = input("Enter student Name:")
    marks=input("Enter student Marks:-")
    d[name]=marks
while True:
    name=input("Enter sttudent Name to get marks: ")
    marks=d.get(name, -1)
    if marks == -1:
        print("student Not Found")
    else:
        print("The Marks of ",name, "are", marks)
    option= input("Do you want to find another student marks [yes|no]")
    if option== "No":
        break
print("Thanks for using our application")
