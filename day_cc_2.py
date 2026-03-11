#write a program to accept any one digit and check pos, negative or zero

# number = int(input("Enter any one number :-"))

# if number> 0:
#     print("numberis positive")
# if number< 0:
#     print("numberis negative")
# if number== 0:
#     print("The number is zero")
# else:
#     print("Not a number")
#===========================================================================

#write a program to accepct day and check working day or weekend

# day = input("Enter the number of working days :-")

# if day == "SATURDAY" or day == "SUNDAY" or day == "saturday" or day == "sunday":
#     print("It's weekend")
# else:
#     print("Working day")
#===========================================================================

# write a program to accepct three paper marks and calculate total marks , 
# percentage and check if percentage is greater of equal to 60 then he or shee is eligible for placement 

# paperOne =  int(input("Enter the marks of first paper :-"))
# paperTwo =  int(input("Enter the marks of two paper :-"))
# paperThree =  int(input("Enter the marks of three paper :-"))

# totalMarks = paperOne + paperTwo + paperThree
# percentage = totalMarks / 3.0
# print("total =", totalMarks)
# print("percetage =", percentage) 

# if percentage >= 60:
#     print("Your eligible for placement")
# else:
#     print("you are not eligible")
#===========================================================================

# wrp to accepct 5 number in 5 different var and check maximum value and print using simple if 

# p1 = int(input("Enter the value of p1:-"))
# p2 = int(input("Enter the value of p2:-"))
# p3 = int(input("Enter the value of p3:-"))
# p4 = int(input("Enter the value of p4:-"))
# p5 = int(input("Enter the value of p5:-"))

# if p1> p2 and p1 > p3 and p1 > p4 and p1 > p5:
#     print("p1 is greater")
# if p2> p1 and p2 > p3 and p2 > p4 and p2 > p5:
#     print("p2 is greater")
# if p3> p1 and p3 > p2 and p3 > p4 and p3 > p5:
#     print("p3 is greater")
# if p4> p1 and p4 > p3 and p4 > p2 and p4 > p5:
#     print("p4 is greater")  
# if p5> p2 and p5 > p3 and p5 > p4 and p5 > p1:
#     print("p5 is greater") 

#nested if else 
# syntax:- 

# if condition-1:
#     if condition-2:
        #statement
    # else:
        #statement
# else:
    # if condition-3:
        #statement
    # else :
       #statement
#===========================================================================

#wrp to accepct three number and check maximum number and print

# condition1 = int(input("Enter the condition One:-"))
# condition2 = int(input("Enter the condition Two:-"))
# condition3 = int(input("Enter the condition Three:-"))

# if condition1 > condition2:
#     if condition1 > condition3:
#         print("n1 is max")
#     else:
#         print("n3 is max")
# else:
#     if condition2> condition3:
#         print("n2 is max")
#     else:
#         print("n3 is max")

#else if ladder

#if condition:
    #statement
#lif condition:
    #statement
#elif condition:
    #statement
#elif:
    #default block
#===========================================================================

#wrp to if percentage is greater than 90 so assign grade A 
#if percentage gretare than 80 assign 'B' and if percantage
#  is gretaer than 60 so assign grade c and if percentage
# is below 60 so print "FAIL"

# percentage = int(input("Enter your percentage:-"))

# if percentage > 90:
#     print("grade A")
# elif percentage > 80:
#     print("grade B")
# elif percentage > 60:
#     print("grade C")
# elif percentage > 40:
#     print("grade D")
# else:
#     print("Fail")
#===========================================================================

#ATM Withdrawal system
#Real-life analogy: ATM checks if balance is enough before cash.
#problem:
#Take account balance and without amount as input .
#conditions:
#If withdrawal amount <= balance = transction successful
#otherwise Insufficint balance
#===========================================================================

# name = "piyushmoroliya"
# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[15]) error 
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])
#===========================================================================
# s = "help4code is a best platform for practicing programming"
# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming"))

#===========================================================================
# s = "Piyush", "Prakash", "Moroliya"
# m = '/'.join(s)
# print(m)
#===========================================================================
# s = "Python is a High level programming Langauge"
# print(s.lower()) 
# print(s.upper()) 
# print(s.swapcase()) 
# print(s.title()) 
# print(s.capitalize()) 
#===========================================================================
# print('Subjects Mraks:-')
# phy = 50
# chem = 60
# math = 70
# print("Physics = {} chemistry={} Math={} ". format(phy,chem,math))
# print("Physics = {0} chemistry={1} Math={2} ". format(phy,chem,math))
# print("Physics = {x} chemistry={y} Math={z} ". format(x=phy,y=chem,z=math))
# total = phy+chem+math
# print("Total Marks",f"{total}")
# print("Roll No=","7".zfill(4))
#===========================================================================
# print('piyush moroliya'.isalnum())
# print('piyushmoroliya'.isalpha())
# print('777f'.isdigit())
# print('sdssdsds'.islower())
# print('PIYUSHm'.isupper())
# print('My Name is piyush'. isupper())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print("Hello".endswith("lo"))

#===========================================================================

import datetime
date = datetime.datetime.now()
print("IT's now:{:%d/ %m/ %Y %H:%M:%S}".format(date))