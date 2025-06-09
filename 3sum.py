def solve(givenNums , target):
    temp = givenNums.copy()
    givenNums.sort()
    
    for k in range(len(givenNums)):
        tempTarget = target
        tempTarget -= givenNums[k]

        start = k + 1
        end = len(givenNums) - 1

        while start < end:
            currentSum = givenNums[start] + givenNums[end]

            if currentSum == tempTarget:
                ans = []

                for i in range(len(temp)):
                    if temp[i] == givenNums[start] or temp[i] == givenNums[end] or temp[i] == givenNums[k]:
                        ans.append(i)

                return ans
            
            if currentSum > tempTarget:
                end -= 1
            else:
                start += 1
    return -1

givenNums = [2,1,10,5,7]
target = 13
print(solve(givenNums, target))