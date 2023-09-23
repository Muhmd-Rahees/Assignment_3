# Write a Python function to sum all the numbers in a list.

# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# Explanation:
# Summation should like 8+2+3+0+7 = 20

lst = [8,2,3,0,7]

def sum():

    sum_lst = 0

    for i in lst:
        sum_lst+=i
    return sum_lst

res = sum()
print(f"Sum of all numbers in a list = {res}")

