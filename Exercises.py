# 1. Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 4
# Number of odd numbers : 5

def even_odd_count(tuple):
    count_odd = 0
    count_even = 0
    for x in tuple:
        if not x % 2:
    	     count_even+=1
        else:
    	     count_odd+=1
    print("Number of even numbers :",count_even)
    print("Number of odd numbers :",count_odd)

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) # Declaring the tuple
even_odd_count(numbers)








# 2. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"

def string_reverse(str1):

    rstr1 = ''
    index = len(str1)
    while index > 0:
        rstr1 += str1[ index - 1 ]
        index = index - 1
    return rstr1
print(string_reverse('1234abcd'))