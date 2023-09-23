# Write a Python program to reverse a string.

# ﻿Sample String : "1234abcd"
# Expected Output : "dcba4321"


# Method - 1

# Without Parameter and with return statement.
str1 = "1234abcd"

def reverse():

    reverse_str1 = str1[::-1]
    return reverse_str1
res = reverse()
print(F"The reverse of the sample string '1234abcd' in METHOD 1 is {res}")


# NEXT>>>


# Method - 2

# With Parameter and with return statement.
str1 = "1234abcd"

def reverse (string):

    reverse_string = string[::-1]
    return reverse_string

res = reverse(str1)
print(f"The reverse of the sample string '1234abcd' in METHOD 2 is {res} ")
