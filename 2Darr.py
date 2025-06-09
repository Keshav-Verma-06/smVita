n = int(input("Enter the number of rows: "))
# m = int(input("Enter the number of columns: "))
# o = int(input("Enter the number of layers: "))

# # Initialize a 2D array (list of lists) with zeros
# array_3d = [[[0 for k in range(o)] for j in range(m)] for i in range(n)]

# # Print the 2D array
# for row in array_3d:
#     print(row)

grid = []

for i in range(n):
    grid.append([int(item) for item in input(f"Enter row {i + 1} values separated by space: ").split()])

# Print the 2D array
for row in grid:
    print(row)


# Calculate the trace of the 2D array
trace = 0
for i in range(n):
    trace += grid[i][i]
print("Trace of the 2D array:", trace)

# calculate transpose of the 2D array

for i in range(n):
    for j in range(n):
        if i < j:
            # Swap elements to transpose the matrix 
            temp = grid[i][j]
            grid[i][j] = grid[j][i]
            grid[j][i] = temp
# Print the transposed 2D array
for row in grid:
    print(row)
