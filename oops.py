# 4 pillars of oops 

# Encapsulation
# class A:
#     def __init__(self,name,age,gender):
#         #constructor
#         self.__name=name #private var can be accessed inside of same class which defines with __
#         self._age=age #protected var can be accessed inside of same class which defines with _
#         self.gender=gender #public var can be accessed inside of same class and outside of class which defines without any prefix
#     def display(self):
#         print(self.__name)
#         print(self._age)
#         print(self.gender)
#     def setAge(self,age):
#         self._age=age
#     def getAge(self):
#         return self._age
# a1=A("Shaaz",20,"Female")
# # a2=A("San",21,"Male")
# print(a1.display())
# a1.setAge(22)
# print(a1.display())

# Abstraction
# from abc import ABC, abstractmethod
# class BankAccount(ABC):
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amount):
#         self.__balance+=amount
#     def withdraw(self,amount):
#         self.__balance-=amount
#     def getBalance(self):
#         return self.__balance
#     @abstractmethod
#     def interestcalc(self):
#         pass
# class SavingsAccount(BankAccount):
#     def interestcalc(self):
#         return self.getBalance()*0.05   

# Polymorphism
class Animal:
    print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Bow bow")
class Cat(Animal):
    def sound(self):
        print("Meow meow")
        
# Inheritance