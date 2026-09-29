# Questions for practice encapsulation
# Q1
class BankAcc:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

# acc1 = BankAcc("harsh", 112)
# print(acc1.get_balance())


# Q2. 
class student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def set_marks(self, updated_marks):
        if 0 < updated_marks <= 100:
            self.__marks = updated_marks
        else:
            print("invaild marks")


# stu1 = student("kamal", 78)
# print(stu1.get_marks())
# stu1.set_marks(98)
# print(stu1.get_marks())


#Q3.

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    def check_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):
            
            if self.__password == old_password:

                if(len(new_password) >= 8):
                    self.__password = new_password
                else:
                    print(f"Password must be 8 characters")

            else:
                print(f"Old Password is incorrect")

# user = User("harsh", "python123")

# print(user.check_password("python123"))

# user.change_password("python123", "django2026")

# print(user.check_password("django2026"))

# user.change_password("wrongpassword", "fastapi123")

# user.change_password("django2026", "abc")



#Q4.

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    # method 1 get_salary
    def get_salary(self):
        return self.__salary

    # mathod 2 set_salary
    def set_salary(self, new_salary):
        if new_salary >= 10000:
            self.__salary = new_salary
        else:
            print(f"Salary must be atleast 10,000")


# employees = [
#     Employee("Harsh", 20000),
#     Employee("Jatin", 25000),
#     Employee("Jitu", 15000)
# ]

# for employee in employees:
#     print(employee.get_salary())


# employees[0].set_salary(25000)

# for employee in employees:
#     print(employee.get_salary())

# employees[1].set_salary(5000)

# for employee in employees:
#     print(employee.get_salary())


#Q5.
class Bank_Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def show_balance(self):
        return self.__balance

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.__balance += deposit_amount
        else:
            print(f"Invalid Amount")

    def withdraw(self, withdraw_amount):
        if 0 < withdraw_amount <= self.__balance:
            self.__balance -= withdraw_amount
            print(f"{withdraw_amount} withdrawal sucessfully")
        else:
            print(f"Insufficient Balance")

# account = Bank_Account("Mohit", 500)
# print(account.show_balance())

# account.deposit(400)
# print(account.show_balance())

# account.withdraw(150)
# print(account.show_balance())


# Q6.
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.__price = price
        self.__quantity = quantity


    def set_price(self, price):
        if price > 0:
            self.__price = price
        else:
            raise ValueError("Invalid price")

    def set_quantity(self, quantity):
        if quantity > 0:
            self.__quantity = quantity
        else:
            raise ValueError("Invalid Quantity")

    def get_total_value(self):
        return self.__price * self.__quantity


# product = Product("laptop", 50000, 2)

# print(product.get_total_value())


# try:
#     product.set_price(-5000)
# except ValueError as e:
#     print(e)


#Q7

class Student:

    def __init__(self, name):
        self.name = name
        self.__marks = {}

    def add_subject(self, subject, marks):
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be from 0 to 100")
        
        if subject in self.__marks:
            raise ValueError("Subject is already exist")
        
        self.__marks[subject] = marks

    def update_marks(self,subject, marks):
        if not 0 <= marks <= 100:
            raise ValueError("Marks must be from 0 to 100")

        if subject not in self.__marks:
            raise ValueError("Subject doesn't exist")
        
        self.__marks[subject] = marks

    def get_marks(self, subject):
        if subject not in self.__marks:
            raise ValueError("Subject doesn't exist")

        return self.__marks[subject]

    def get_average(self):
        if len(self.__marks) == 0:
            return 0

        return sum(self.__marks.values()) / len(self.__marks)

# student = Student("Harsh")

# student.add_subject("Python", 85)
# student.add_subject("SQL", 78)
# student.add_subject("Django", 90)

# print(student.get_marks("Python"))

# student.update_marks("Python", 95)

# print(student.get_marks("Python"))

# print(student.get_average())

# print("------------------------------------------------------------------------------------")


# Q8
class Person:

    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        print(f"Fetching....")

        return self.__age

    @age.setter
    def age(self, new_age):
        if not 0 < new_age <= 120:
            raise ValueError("Invaild Age")
        else:
            self.__age = new_age

        return self.__age

# person = Person(21)

# print(person.age)

# person.age = 25
# print(person.age)


# Q9
class Vehicle:

    def __init__(self, brand, speed=0, fuel=100):
        self.brand = brand
        self.__speed = max(0, min(speed, 200))
        self.__fuel = max(0, min(fuel, 100))

    def get_speed(self):
        return self.__speed

    def get_fuel(self):
        return self.__fuel

    def accelerate(self, amount):

        if amount <= 0:
            print("Acceleration amount must be greater than 0.")
            return

        # Maximum acceleration possible because of speed limit
        speed_capacity = 200 - self.__speed

        # Actual requested acceleration
        actual_amount = min(amount, speed_capacity)

        # Fuel required for actual acceleration
        fuel_needed = actual_amount / 10

        # Check whether enough fuel is available
        if fuel_needed > self.__fuel:
            # Use all remaining fuel
            fuel_needed = self.__fuel
            actual_amount = fuel_needed * 10

        # Update speed and fuel
        self.__speed += actual_amount
        self.__fuel -= fuel_needed

        print(
            f"[{self.brand}] "
            f"Speed: {self.__speed:.1f} km/h | "
            f"Fuel: {self.__fuel:.1f} L"
        )

    def brake(self, amount):

        if amount <= 0:
            print("Brake amount must be greater than 0.")
            return

        self.__speed = max(self.__speed - amount, 0)

        print(
            f"[{self.brand}] "
            f"Speed: {self.__speed:.1f} km/h"
        )

    def refuel(self, amount):

        if amount <= 0:
            print("Refuel amount must be greater than 0.")
            return

        actual_amount = min(amount, 100 - self.__fuel)

        self.__fuel += actual_amount

        print(
            f"[{self.brand}] "
            f"Fuel: {self.__fuel:.1f} L"
        )


# car = Vehicle("Tata", 50, 60)

# car.accelerate(30)

# print(car.get_speed())
# print(car.get_fuel())

# car.brake(20)

# print(car.get_speed())

# car.refuel(10)

# print(car.get_fuel())

# Q.10

class Wallet:

    def __init__(self, owner, balance = 0):
        self.__owner = owner
        self.__balance = balance
        self.__transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit amount must be greater than zero..")
        self.__balance += amount

        self.__transactions.append({
            "type": "deposit",
            "amount": amount
        })

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > self.__balance:
            raise ValueError("Insufficient balance.")

        self.__balance -= amount

        self.__transactions.append({
        "type": "withdraw",
        "amount": amount
        })

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions.copy()

    def get_total_deposited(self):
        total = 0

        for transaction in self.__transactions:
            if transaction["type"] == "deposit":
                total += transaction["amount"]

        return total

    def get_total_withdraw(self):
        total = 0

        for transaction in self.__transactions:
            if transaction["type"] == "withdraw":
                total += transaction["amount"]

        return total


# wallet = Wallet("Harsh")

# wallet.deposit(10000)
# wallet.withdraw(2500)
# wallet.deposit(5000)

# print("Balance:", wallet.get_balance())
# print("Transactions:", wallet.get_transactions())
# print("Total Deposited:", wallet.get_total_deposited())
# print("Total Withdrawn:", wallet.get_total_withdraw())