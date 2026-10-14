# Here is the solution of the inheritance problem
#Q1 - Basic Inheritance
class Animal:
    def eat(self):
        print("Animal is eating...")


class Dog(Animal):
    def bark(self):
        print("Dog is barking....")

dog = Dog()

# dog.eat()
# dog.bark()


# Q2 - Constructor Inheritance
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age,course):
        self.name = name
        self.age = age
        self.course = course

    def show_details(self):
        print(f"Name: {self.name}\nAge: {self.age}\nCourse: {self.course}")

student = Student("Harsh", 21, "Computer Science")
# student.show_details()

# Q3 — super() and Constructor Reuse
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_details(self):
        print(f"Name : {self.name}\nSalary : {self.salary}\nDepatment : {self.department}")

manager = Manager("Jatin", 10000, "Development")
# manager.show_details()

# Q4 — Method Overriding

class Animal:

    def sound(self):
        print("Animal make a sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Cat(Animal):
    def sound(self):
        print("Cat Meows")

dog = Dog()
cat = Cat()

# dog.sound()
# cat.sound()

# Q5. Inheritance + Encapsulation

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Please enter a valid amount.")
        self.__balance += amount
        print(f"{amount} deposited in your account sucessfully.")

    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):

    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        self.deposit(interest)

        print(f"Interest of ₹{interest:.2f} added to the account.")

# account = SavingsAccount("Harsh", 10000, 5)

# print(account.get_balance())

# account.deposit(2000)
# account.add_interest()

# print(account.get_balance())


# Q6. Multilevel Inheritance

class Vehicle:

    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        return self.brand

class Car(Vehicle):

    def __init__(self, brand, fuel_type):
        super().__init__(brand)
        self.fuel_type = fuel_type

    def show_details(self):
        print(f"Brand : {self.brand}\nFuel_type : {self.fuel_type}")

class ElectricCar(Car):

    def __init__(self, brand, fuel_type, battery_capacity):
        super().__init__(brand, fuel_type)
        self.battery_capacity = battery_capacity

    def show_details(self):
        print(f"Brand : {self.brand}\nFuel_type : {self.fuel_type}\nBattery Capacity : {self.battery_capacity}")

# car = ElectricCar("Tata", "Electric", 40)
# car.show_brand()
# car.show_details()

# Q7. Hierarchical Inheritance

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_employee(self):
        return self.name and self.salary

class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_details(self):
        print(f"Name : {self.name}\nSalary : {self.salary}\nProgramming language : {self.programming_language}")

class Designer(Employee):

    def __init__(self, name, salary, design_tool):
        super().__init__(name, salary)
        self.design_tool = design_tool

    def show_details(self):
        print(f"Name : {self.name}\nSalary : {self.salary}\nDesign_tool : {self.design_tool}")

# dev = Developer("Harsh", 50000, "Python")
# designer = Designer("Jatin", 45000, "Figma")

# dev.show_details()
# designer.show_details()


# Q8. Multiple Inheritance

class Camera:
    def take_photo(self):
        print(f"Take a Photo...")

class Phone:
    def make_call(self):
        print(f"Making a call..")

class Smartphone(Camera, Phone):
    def browse_internet(self):
        print(f"Browsing a Internet...")

phone = Smartphone()

# phone.take_photo()
# phone.make_call()
# phone.browse_internet()


# Q9 — Inheritance + Polymorphism

class Payment:
    def pay(self, amount):
        print(f"Processing payment of {amount}")

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Processing UPI payment of {amount}")

class CardPayment(Payment):
    def pay(self, amount):
        print(f"Processing Card payment of {amount}")

payments = [UPIPayment(), CardPayment()]

# for payment in payments:
#     payment.pay(1500)


# Q10 — Advanced Inheritance Challenge

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary < 10000:
            raise ValueError("New Salary must be greater then 10,000")
        else:
            self.__salary = new_salary


    def show_details(self):
        print(f"Name : {self.name}\nSalary : {self.get_salary()}")

class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        super().__init__(name ,salary)
        self.programming_language = programming_language

    def show_details(self):
        print(f"Name : {self.name}\nSalary : {self.get_salary()}\nProgramming Language : {self.programming_language}")

class Manager(Employee):

    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def show_details(self):
        print(f"Name : {self.name}\nSalary : {self.get_salary()}\n Team Size : {self.team_size}")


# employees = [
#     Developer("Harsh", 50000, "Python"),
#     Manager("Jatin", 70000, 5)
# ]

# for employee in employees:
#     employee.show_details()


# employees[0].set_salary(60000)
# print(employees[0].get_salary())
