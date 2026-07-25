# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# #right angled triangle
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# #inverted right angled triangle
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("*",end=" ")
#     print()

# #Diamond pattern
# n=5 
# for i in range(n): 
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()
# for i in range(n-2,-1,-1):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for j in range(2*i+1):
#         print("*",end=" ")
#     print()

# #Armstrong number
# n=int(input("Enter a number: "))
# sum=0
# temp=n
# while temp>0:
#     digit=temp%10
#     sum+=digit**3
#     temp//=10
# if sum==n:
#     print(n,"is an Armstrong number")
# else:
#     print(n,"is not an Armstrong number")   

# #Hollow square pattern  
# """
# * * * * * 
# *       *
# *       *
# * * * * *
# """
# n=int(input("Enter a number: "))
# for i in range(n):
#     for j in range(n):
#         if i==0 or i== n-1 or j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#pascal's triangle
""" 
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1 
"""
# n=int(input("Enter the num of rows: "))
# for i in range(n):
#     print(" " *(n-i-1),end="")
#     num=1
#     for j in range(i+1):
#         print(num,end=" ")
#         num=num*(i-j)//(j+1)
#     print()

