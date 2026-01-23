
# What is Python?
# Python is a high-level, interpreted programming language.

# What is a function?
# A function is a block of reusable code.



####### some examples ..........

# def word_count(str):
#     counts= dict()
#     words= str.split()
#     for word in words:
#         if word in count:
#             counts[word] += 1
#         else:
#             counts[word] = 1
#     return counts
# print(word_count('the quick brown fox jumps over the lazy dog'))


######## CREATING A LIST OF EMPTY DICTIONARIES

# print([{} for _ in range(20)])



#######  create  a list of empty dictionaries ###########

n=20
s=[{}for i in range(n)]
print(s)

### ONLY SINGLE LINE LOO PRINT CHESTAM DICT,,,,CHUDU,,,

# print([{} for i in range(98)])


############ extend a list without append ####

# l1=[45,66,7,6]
# l2=[54,6,56]
# l1.append(l2)
# print(l1)

# l1=[45,66,7,6]
# l2=[54,6,56]
# l1.extend(l2)
# print(l1)


##### to solve the fibonacci sequence  using recursive ######

# def fib(n):
#     if n==1 or n==2:
#       return 1
#       # (n-1)+(n-2)
#     else:
#        return(fib(n-1)+fib(n-2))
# print(fib(9))
    

### find the largest number among the three input numbers#############


### method 1 ###

# l=[87,89,98,78]
# print(max(l))


######## method 2 ##

# num1=float(input("Enter the Number:"))
# num2=float(input("Enter the Number:"))
# num3=float(input("Enter the Number:"))
 
#  if (num1>=num2) and (num1>=num3):
#      largest=num1
# elif (num2>=num1) and (num2>=num3):
#      largest=num2
# else:
#      largest=num3
# print("largest number is:",largest)



#####  python prog.. to check if a number is positive positive negative or 0,,,,,,,,######
### +, -, 0, ###

# num=float(input("enter the number:"))
# if num>0:
#     print("positive number")
# elif num==0:
#     print("zero")
# else:
#     print("negative")


#### check if the number is an Amstrong number or not
#### without using power function 

m=int(input("enter the number:"))
s=m
b=len(str(m))
sum1=0
while m!=0:
    r=m%10
    sum1=sum1+(r**b)
    m=m//10
if s==sum1:
    print("amstrong number")
else:
    print("not a amstrong number")


##### check if the number even or odd,,,,,
#### a number is even is division by 2 gives a remainder of 0 , it is even number
#### if the number is 1, it is odd number,,

# num=int(input("enter the number:"))
# if num%2==0:
#     print("{0}is even".format(num))
# else:
#     print("{0}is odd".format(num))


##### python prog to get a substring of a string
##### using string slicing

# st="hellonani"
# print(st[0:6])

# l=[4,8,9,7,6,5,8,9,7,8,9] 
# print(l[0:10:3])


##### python prog to get the last element of the list
##### using negative indexing,,

# l=[4,8,7,6,4]
# print(l[3])


# l=[4,8,7,6,4]
# print(l[-1])


### python: add two given lists using map and lambda
## first l1 loo 2nd l2 loo rendu add ayithayi 3+3=6,4+45=59,ila,,,,output vastundi


# l1=[3,4,45,56]
# l2=[3,55,6,65]
# print("orginal list")
# result=map(lambda x,y:x+y,l1,l2)
# print("result")
# print(list(result))
#### python progam to add two matrices using nested loop,,,,

# x=[[12,7,8],
#    [5,7,6],
#    [8,9,4]]

# y=[[6,7,8],
#   [5,6,4],
#    [5,9,8]]

# result=[[0,0,0],
#        [0,0,0],
#         [0,0,0]]
# print(len(x))
# for i in range(len(x)):
#     for j in range(len(x[0])):
#         result[i][j]=x[i][j][+y[i][j]]
# for r in result:
#     print(r)


######  write a program to detect the number of local variable and declared in function

## local variable = inside func
##global variable = outside func

# n=8 # global fun

# def nani():
#     x=2 ## local fun
#     y=3
#     n="nani"
#     d=2.2
# print(nani.__code__.co_nlocals)


### p p to compute all the permutations of the str,,,

# def get_nani(string,i=0):
#     if i==len(string):
#         print("".join(string))
#     for j in range(i,len(string)):
#         words=[c for c in string]
#         words[i],words[j]=words[j],words[i]
#         get_nani(words,i+1)
# get_nani('nani')



### write the numpy program to generate random integers between 1 and 300,

# import numpy as np
# x=np.random.randint(low=1,high=300)
# print(x)


###### program to print half pyramid using,,,

# print("*")
# print("* *")
# print("* * *")
# print("* * * *")

# rows=18
# for i in range(rows):
#     for j in range(i+1):
#         print("@",end=" ")
#     print()


### python prog to remove punctuation from a string,,,

# punctuations="''''!@#$%^&*()_+,."
# mystr=input("enter the string:")
# new_str=""
# for m in mystr:
#     if m not in punctuations:
#         new_str+=m
# print(new_str)


####### python program to reverse a number,,,,,,,,

# nani=9908
# c=str(nani)[::1]
# print(c)


####  transpose a matrix using a nested loop,,,,,,,,,

# x=[[34,6],
#    [6,8],
#    [8,9]]
# result=[[0,0,0],
#         [0,0,0]]

# # import numpy as np    ##### these (#)three lines are apply for comments  then i/p will be  produce...
# # n=np.transpose(x)     ######
# # print(n)              #######

# for  i in range(len(x)):
#     for j in range(len(x[0])):
#         result[j][i]=x[i][j]
# for r in result:
#     print(r)

############## find all numbers which are divisible by7 but not a multiple of 5,,

# l=[]
# for i in range(0,2000):
#     if i%7==0 and i%5!=0:
#         l.append(i)
# print(l)



### write a python function to sum all the numbers in a list,,,,,,

# def sum(numbers):
#     total=0
#     for x in numbers:
#         total+=x
#     return total
# print(sum([6,7,8,9,4,3]))

