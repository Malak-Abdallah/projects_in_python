import re

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
sen = ""

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

columns = list(zip(*matrix))
for i in range(m):
    for j in range(n):
        x = (re.findall('[a-zA-Z0-9]', columns[i][j]))
        if len(x) == 0:
            sen = sen + ' '
        else:
            sen = sen + x[0]
        x.clear()

print(sen)
