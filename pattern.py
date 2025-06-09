# n = int(input("Enter the number of rows: "))
# m = int(input("Enter the number of columns: "))

# for currRow in range(n):
#     for currNum in range(m):
#         print(currNum + 1, end=" ")
#     print()  # Move to the next line after each row

# n = int(input())

# # for currRow in range(n):
# #     for currNum in range(n):
# #         if currNum <= currRow:
# #             print(currNum + 1, end=" ")
# #         else:
# #             print(" ", end=" ")
# #     print()  # Move to the next line after each row

# for currRow in range(n):
#     for currNum in range(n):
#         if currNum <= currRow:
#             print(currNum + 1, end=" ")
#         else:
#             break
#     print()  # Move to the next line after each row

n = int(input("Enter the number of rows of triangle: "))

for currRow in range(n):
    for currNum in range(n):
        if currNum < n - (currRow + 1):
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()  # Move to the next line after each row