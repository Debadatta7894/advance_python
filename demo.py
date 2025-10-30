# print ("Hello World")



# numbe = int(input("Enter numbr :"))
# if(numbe % 2 ==0):
#     print("EVEN")
# else:
#     print("ODD")



# pre = int(input("Enter percentage :"))

# if(pre >= 90):
#     print("This is Good A+", pre,"%")
# elif(pre >=80 and pre < 90):
#     print("This is B", pre,"%")
# elif(pre >=70 and pre < 80):
#     print("This is C", pre,"%")
# elif(pre >=30 and pre < 70):
#     print("This is D", pre,"%")
# else:
#     print("Not pass", pre,"%")    


# a = int(input("Enter 1st Numbe :" ))
# b = int(input("Enter 2nd Numbe :" ))
# c = int(input("Enter 3rd Numbe :" ))
# d = int(input("Enter 4th Numbe :" ))

# if(a>b and a>c and a>d):
#     print("A is Big Numbe :", a)
# elif(b>c and b>d):
#     print("B is Big Numbe :", b)   
# elif(c>d):
#     print("C is Big Numbe :", c)
# else:
#     print("D is Big Numbe :", d)



# num = int(input("Enter a number :"))

# if(num % 7 == 0):
#     print("This is valid Number.and This number is ",num)
# else:
#     print( num,"is Not Vlaid. Enter a valid Number")




# list = [2,1,3]
# list.sort()
# print(list)

# list = [2,1,3,5,2,5]
# list.insert(1, 10)
# print(list)

# list = [2,1,3,5,2,5]
# list.insert(1, "litu")
# print(list)

# all_film=[]

# film = input("Enter 1st film name :")
# film1 = input("Enter 2st film name :")
# film2 = input("Enter 3st film name :")

# all_film .append(film)
# all_film .append(film1)
# all_film .append(film2)
# print(all_film)


# grade=["C","D","A","A","B","B","A"]
# grade.count("A")
# print(grade.count("A"))

# val = ["D","A","C","B"]
# val.sort()
# print(val)


# info = {
#     "key":"value",
#     "marks":[28,98,83,92],
#     "sub":('eng','math','odia','Science'),
#     "name":"Debadatta",
#     "age":24,
#     "passing year": 2021
# }
# print(info)
# print(info["name"])
# print(info["marks"])
# print(type(info))



# student = {
#     "name":"Debadatta Jena",
#     "sub":{
#         "mat":80,
#         "phy":90,
#         "chm":78
#     }
# }
# print(student)

# print(student.keys())
# print(list(student.values())) #Using type casting
# print(student.items())
# print(student.get("sub"))

# collection = {1,2,2,3,4,5,6}

# print(collection)
# print(type(collection))


# num = set()

# num.add(1)
# num.add(2)
# num.add(2)
# num.add(3)
# num.add(4)
# num.add(5)
# num.add(6)
# num.add(7)
# num.add(3)

# num.remove(5)

# num.clear()



# print(num)


# name = {"Litu","java","python","c++","HTML","CSS"}

# print(name.pop())
# print(name.pop())
# print(name.pop())
# print(name.pop())


# set1 = {1,2,3,4,5}
# set2 = {2,4,6,8,7}

# print(set1.union(set2))

# print(set1.intersection(set2))

# dict = {
#   "cat": "a small animal",
#   "table":["a piece furniture"," List of facts and figure"]
#  }
# print(dict)



# subject = {
#     "python","java","C++","python","javascript","java","python","java","C++","c"
# }

# print(subject)

# marks ={}
# x = int(input("Enter phy :"))
# marks.update({"phy:":x})

# Y = int(input("Enter mat :"))
# marks.update({"mat:":Y})

# Z = int(input("Enter chm :"))
# marks.update({"chm:":Z})

# print(marks)


# values={9,"9.0"}
# print(values)


# count = 1
# while count <=5:
#     print("Litu is devloper")
#     count= count+1

# count = int(input("Enter Numbe :"))
# while count <=40:
#     print(count)
#     count = count+1

# count = 69
# while count >=1:
#     print(count)
#     count = count-1


# num = 1
# while num <=100:
#     print(num)
#     num +=1

# num1 = 100
# while num1 >=1 :
#     print(num1)
#     num1 -=1


# multi = 1
# while multi <=10:
#     print(multi * 3)
#     multi +=1



# n = int(input("Enter number :"))
# num = 1
# while num <= 10:
#     print(n * num)
#     num = num+1

# nums = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx +=1

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = 36
# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("Found of Index",i)   
#     i +=1 


# num = 1
# while num <=10:
#     print(num)
#     if(num == 6):
#         break
#     num+=1

# list = [1,2,3,4,5,6,7,8,9]

# for num in list:
#     print(num)


# list = [1,2,3,4,5,6,7,8,9]

# for num in list:
#     if(num == 6):
#         print("I found ", num)
#         break
#     print(num)
# else:
#     print("END")

# nums = [1,4,9,16,25,36,49,64,81,100]
# for val in nums:
#     print(val)






# nums = (1,4,9,16,25,36,49,64,81,100,64,25,36,49,64 )
# x = 64

# idx = 0
# for val in nums:
#     if(val == x):
#         print("number found at index" ,idx)
#         # break
#     idx += 1


    

# for val in range(5): #range (stop)
#     print(val)

# for val in range(4,10): #range (star , stop)
#     print(val)

# for val in range(2 ,50,2): #range (start , stop ,step)
#     print(val)


# num = range(11)
# for val in num:
#     print(val)

# for val in range(1 ,101):
#     print(val)

# for val in range(100 ,0,-1):
#     print(val)

# n = int(input("Enter numbar"))
# for val in range(1,11):
#     print (val* n)


# for val in range(10):
#     pass
# print("some useful work")

# n = 100

# sum = 0
# for val in range(1,n+1):
#     sum += val
# print("Total sum = ",sum)


# n = 79
# sum = 0
# val = 1
# while val <=n:
#     sum += val
#     val += 1
# print("Total sum = ", sum)

# n = 5

# fact = 1
# for val in range(1,n+1):
#     fact *= val
# print("Total fact = ",fact)


# function

# def cal_sum(a,b):
#     sum = a+b
#     print(sum)
#     return sum
# cal_sum(3,5)

# def cla_sum(a, b):
#     return a + b

# cla_sum(3, 4)

# function Defination




# def cla_sum(a, b): # a,b is Parameters
#     return a + b

# print(cla_sum(3, 4)) #function Call ,(3,4) is arguments

# def cal_ave(a,b,c):
#     sum = a + b + c
#     return(sum/3)
# print(cal_ave(98,97,95))

# def cal_product(x = 1, y = 1 ):
#     return x * y
# print(cal_product())

# cities = ["Delhi","gurgaon","noida","pune","Odisha","Mumbai","Chennai"]

# def citi_len(cities):
#     return(len(cities))
# print(citi_len(cities))
# print(citi_len(cities="pune"))

# cities = ["Delhi","gurgaon","noida","pune","Odisha","Mumbai","Chennai"]

# def citi_val(list):
#     for item in list:
#         print(item , end=" ")

# citi_val(cities)        

# n = 5
# fact = 1
# for num in range(1, n+1):
#     fact *= num
#     print(fact)



# def cal_fact(n): 
#     fact = 1
#     for num in range(1, n+1):
#         fact *= num
#     print(fact)

# cal_fact(7)    


# val = int(input("Enter USD value :" ))

# def convert(usd_val):
#     inr_val = usd_val * 83
#     print(usd_val,"USD = ",inr_val,"INR")

# convert(val)





# HM WORK

# val = int(input("Enter Numbe :"))

# def ev_odd(n):
#     if(n % 2 == 0):
#         print( n ,"Is a EVEN Numbe")
#     else:
#         print(n ," Is a ODD Number") 

# ev_odd(val)


# recursion function

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)      
# show(9)






# def show_num(n):
#     for item in range(n):
#         print(item)
# show_num(5) 




# val = int(input("Enter numbe :"))

# def show_num(n):
#     for item in range(n):
#         print(item)
# show_num(val)        


# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n
    
# print(fact(7))


# def cal_natu(n):
#     if(n == 0):
#         return 0
#     return cal_natu(n-1) + n
# print(cal_natu(9) )   



# f = open("demo.txt","r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# f = open("demo.txt","r")
# data = f.read(71)
# data = f.readline()
# print(data)
# f.close()


# f = open("demo.txt" ,"w")
# f.write("I want to learn javascript today")

# f.close()


# f = open("demo.txt","a")
# f.write("\nI am java and javascript Devloper.")
# f.close()

# f = open("demo_new.txt","w")
# f.close()

# f = open("demo_new.txt","a")
# f.close()

# f = open("demo_new.txt","r+")
# f.write("That")
# f.close()

# f = open("demo_new.txt","w+")
# f.write("not")
# f.close()

# f = open("demo_new.txt","a+")
# f.write(" is")
# f.close()
 
# with open("demo_new.txt","r") as f:
#     data=f.read()
# print(data)



# import os
# os.remove("demo_new.txt")


# with open("practice.txt","w") as f:
#     f.write("Hii everyone\nwe are learning file i/o \nUsing java\nI like pogramming in java")


# with open("practice.txt","r") as f:
#     data = f.read()
#     new_data = data.replace("java","python")
#     print(new_data)
# with open("practice.txt","w") as f:
#     f.write(new_data)


# with open("practice.txt","r") as f:
#     data = f.read()
#     if(data.find("learning") != -1):
#         print("Foud")
#     else:
#         print("Not Found")

# def check_word():
#     with open("practice.txt","r") as f:
#         data = f.read()
#     if("learning" in data):
#         print("Foud")
#     else:
#         print("Not Found")
        
# check_word()









# class Student:
#     name = "Kiran"


# s1 = Student()
# print(s1.name)    

# class Car:
#     color = "blue"
#     brand = "Hond"
# car1 = Car()
# print("Car Colour :",car1.color)
# print("Brand name :",car1.brand)








# class Student:
 
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("Adding new student in Database..")

# s1 = Student("Kiran" ,79)
# print ("My name is ",s1.name,"and my mark is",s1.marks) #kiran

# s2 = Student("Sipa",98)
# print("My name is ",s2.name,"and my mark is",s2.marks)









# class Student:
#     def __init__(self,name,mark):
#         self.name = name
#         self.mark = mark

#     def welcome(self):
#         print("Welcome student",self.name)


# s1 = Student("Kiran",66)
# s1.welcome()






# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks


#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             print("Hii",self.name,"Your avg score is:",sum/3)


# s1 = Student("Debadatta Jena", [99,98,97])
# s1.get_avg()





# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         total = 0
#         for val in self.marks:
#             total += val
#         avg = total / len(self.marks)
#         print("Hi", self.name, "Your avg score is:", avg)


# s1 = Student("Debadatta Jena", [97, 99, 98])
# s1.get_avg()


# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#              self.clutch = True
#              self.acc = True
#              print("Car started..") 

# car1 = Car()
# car1.start()           












#Bank issue solved


# class Account:
#         def __init__(self,bal,acc):
#             self.balance = bal
#             self.account_no = acc


#       # debit method
#         def debit(self,amount):
#               self.balance -= amount
#               print("RS.",amount,"Was Debited")
#               print("Totla balance = ",self.get_balance())

#       # credit mthod 
#         def credit(self,amount):
#             self.balance += amount
#             print("RS.",amount,"Was Credited")
#             print("Totla balance = ",self.get_balance())

#        #Finall balance
#         def get_balance(self):
#               return self.balance     

# acc1 = Account(10000, 1234567)
# acc1.debit(1000)
# acc1.credit(5000)


# class Student:
#     def __init__(self,name):
#         self.name = name 

# s1 = Student("debadatta")
# print(s1.name)
# del s1.name
# print(s1)






# class Account:
#     def __init__(self,acc_no,acc_passwd):
#         self.acc_no = acc_no
#         self.__acc_passwd = acc_passwd


# acc1  =  Account("123456","abcdef")


# print(acc1.acc_no)
# print(acc1.__acc_passwd)




# class person:
#     __name = "javascript"

# p1 = person()


# print(p1.__name)








# class person:
#     __name = "javascript"

#     def __hello(self):
#         print("Hello persion!")

#     def   welcome(self):
#         self.__hello() 

# p1 = person()
# print(p1.welcome())





# class Car:

#     colour = "blakc"
#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car Stopped..")


# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")   


# print (car1.name)
# print(car2.start())
        




# class Car:

#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car Stopped..")


# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand = brand


# class Fortuner(ToyotaCar):
#     def __init__(self, type):
#         self.type = type


# car1 = Fortuner("disel")
# car1.start()


# class A:
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A, B):
#     varC = "Welcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varC)   
# print(c1.varC) 




# class Car:

#     def __init__(self,type):
#         self.type = type
        

#     @staticmethod
#     def start():
#         print("Car started..")

#     @staticmethod
#     def stop():
#         print("Car Stopped..")


# class ToyotaCar(Car):
#     def __init__(self,name,type):
#         self.name = name
#         super().__init__(type)
#         super().start()

# car1 = ToyotaCar("furtuner","electric")
# print(car1.type)



# class Person:
#     name  = "Javascript"

#     def cahngeName(self,name):
#         self.name = name


# p1 = Person()
# p1.cahngeName("Damayanti Jena")
# print(p1.name)
# print(Person.name)


# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chme = chem
#         self.math = math
       
#     @property
#     def percentage(self):
#         return str((self.phy + self.chme + self.math) / 3) + "%"

# stu1 = Student(78,36,54)
# print(stu1.percentage)

# stu1.phy = 58
# print(stu1.percentage)







# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNumbr(self):
#         print(self.real,"i +" ,self.img,"j")

#     def __add__(self,num2):
#         newReal = self.real + num2.real
#         newImg = self.img  + num2.img
#         return Complex(newReal,newImg)
    
    
#     def __sub__(self,num2):
#         newReal = self.real - num2.real
#         newImg = self.img  - num2.img
#         return Complex(newReal,newImg)
    

#     def __mul__(self,num2):
#         newReal = self.real * num2.real
#         newImg = self.img  * num2.img
#         return Complex(newReal,newImg)
    

#     def __truediv__(self,num2):
#         newReal = self.real / num2.real
#         newImg = self.img  / num2.img
#         return Complex(newReal,newImg)
    
#     def __mod__(self,num2):
#         newReal = self.real % num2.real
#         newImg = self.img  % num2.img
#         return Complex(newReal,newImg)

# num1 = Complex(1, 5)
# num1.showNumbr()  


# num2 = Complex(9, 6)
# num2.showNumbr()  


# num3 = num1 + num2
# num3.showNumbr()

# num3 = num1 - num2
# num3.showNumbr()

# num3 = num1 * num2
# num3.showNumbr()

# num3 = num1 / num2
# num3.showNumbr()

# num3 = num1 % num2
# num3.showNumbr()



# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#     def talk(self):
#         print('Hello i am :',self.name)
#         print('my Roll Numbe',self.rollno)
#         print('My Marks :',self.marks)
# s=Student('litu',24,90)
# s1 = Student('jiban',23,68)
# s.talk()
# s1.talk()
# print('student name:',s.name)
# print('student rollno:',s.rollno)
# print('student marks:',s.marks)



# class Test:
#     def __init__(self):
#         print(id(self))
# # t = Test()
# # print(id(t))
# print(id(Test()))


# class Test:
#     def __init__(self):
#         print('constructor')

#     def m1(self,x):
#         print("method")

# t = Test()    
# t.m1(5)    






# class Student:
#     def __init__(self,name,rollno,marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = marks
#     def talk(self):
#         print('Hello i am :',self.name)
#         print('my Roll Numbe',self.rollno)
#         print('My Marks :',self.marks)
# s=Student('litu',24,90)
# s1 = Student('jiban',23,68)
# s.talk()
# s1.talk()


# x=y=z = 10
# print(x,y,z)


# for ch in "hello":
#     print(ch)


# for num in range(0,6):
#     print (num)


# for ch in [10,20,30,40,50]:
#     print(ch)


# for name in "Debadatta jena":
#     print(name)

# for i in range(5):
#     print("Debadatta jena")

# for even in range(1,20):
#     if even % 2 == 0:
#         print(even)    

# lst = [10,20,30,40,50]       
# cunt = 0
# for total in lst:
#   cunt+= total
#   print(F'Total : {cunt}')

# var = input("Enter a string: ")
# rev = ""

# for a in var:
#     rev = a + rev

# print(rev)



# var = "automation"
# num = 0

# for ch in var:
#     if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
#         num += 1

# print(num)



# num = int(input("Enter a number: "))
# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial is :", fact)
   




# l = [4, 50, 20, 70, 7, 10]

# max = l[0]   

# for num in l:
#     if num > max:
#         max = num

# print("Print maximu number",max)        

# num = 0

# while num < 5:
#     num =  num + 1
#     print(num)

# count = 0
# while count < 5:
#     count = count + 1
#     print("Debadatta jena")


# i = 0
# total = 0

# while i <= 5:
#     total = total + i
#     i = i + 1

# print(total)    
    

# a = 10
# while a >= 0:
#     print(a)
#     a = a-1

# a = 1
# num =  int(input("Enter the number :"))
# while a <= 10:
#     print(a * num)
    # print(f"{num} * {a} = {a * num}")
    # a = a + 1    


