# Python OOP Practice — Encapsulation

This folder contains my **Python Object-Oriented Programming (OOP) practice** focused on **Encapsulation**.

I have implemented **10 practice questions**, progressing from basic private attributes and getters/setters to more advanced state management using properties, validation, lists, dictionaries, and transaction tracking.

## 📂 File Structure

```text
python-oop-practice/
│
├── encapsulation/
│   ├── encapsulation.py
│   └── README.md
│
└── ...
```

## 🎯 Learning Objectives

Through these exercises, I practiced:

* Private attributes using `__`
* Getters and setters
* Data validation
* Encapsulation of object state
* `raise ValueError`
* Lists and dictionaries inside classes
* `@property` and property setters
* Managing object state safely
* Working with multiple objects
* Transaction and balance management
* Writing reusable class methods

## 📝 Practice Questions

### Q1 — Bank Account

Created a `BankAcc` class with:

* Owner
* Private balance
* Getter method for balance

**Concepts:** Private attributes, getters.

---

### Q2 — Student Marks

Created a `student` class that stores marks privately and allows marks to be updated only when they are within a valid range.

**Concepts:**

* Private attributes
* Getter
* Setter
* Validation

---

### Q3 — User Password

Created a `User` class with password protection.

Features include:

* Password verification
* Changing password
* Old password validation
* Minimum password length validation

**Concepts:** Encapsulation, validation, authentication-style logic.

---

### Q4 — Employee Salary

Created an `Employee` class with a private salary.

The salary can only be changed when the new salary satisfies the minimum salary requirement.

**Concepts:**

* Private attributes
* Getters/setters
* Validation
* Working with multiple objects

---

### Q5 — Bank Account Operations

Created a `Bank_Account` class supporting:

* Checking balance
* Depositing money
* Withdrawing money
* Insufficient balance validation

**Concepts:** Encapsulation, state modification, validation.

---

### Q6 — Product Management

Created a `Product` class containing:

* Product name
* Private price
* Private quantity
* Price validation
* Quantity validation
* Total inventory value calculation

**Concepts:**

* Private attributes
* Validation
* Exceptions
* Calculations using object state

---

### Q7 — Student Subject Management

Created a `Student` class that manages subjects and marks using a private dictionary.

Features include:

* Add subject
* Update marks
* Get marks
* Prevent duplicate subjects
* Validate marks between 0 and 100
* Calculate average marks

**Concepts:**

* Encapsulation
* Dictionaries
* Validation
* Exceptions
* Data processing

---

### Q8 — Property Decorator

Created a `Person` class using:

```python
@property
```

and:

```python
@age.setter
```

The age is stored privately and validated when changed.

**Concepts:**

* `@property`
* Property setters
* Private attributes
* Data validation

---

### Q9 — Vehicle

Created a more advanced `Vehicle` class with private:

* Speed
* Fuel

Features include:

* Acceleration
* Braking
* Refueling
* Maximum speed validation
* Fuel limitations
* Automatic adjustment based on available fuel

**Concepts:**

* Encapsulation
* State management
* Validation
* Conditional logic
* Real-world object modelling

---

### Q10 — Digital Wallet

Created a `Wallet` class that manages:

* Owner
* Balance
* Transactions
* Deposits
* Withdrawals
* Transaction history
* Total deposited amount
* Total withdrawn amount

Transactions are stored as dictionaries inside a private list.

Example transaction:

```python
{
    "type": "deposit",
    "amount": 10000
}
```

The transaction history is returned using a copy to protect the internal list.

**Concepts:**

* Advanced encapsulation
* Private state
* Lists of dictionaries
* Transaction tracking
* Data validation
* Defensive copying
* State management

## 📊 Progression

| Question | Topic                       | Difficulty              |
| -------- | --------------------------- | ----------------------- |
| Q1       | Private Attribute & Getter  | Beginner                |
| Q2       | Getter, Setter & Validation | Beginner                |
| Q3       | Password Encapsulation      | Beginner                |
| Q4       | Salary Management           | Beginner → Intermediate |
| Q5       | Bank Transactions           | Intermediate            |
| Q6       | Product & Exceptions        | Intermediate            |
| Q7       | Dictionary-Based State      | Intermediate            |
| Q8       | `@property`                 | Intermediate            |
| Q9       | Vehicle State Management    | Advanced                |
| Q10      | Digital Wallet              | Advanced                |

## 🛠️ Technologies

* Python 3
* Object-Oriented Programming
* Encapsulation
* Exception Handling
* Lists
* Dictionaries
* `@property`

## ▶️ How to Run

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project:

```bash
cd python-oop-practice
```

Run the encapsulation file:

```bash
python encapsulation/encapsulation.py
```

Most practice examples are currently commented out in the file. Uncomment the required example at the bottom of each question to test it.

## 📚 What I Learned

After completing these exercises, I understand how encapsulation can be used to control and protect an object's internal state.

I also learned how to:

* Hide implementation details using private attributes
* Control how data is modified
* Validate user input
* Raise exceptions for invalid operations
* Use properties to provide controlled access
* Design classes around real-world entities
* Maintain consistent object state

## 🚀 Next Topic

**Inheritance**

The next stage of my Python OOP practice will focus on inheritance, followed by:

1. Inheritance
2. Polymorphism
3. Abstraction
4. Magic/Dunder Methods
5. Composition
6. OOP Mini Projects
