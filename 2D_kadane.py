import sys

matrix = [
    [3,8,9,1,3],
    [-4,-1,1,7,-6],
    [-2,-3,8,1,-1]
]

def kadaneAlgorithm(givenNums):
    start = 0
    end = 0
    maxSum = -sys.maxsize - 1
    currentSum = 0

    n = len(givenNums)

    while end < n:
        while currentSum < 0:
            currentSum -= givenNums[start]
            start += 1
        
        currentSum += givenNums[end]
        end += 1

        maxSum = max(maxSum, currentSum)

    return maxSum

n = len(matrix)
m = len(matrix[0])
ans = -sys.maxsize - 1

for i in range(m):
    temp = []
    for j in range(n):
        temp.append(matrix[j][i])
    print("Initial temp:", temp)
    ans = max(ans, kadaneAlgorithm(temp))
    print("Current max after first column:", ans)
    for j in range(i+1, m):
        for k in range(n):
            temp[k] += matrix[k][j]

        print("Updated temp:", temp)
        ans = max(ans, kadaneAlgorithm(temp))
        print("Current max after column", j, ":", ans)

    print("-----------------------------------")
print("Largest subarray sum in 2D matrix is:", ans)