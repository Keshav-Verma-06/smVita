import sys

def getNum(char):
    if char == '0':
        return 1
    return -1

def flipBits(givenStr):
    ans = 0
    for i in givenStr:
        if i == '1':
            ans += 1

    maxSum = -sys.maxsize - 1
    currSum = 0
    start = 0
    end = 0

    n = len(givenStr)
    while end < n:
        while currSum < 0:
            currSum -= getNum(givenStr[start])
            start += 1

        currSum += getNum(givenStr[end])
        end += 1

        maxSum = max(maxSum, currSum)

    return ans + maxSum

givenStr = "0001000"
print("Largest subarray sum is:", flipBits(givenStr))