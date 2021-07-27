# Any problem that asks to find the top/smallest/frequent
# 'K' elements amond a given set falls under this pattern.

## EXAMPLE PROBLEM ##
# Given an unsorted array of numbers, find the 'K' largest
# numbers in it.

## Brute force approach:
# Sort the array and return the largest K numbers
# Time: O(n logn) 

######################################################

## Heap approach:

from heapq import *

def find_k_largest_nums(nums, k):
    minHeap = []
    # put first 'K' numbers in the min heap
    for i in range(k):
        heappush(minHeap, nums[i])
    
    # go thru the remaining nums of the arr, if the number from the array
    # is bigger than the top(smallest) number of the min-heap, remove the top num from 
    # heap and add the number from array
    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])
    
    # the heap has the top 'K' numbers, return them in a list
    return list(minHeap)

def main():

    print("Here are the top K numbers: " +
        str(find_k_largest_nums([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
        str(find_k_largest_nums([5, 12, 11, -1, 12], 3)))

main()

# Time: O(N logK)
# Space: O(K) top K numbers in the heap