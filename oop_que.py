#Create a Student class with name, age, and marks. Display student details.

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks


s1 = Student("Ashwini", 21, 85)
print('name',s1.name)
print('age',s1.age)
print('marks',s1.marks)



class Student:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks

    def details(self):
        print('name',self.name)
        print('age',self.age)
        print('marks',self.marks)

s1 = Student('ashwini',21,98)
s1.details()


#Create an Employee class with name and salary. Add a method to calculate annual salary.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def annual_salary(self):
        a_salary = self.salary*12
        print('annual_salary',a_salary)
        return a_salary

e1=Employee('ashwini',45000)
e1.annual_salary()


#Create a BankAccount class with deposit and withdrawal methods.

class BankAccount:
    def __init__(self,balance):
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount
        print('deposited ₹',amount)

    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print('withdrawal ₹',amount)
        else:
            print('Insufficient balance')
    def display(self):
        print('remaining balance',self.balance)

ba1=BankAccount(500)
ba1.deposit(250)
ba1.withdraw(751)
ba1.display()


#Create a Car class with brand and model. Add a method to display details.


class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def details(self):
        print('Brand',self.brand)
        print('Model',self.model)

c1= Car('BMW','3 Series')
c1.details()
 

#Create a Rectangle class to calculate area and perimeter.

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        a=self.length*self.width
        print("area of rectangle",a)

    def perimeter(self):
        p=2*(self.length+self.width)
        print('perimeter of rectangle',p)

r1 = Rectangle(14,6)
r1.area()
r1.perimeter()


#Create a Person class and inherit it into a Student class.

class Person:
    def __init__(self,name, age, marks):
        
        self.name = name
        self.age = age
        self.marks = marks
       

    def show(self):
        print(self.name,self.age,self.marks)

class Student(Person):
    def standard(self):
        print(self.name,'is studying in X')
        
        
s1=Student("ashwini",21,89)
s1.show()
s1.standard()


#Demonstrate method overriding using parent and child classes.


class Animal:
    def sound(self):
        print('Animal sound')

class Dog:
    def sound(self):
        print("bark")

class Cat:
    def sound(self):
        print('meow')

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


#Create a class with private attributes and access them using getter and setter methods.


class Employee:
    def __init__(self,salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if salary>0:
            self.__salary = salary
        else:
            print('invalid salary')

e1 = Employee(32000)
print(e1.get_salary())
e1.set_salary(45000)
print(e1.get_salary())


#Demonstrate polymorphism using different classes with the same method name.


class Cat:
    def sound(self):
        print("meow")

class Dog:
    def sound(self):
        print('bark')

class Cow:
    def sound(self):
        print("moo")


animal = [Cat(),Dog(),Cow()]

for i in animal:
    i.sound()


#Demonstrate polymorphism using different classes with the same method name.


from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2
    
    

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

c=Circle(4.2)
r=Rectangle(12,8)

print("area of circle",c.area())
print("area of rectangle",r.area())

    

