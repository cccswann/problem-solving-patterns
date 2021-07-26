## EXAMPLE PROBLEM ##
# Given an array of n−1 integers in the range from 1 to n, 
# find the one number that is missing from the array.

## Straight forward approach:
# Find sum of all integers from 1 to n (s1)
# Subtract all the numbers in the input array from s1

def find_missing_num(arr):
    n = len(arr) + 1 
    # find sum of all numbers from 1 to n
    s1 = 0 
    for i in range (1, n+1):
        s1 += i
    
    # subtract all numbers in input from sum
    for i in arr:
        s1 -= i
    
    # s1, now, is the missing number
    return s1

def main():
    arr = [1, 5, 2, 6, 4]
    print('Missing number is: ' + str(find_missing_num(arr)))

main()

# Time: O(n)
# Space: O(1)
# Inefficiency/Problem: integer overflow can occur when n is large

#######################################################################

## XOR implementation:

def find_missing_num(arr):
    n = len(arr) + 1
    # x1 represents XOR of all values from 1 to n
    x1 = 1
    for i in range(2, n+1):
        x1 = x1 ^ 1
    
    # x2 represents XOR of all values in arr
    x2 = arr[0]
    for i in range(1, n-1):
        x2 = x2 ^ arr[i]

    # missing number is the xor of x1 and x2
    return x1 ^ x2

def main():
    arr = [1, 5, 2, 6, 4]
    print('Missing number is: ' + str(find_missing_num(arr)))

main()