# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

# ﻿Sample String : 'The quick Brow Fox'

# Expected Output :

# No. of Upper case characters : 3

# No. of Lower case Characters : 12



# METHOD - 1
# With parameter and with return statement.
sample_str = "The quick Brow Fox"

def cases(sample_str):

    upper = 0
    lower = 0
    for i in sample_str:
        if i.isupper():
            upper += 1
        if i.islower():
            lower +=1
    return upper,lower 

upper,lower = cases(sample_str)
print(f"No: of upper cases : {upper}")
print(f"No: of lower cases : {lower}")



# METHOD - 2
# without parameter and without return statements.
sample_str = "The quick Brow Fox"

def cases():

    upper = 0
    lower = 0
    for i in sample_str:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
    print(f"No : of upper cases : {upper}")
    print(f"No : of lower cases : {lower}")

cases()



# METHOD - 3
# With parameter and without return statements. 
sample_str = "The quick Brow Fox"

def cases(sample_str):

    upper = 0
    lower = 0
    for i in sample_str:
        if i.isupper():
            upper +=1
        if i.islower():
            lower += 1
    print(f"No : of upper cases : {upper}")
    print(f"No : of lower cases : {lower}")

cases(sample_str)



# METHOD - 4
# Without parameter and with return statements. 
sample_str = "The quick Brow Fox"

def cases():

    upper = 0
    lower = 0
    for i in sample_str:
        if i.isupper():
            upper +=1
        if i.islower():
            lower += 1
    return upper,lower
    
res = cases()
print(f"No : of upper cases : {res[0]}")
print(f"No : of lower cases : {res[1]}")