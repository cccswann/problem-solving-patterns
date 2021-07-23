## PROBLEM: ##
# Given an array of sorted numbers and a target
# sum, find a pair in the array whose sum is equal
# to the given target.

## Brute force solution:
# Could be to iterate through array taking one at a time and
# search for second number thru binary search.
# Time complexity would be O(N * logN) 

###################################################################

## Two Pointers approach:
# One pointer at beginning of array and one at the end;
# Every step we see the two pointers add up to the target sum. 
# we either find our pair, or increment the left pointer, or decrement the right

def pair_with_targetsum(arr, target_sum):
    left, right = 0, len(arr)-1
    while (left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]
        
        if target_sum > current_sum:
            left += 1  
        else:
            right -= 1
    return [-1, -1]

# Time complexity: O(n) n is the total number of elem in the given array
# Space complexity: O(1) runs in constant space
        
####################################################################################

## Hash Table Approach:
# Time: O(n)
# Space: O(n)

def pair_with_targetsum_hash(arr, target_sum):
    nums = {}
    for i, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum - num], i]
        else:
            nums[arr[i]] = i
    return [-1, -1]

def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum_hash([1, 2, 3, 4, 6], 6))

main()