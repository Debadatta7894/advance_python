
# # Write a Python program to create a generator that yields the square of numbers from 1 to N.
# def cal(a,b):
#     add =  a + b
#     sub = a - b
#     mul = a * b
#     yield add
#     yield sub
#     yield mul
    
# total = cal(10,2)
# print(next(total))
# print(next(total))
# print(next(total))



# # Write a Python program to create a class named 'Student' with attributes 'name', 'age', and 'email'.

# class student():
#     def __init__(self,name,age,email):
#         self.name = name
#         self.age = age
#         self.email = email
# name = input("Enter your name :")
# age = input("Enter your age :")
# email = input("Enter your email :")

# stu = student(name,age,email)
# print(stu.__dict__)


class Bus:
    def __init__(self,bus_name,source,destination,total_seats,seat_charge,cancel_charge):
        self.bus_name = bus_name
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.seat_charge = seat_charge
        self.cancel_charge = cancel_charge
        
        self.total_book = 0
        self.total_cancel = 0
        
    def book(self,count):
        if self.total_seats - self.total_book >= count:
            self.total_book +=count
        else:
            return 'seat not avl'
    def cancel(self,count):
        self.total_cancel+=count
    
    def summary(self):
        travels = self.total_book - self.total_cancel
        total_collection = travels * self.seat_charge + self.total_cancel * self.cancel_charge
        total_refund = self.total_cancel*(self.seat_charge - self.cancel_charge)
        return travels,total_collection,total_refund
        
        
        
bus_booking = Bus("Dolphin","Bhubanswar","Puri",60,100,30)

# monday : 40 booked ,13 canceled
bus_booking.book(40)
bus_booking.cancel(13)
print('Till monday :-',bus_booking.summary())

#tuesday :-20 bookeed and 8 cancelled
bus_booking.book(20)
bus_booking.cancel(8)
print('Till tuesday :-', bus_booking.summary())

#wednes day :- 25 booked , 0 cancelled
print(bus_booking.book(25))
bus_booking.cancel(0)
print('Till wednesday :-',bus_booking.summary())