#4 Write a closure that returns a function which always adds 5 to any number.
# def add5():
#     def inner(x):
#         return x + 5
#     return inner
# print(add5()(10))

#5 Write a closure that creates a counter function. Each time you call it, it should return the next number.
# def create_counter():
#     count = 0
#     def counter():
#         nonlocal count
#         count += 1
#         return count
#     return counter
# counter = create_counter()
# print(counter())  

#6 Write a decorator that prints "Before function call" before running a function.
# def print_before(a):
#     def wrapper(*args, **kwargs):
#         print("Before function call")
#         return a(*args, **kwargs)
#     return wrapper

# @print_before
# def hello(name):
#     print(f"Hello, {name}!")
# hello("Buzurg")


#7 Write a decorator that checks if a user is authenticated (boolean is_authenticated). If not, it should print "Access denied".
# def require_authentication(f):
#     def wrapper(*args, **kwargs):
#         if not is_authenticated:
#             print("Access denied")
#             return
#         return f(*args, **kwargs)
#     return wrapper
# is_authenticated = True
# @require_authentication
# def view_profile():
#     print("User profile")
# view_profile()  

#9 Write a class Car with attributes brand and speed. Add a method drive() that prints "Driving {brand} at {speed} km/h".
# class Car:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

#     def drive(self):
#         print(f"Driving {self.brand} at {self.speed} km/h")
# my_car = Car("Toyota", 100)
# my_car.drive()

#10 Write a class BankAccount with methods deposit(amount), withdraw(amount), and get_balance(). Ensure that withdrawing more than the balance prints "Not enough money".
# class BankAccount:
#     def __init__(self, initial_balance=0):
#         self.balance = initial_balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Not enough money")
#         else:
#             self.balance -= amount

#     def get_balance(self):
#         return self.balance
# account = BankAccount(100)
# account.deposit(50)
# account.withdraw(30)
# print(account.get_balance())
# account.withdraw(150)

#3 What happens when you use a list as a default argument in a function? Why is it dangerous?
# def append_to_list(value, my_list=[]):
#     my_list.append(value)
#     return my_list
# print(append_to_list(1))  
# print(append_to_list(2))
#Write a query to find all users registered in the last 7 days.