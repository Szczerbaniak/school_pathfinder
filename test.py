
maze = [
    [1, 1, 1, 1, 2, 1, 1, 1],#0
    [1, 0, 0, 0, 0, 0, 1, 0],#1
    [1, 0, 1, 1, 1, 1, 1, 1],#2
    [1, 0, 0, 0, 0, 1, 0, 1],#3
    [1, 0, 1, 0, 1, 0, 0, 1],#4
    [1, 0, 0, 1, 0, 0, 1, 1],#5
    [1, 1, 0, 0, 0, 1, 1, 1],#6
    [1, 3, 0, 1, 1, 1, 1, 1] #7
    ]

def findPlaceInMatrix(matrix, data):
    for row_num, row in enumerate(matrix):
        if (data in row):
            column_num = row.index(data)
            return [row_num, column_num]

print(findPlaceInMatrix(maze, 2))