# x=int(input("Enter a number: "))
# y=int(input("Enter a number: "))
# try:
#     print(x/y)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# finally:
#     print("Done")

# for i in range(5):
#     if i==4:
#         break
#     print(i)
# else:
#     print("Done")

# try:
#     a=int(input("Enter a number: "))
#     print(a)
# except ValueError as e:
#     print(e)
# else:
#     print("Done")

# #to throw an error
# a=int(input("Enter a number:"))
# if a < 0:
#     raise ValueError("Number is negative")
# else:
#     print(a)

## task 1
# while True:
#     try:
#         a=int(input("enter a num:"))
#         print(a)
#         break
#     except ValueError as e:
#         print(e)

# #task 2
# try:
#     l=[1,2,3,4,5,6,7,8,9,10]
#     print(l[10])
# except IndexError as e:
#     print(e)
