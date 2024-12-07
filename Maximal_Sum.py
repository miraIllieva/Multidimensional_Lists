rows, cols = [int(num) for num in input().split()]

# Read the matrix
matrix = [[int(num) for num in input().split()] for row in range(rows)]

result = -181
max_col = 0
max_row = 0

# Find the sum of the 3x3 sub-matrix with the maximum sum
for row in range(rows - 2):
    for col in range(cols - 2):
        sum = 0
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                sum += matrix[i][j]
        if sum > result:
            result = sum
            max_col = col
            max_row = row

# Print the result and the corresponding 3x3 sub-matrix
print(f"Sum = {result}")
for row in range(max_row, max_row + 3):
    for col in range(max_col, max_col + 3):
        print(matrix[row][col], end=' ')
    print()  # to move to the next line after printing a row
