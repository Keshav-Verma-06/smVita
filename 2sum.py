def solve(givenNums , target):
    temp = givenNums.copy()
    givenNums.sort()
    start = 0
    end = len(givenNums) - 1

    while start < end:
        currentSum = givenNums[start] + givenNums[end]
        if currentSum == target:
            ans = []
            for i in range(len(temp)):
                if temp[i] == givenNums[start] or temp[i] == givenNums[end]:
                    ans.append(i)
            return ans
        if currentSum > target:
            end -= 1
        else:
            start += 1
    return -1

givenNums = [2,1,10,5,7]
target = 12
print(solve(givenNums, target))