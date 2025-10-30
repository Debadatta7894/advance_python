# Print numbers from 1 to 10 using a while loop.

# a = 0

# while a <=10:
#     print(a)
#     a+=1

# Print even numbers between 1 and 20.

# num = int(input("Enter number: "))
# a = 0
# while a <= num:
#     print("Print Even number",a)
#     a+=2

# Print odd numbers between 1 and 15.

# num = int(input("Enter number: "))
# a = 1
# while a <= num:
#     print("Print odd number",a)
#     a+=2

# Print numbers in reverse from 10 to 1.

# i = 10
# while i >= 1:
#     print(i)
#     i-=1


# Print the first 10 natural numbers and their squares.

# a = 1
# while a<=10:
#     print(a * a)
#     a+=1

# Print the multiplication table of 5 using a while loop.

# a = 1
# num = int(input("Enter multiplay number : "))
# while a <= 10:
#     print(f"{num} x {a} = {num*a}")
#     a =a + 1

    


# Print your name 5 times using a while loop.

# a = 0
# while a <= 5:
#     print("Debadatta Jena")
#     a+=1

# Find the sum of first 10 natural numbers.

# a = 0
# sum = 1
# while a <= 10:
#     sum = sum+a
#     a+=1
# print("Total Sum:",sum)

# Find the sum of all even numbers between 1 and 20.

# a = 2
# sum = 0
# while a <= 20:
#     sum = sum + a
#     a+=2
# print(sum)

# Print all numbers divisible by 3 between 1 and 30.

# a = 1

# while a <= 30:
#     print (a)
#     a+=2

# Take a number from the user and print its digits separately.


# num = input("Enter a number: ")

# for digit in num:
#     print(digit)

# Find the sum of digits of a number using a while loop.

# Count how many digits are in a given number.

# Reverse a given number using a while loop.

# Print Fibonacci series up to 10 terms.

# Print factorial of a given number using while loop.

# num =  int(input("Enter a number: "))

# i = 0
# total = 0

# while i <= num:
#     total = total + i
#     i = i + 1

# print(total)    
    

# Print all multiples of 7 between 1 and 100.

# num = 7

# while num <= 100:
#     print(num)
#     num += 7

# Print numbers from 1 to 50 but skip numbers divisible by 5.

# a =  1

# while a <= 50:
#     if(a % 5 == 0):
#         a+=1
#     print (a)
#     a+=1    


# for i in range(1,50):
#     if i % 5 == 0:
#         continue
#     print(i)

# Calculate the product of digits of a number.

# num = int(input("Enter a number: "))
# product = 1
# temp = num

# while temp > 0:
#     digit = temp % 10
#     product *= digit
#     temp //= 10

# print("Product of digits of", num, "is:", product)




# num = int(input("Enter a number: "))
# product = 1

# for digit in str(num):
#     product *= int(digit)

# print("Product is:", product)

# Check if a number is a palindrome

# num =  int(input("Enter a number :"))

# x = num

# rev = 0
 
# while num > 0:
#     rev *= 10 + (num % 10)
#     num = num // 10 


# if x == rev:
#     print(f"{x} is a palindrome.")
# else:
#     print(f"{x} is not a palindrome.")
# Find the largest digit in a given number.

# num = int(input("Enter a number: "))

# largest = 0

# while num != 0:
#     digit = num % 10        
#     if digit > largest:     
#         largest = digit
#     num = num // 10         

# print("The largest digit is:", largest)

# Count how many even and odd digits are in a number.

# num = int(input("Enter a number: "))


# num = abs(num)

# even_count = 0
# odd_count = 0

# while num > 0:
#     digit = num % 10
#     if digit % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
#     num = num // 10

# print(f"Even digits: {num}= {even_count}")
# print(f"Odd digits: {num}= {odd_count}")





# x = 0

# while not(1 <= x <= 100):
#     x = int(input("Enter a number between 1 to 100 :"))
#     if 1 <= x <= 100:
#         print("Valid Number :",x)
#     else:
#         print("Invalid number :",x)



for i in range(5):
    x = int(input("Please enter a number 1 to 100 : "))
    if 1<=x<=100:
        print("Valid number :",x)
        break
    else:
        print("Invalid number . Try again.")


# Reverse function in using for loop
# str = "litu"
# rev = ""

# for a in str:
#     rev = a + rev

# print(rev)


# a =  1

# while a <= 11:
#     if(a % 2 == 0):
#         a+=1
#         continue
#     print (a)
#     a+=1  

# a =  1

# while a <= 11:
#     if(a % 2 == 0):
#         a+=1
#         break
#     print (a)
#     a+=1      


# Print numbers from 1 to 10, but stop when number becomes 6.
# for i in range(1, 10):
#     if i == 6:
#         break
#     print(i)
# Print numbers from 1 to 10, but skip number 5.

# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)
# Print all numbers from 1 to 10 except multiples of 3.

# for i in range(1, 11):
#     if i % 3 == 0:
#         continue
#     print(i)
# Print numbers 1–10, but stop if number is divisible by 7.
# for i in range(1, 11):
#     if i % 7 == 0:
#         break
#     print(i)
# Write a program that prints “Found” when number 9 is reached, then stops using break.    
# for i in range(1, 11):
#     if i  == 9:
#        print("Found")
#        break
#     print(i)