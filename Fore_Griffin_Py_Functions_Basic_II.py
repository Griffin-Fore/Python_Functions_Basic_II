# 1. Countdown - Create a function that accepts a number as an input.
#   Return a new list that counts down by one, from the number (as the 0th element) 
#   down to 0 (as the last element).

def count_down_from_x(x):
    if x > 0:
        for i in range(x,-1,-1):
            print(i)

# count_down_from_x(5)
# count_down_from_x(17)
# count_down_from_x(-3)

# 2. Print and Return - Create a function that will receive a list with two numbers.
#    Print the first value and return the second.

# def two_number_list(a):
#     print(a[0])
#     return a[1]

# print(two_number_list([1,2]))
# print(two_number_list([3,5]))
# print(two_number_list([4,7]))

# 3. First Plus Length - Create a function that accepts a list
# and returns the sum of the first value in the list plus the list's length.

# def first_plus_length(a):
#     return a[0] + len(a)

a1 = [1,2,3,4,5,6]
a2 = [1,2,3]
a3 = [1]

# print(first_plus_length(a1))
# print(first_plus_length(a2))

# 4. Values Greater than Second - Write a function that accepts a list
# and creates a new list containing only the values from the original list 
# that are greater than its 2nd value. Print how many values this is and then return the new list. 
# If the list has less than 2 elements, have the function return False

# def values_greater_than_second(a):
#     if len(a) < 2:
#         return False
#     anew = []
#     for i in range(2,len(a)+1):
#         anew.append(i)
#     print(len(anew))
#     return anew

# print(values_greater_than_second(a1))
# print(values_greater_than_second(a3))

# 5. This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size,
# and whose values are all the given value.

# def lengthyValue(a,b):
#     newArr = []
#     for i in range (0,a):
#         newArr.append(b)
#     return newArr

# print(lengthyValue(3,4))
# print(lengthyValue(5,7))
# print(lengthyValue(4,6))
# print(lengthyValue(1,2))
