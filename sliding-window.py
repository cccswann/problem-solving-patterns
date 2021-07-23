## PROBLEM: ##
## Given an array, find the average of all contiguous 
## subarrays of size 'K' in it.

## Brute Force Approach:
# Calculate the sum of every K-element contiguous
# subarray of the given and divide the sum by K to
# find the average

def find_averages_of_subarrays(arr, K):
    result=[]
    for i in range(len(arr)-K+1):
        # find sum of next 'K' elements
        _sum = 0.0
        for j in range(i, i+K):
            _sum += arr[j]
        #calculate average
        result.append(_sum/K) 
    return result

def main():
    result = find_averages_of_subarrays([1,3,2,6,-1,4,1,8,2], 5)
    print("Averages of subarrays of size K: " + str(result))

main()

# Time complexity: O(N * K) where N is the number of elements of the array
# Inefficiency: For any two consecutive subarrays, the overlapping part will
# be evaluated twice.

##################################################################################

## Sliding Window Approach
# Each contiguous subarray is a sliding window of '5' elements
# Slide the window by one element when we move on to the next
# subarray. To reuse the sum from the prev, subtract the elem 
# going out of the window and add the elem now being included.

def find_averages_of_subarrays(arr, K):
    result = []
    windowSum, windowStart = 0.0, 0 
    for windowEnd in range(len(arr)):
        windowSum += arr[windowEnd] # add the next element
        # slide the window, we don't need to slide if we've not hit the
        # required window size of 'k'
        if windowEnd >= K -1:
            result.append(windowSum / K) # calculate the average
            windowSum -= arr[windowStart] # subtract the element going out
            windowStart += 1 # slide the window ahead
    return result

def main():
    result = find_averages_of_subarrays([1,3,2,6,-1,4,1,8,2], 5)
    print("Averages of subarrays of size K: " + str(result))

main()

# Time complexity: O(N) 
