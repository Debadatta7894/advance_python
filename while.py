# s = "india"

# for i in s:
#     if s.count(i) != 2:
#         print(i," is first letter")
#         break






# Using while loop print numbers from 10 to 15.
# 10,11,12,13,14,15
# a = 10

# while a < 16:
#     print(a,end = " ")
#     a+=1

# print cubes af numbers from 1 to 5

# a = 1

# while a <= 5:
#     print(a ** 3, end = " ")

#     a+=1  

# print Odd numbers from 1 to 10.

# a = 1
# while a <= 10:
#     if a % 2 != 0:
#         print(a,end = " ")
#     a+=1

# write a program to calculate the product of numbers from 1 to 5
# prod = 1
# num = 1

# while num <= 5:
#     prod *= num
#     num+= 1 
# print(prod)   


# write a pogram to reverse each word in the sentence "Hello world" using while loop

# sentense = "Hello World"
# word = sentense.split()

# for words in word:
#     i = len(words) - 1
#     while i >= 0:
#         print(words[i], end= " ")
#         i-=1   
#     print(end=" ")     


# write a program to count the number of consonants in the word "leaning"


# word = input("Enter a word : ")
# vowels = "aeiou"
# count = 0
# index = 0

# while index < len(word):
#     if word[index].lower() not in vowels and word[index].isalpha():
#         count+=1
#     index +=1    
# print("Number of consonants",count)



# Write a pogram to print the first 5 multiples of 3

# num = 1

# while num <= 5:
#     print(num * 3 ,end = " ")
#     num+=1

# Write a program to calculate 3 to the power of 4.

# base = 3
# exponent = 4
# while base < 4:
#     print(base ** exponent)
#     base +=1

# write a program to check if a given uumber such as 16 is perfect square


# num  = int(input("Enter a number: "))
# a = 1
# is_perfect_square = False

# while a * a <= num:
#     if a * a == num:
#         is_perfect_square = True
#         break
#     a += 1

# if is_perfect_square:
#     print(num, "is a perfect square")
# else:
#     print(num, "is not a perfect square")


# Write a program to count occurrences of character "s" in the string "success"

# s1 = "success"
# s2 = s1.count("s")
# print(s2)

# s1 = input("Enter a string: ")
# ch = input("Enter a characters: ")
# count = 0
# index = 0
# while index < len(s1):
#     if s1[index] == ch:
#         count += 1
#     index += 1    
# print ("Number of occurrences of", ch, ":", count) 





