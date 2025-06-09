import sys

def largestSubarraySum(givenNums):
    maxSum = -sys.maxsize - 1
    currSum = 0
    start = 0
    end = 0

    n = len(givenNums)
    while end < n:
        while currSum < 0:
            currSum -= givenNums[start]
            start += 1
        
        currSum += givenNums[end]
        end += 1

        maxSum = max(maxSum, currSum)

    return maxSum

# givenNums = [1, 4, -3, 10, -20, 12]
givenNums = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
print("Largest subarray sum is:", largestSubarraySum(givenNums))