# Task 6 – Java OOP Assessment

This assessment covers **Encapsulation, Abstraction, Inheritance, and Polymorphism** in Java.

---

## Problem 1 – Encapsulation
Create a class `BankAccount`:
- Private fields: `accountNumber`, `accountHolder`, `balance`.
- Public getter & setter for `accountHolder`.
- Methods:
  - `deposit(double amount)` – increase balance.
  - `withdraw(double amount)` – decrease balance only if sufficient funds exist.
- Write a test `Main` method to:
  - Create a `BankAccount` object.
  - Perform deposits and withdrawals.
  - Print the final balance.

---

## Problem 2 – Abstraction
Design an abstract class `Shape`:
- Abstract methods: 
  - `double calculateArea()`
  - `double calculatePerimeter()`

Create subclasses:
- `Circle` with field `radius`.
- `Rectangle` with fields `length` and `width`.

In a `Main` method:
- Create a list/array of `Shape` objects.
- Print the area and perimeter of each.

---

## Problem 3 – Inheritance & Polymorphism
Create a class hierarchy for an **Employee System**:
- Base class `Employee` with:
  - Fields: `name`, `salary`
  - Method: `getDetails()`

Subclasses:
- `Manager` → field `teamSize`. Override `getDetails()`.
- `Developer` → field `programmingLanguage`. Override `getDetails()`.
- `Intern` → field `mentorName`. Override `getDetails()`.

Create `EmployeeManagementSystem`:
- Store a list of employees.
- Print details of each (demonstrating polymorphism).
