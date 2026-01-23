
# ACCESS BOTH KEYS AND VALUES USING ITEMS() FROM DICT

# details={"name":"nani","roll":37}
# for i,j in details.items():
#     print(i,j)


# PYTHON PROGRAM TO CALCULATE THE LENGTH OF STRING

# t="hello this is nani"
# # print(len(t))
# def string_length(str1):
#     count=0
#     for char in str1:
#         count+=1
#     return count
# print(string_length(t))



#python function that accepts a string and calculate the numbers of upper case letters and lower case letters.


# def string_test(s):
#    d={'Upper_case':0,"Lower_case":0}
#    for i in s:
#       if i.isupper():
#          d['Upper_case']+=1
#       elif i.islower():
#          d['Lower_case']+=1
#       else:
#          pass
#     print("Upper case letters:"d["Upper_case"])
#     print("Lower case letters",d["Lower_case"])
#  string_test("Hello This Is vishnu Chaithanya")



# check if the first and last number of a list is the same

# numbers_x=[10,20,30,40,50,10]
# def  first_last(numbers_x):
#     first=numbers_x[0]
#     last=numbers_x[-1]
#     if first==last:
#         return True
#     else:
#         return flase
# print(first_last(numbers_x))


####### create a list of empty dictionaries

# n=20
# n=[{} for _ in range(n)]
# print(n)

###### or ##### single line answer,,,,,

# print([{} for _ in range(60) ])

 
 ### EXTEND A LIST WITHOUT APPEND

# l1=[2,3,4]
# l2=[5,8,9]
# l1.extend(l2)
# print(l1)


# l1=[2,3,4]
# l2=[5,8,9]
# l1.append(l2)
# print(l1)

# l1=[2,3,4]
# l2=[5,8,9]
# l1[0:]=l2
# print(l1)

# l1=[2,3,4]
# l2=[5,8,9]
# l1[:0]=l2
# print(l1)



### pp to solve the fibonacci sequence using recursion...........

# def fib(n):
#     if n==1 or n==2:
#         return 1
#         #(n-1)+(n-2)# formula
#     else:
#         return(fib(n-1)+fib(n-2))
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
# print("largest Number is:",largest)