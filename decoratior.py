# def decore4(cal):
#     def all(a,b):
#         add = a + b
#         sub = a - b
#         mul = a * b
#         div = a / b
#         return add,sub,mul,div
#     return all

# def decore3(cal):
#     def division(a,b):
#         res = a / b
#         return res,cal(a,b)
#     return division

# def decore2(cal):
#     def substrc(a,b):
#         res = a - b
#         return res,cal(a,b)
#     return substrc

# def decore(cal):
#     def mul(a,b):
#         res = a * b
#         return res,cal(a,b)
#     return mul  


# @decore4
# @decore3
# @decore2
# @decore
# def cal(a,b):
#     add = a + b
#     return add
# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter a number : "))
# print(cal(num1,num2))



# def decore(func):
#     def odd():
#         print("Odd number :  ")
#         for i in range(1,21):
#             if i % 2 != 0:
#                 print(i,end = ",")
#             print("\nEven number :  ")    
#             func()
#     return odd
# @decore
# def check_num():
#     for i in range(1,21):
#         if i % 2 == 0:
#             print(i,end=",")
# check_num() 



# def decore(func):
#     def odd():
#         print("Odd numbers:")
#         for i in range(1, 21):
#             if i % 2 != 0:
#                 print(i, end=", ")
#         print("\nEven numbers:")
#         func()  
#     return odd 

# @decore
# def check_num():
#     for i in range(1, 21):
#         if i % 2 == 0:
#             print(i, end=", ")

# check_num()






