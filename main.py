r = int(input())
c = int(input())
matrix = []
for i in range(r):
    row = []
    for j in range(c):
        element = int(input())
        row.append(element)
    matrix.append(row)
diagonal_sum = 0
for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]
print(diagonal_sum)
