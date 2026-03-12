# for i in range(1, 11):
#     print(i * 2, i * 3, i * 4, i * 5, 
#           i * 6, i * 7, i * 8, i * 9, i * 10)


#for(initilization; condition; increment/decrement)
# name = 'piyush'
# data = ['a','e','i','o','u']
# vowel = 0
# cons = 0
# for i in name:
#     if i in data:
#         pass
#     else:
#         cons+=1
#     print("vowel = ", vowel)
#     print("consonent = ", cons)

#     unique_chars = set(name)
#     print(unique_chars)



# newname = ''
# for i in name:
#     if i not in newname:
#         newname += i 
#     print(name)
#     print(newname)


#BODMS
# a = 50
# b = 30
# c = 20
# d = 10
# print((a+b)*c/d)
# print((a-b)*(c/d))
# print(a+(b*c)/d)

# x = ['A','B','C']
# y = ['A','B','C']
# z = [1,2,3,4]
# print(x==y)
# print(x==z)
# print(x !=z)

# mylist =[2,5,8,4,1,9,8]
# even = 0
# odd = 0
# for i in mylist:
#     if i%2 == 0:
#        even += 1
#     else:
#        odd += 1
# print("Even=", even)
# print("Odd=",odd)

# n = [1,2,3,4,5,5,5,1,2,4,4,6,6,6]
# print(n.count(1))
# print(n.count(2))
# print(n.count(3))
# print(n.count(4))
# print(n.count(5))
# print(n.count(6))
# print(n.count(7))


# rollno = [3,5,7,1,11,4,5,2]
# for x in rollno:
#     if x ==2 or x == 4 or x == 6 or x == 8 or x == 10:
#         print("Even no is found ", x)
#         break


# name = "piyush"
# i  = 0
# for x in name:
#     if x == 'n':
#         print("The character present at index no ", i, "value=:",x)
#         break
# i=i+1


# for i in range(1,6):
#     if i==3:
#         continue
#     print(i)

# for i in range(5,0,-1):
#     if i==3:
#         continue
#     print(i)

# for i, j in zip(range(1,6), range(5,0,-1)):
#     if i == 3 and j == 3:
#         continue
#     print(i, " ",j) 

#WAP to accept any character and check the entered character is 
# upper case, lower case, digit and special symbol

# char = input("Enter any char:-")

# if char>=65 and char<=91:
#     print("your entered char is in upper case:-")
# elif char>=97 and char<=122:
#     print("your entered char is in lower case:- ")
# elif ch >= 48 and char 


v = ['a','e','i','o','u']
w = input("Enter the word where we will search the vowels :")
found = []
for i in w:
    if i in v:
        if i not in found:
            found.append(i)
print('foun vovels=', found)
print('unique vovels=',len(found),'from the given word =',w)