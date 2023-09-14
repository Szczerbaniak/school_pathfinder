import random

maze = [
        [1, 1, 1, 1, 2, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 1],
        [1, 3, 0, 1, 1, 1, 1, 1]
    ]

traveled_maze = maze

def findPlaceInMatrix(matrix, data):
    for row_num, row in enumerate(matrix):
        if (data in row):
            column_num = row.index(data)
            return [row_num, column_num]

start_num = 2
start_position = findPlaceInMatrix(maze, start_num)

destination_num = 3
destination = findPlaceInMatrix(maze, destination_num)

junctions = []

position = start_position

traveled_maze[position[0]][position[1]] = "x"

route = []


def isMoveInMatrix(position, yMove, xMove):
    if not (0 <= position[0] + yMove and position[0] + yMove <= 7):
        return False
    if not (0 <= position[1] + xMove and position[1] + xMove <= 7):
        return False
    return True

def isLegalPosition(position, yMove, xMove):
    if (isMoveInMatrix(position, yMove, xMove)):
        return maze[position[0] + yMove][position[1] + xMove] != 1
    return False


def possibleNextPositions(new_position):
    possible_next_position = []

    # up
    if (isLegalPosition(new_position, -1, 0) and traveled_maze[new_position[0] - 1][new_position[1]] != "x"):
        possible_next_position.append([new_position[0] -1, new_position[1]])

    # down
    if (isLegalPosition(new_position, 1, 0) and traveled_maze[new_position[0] + 1][new_position[1]] != "x"):
        possible_next_position.append([new_position[0] + 1, new_position[1]])

    # left
    if (isLegalPosition(new_position, 0, -1) and traveled_maze[new_position[0]][new_position[1] - 1] != "x"):
        possible_next_position.append([new_position[0], new_position[1] - 1])

    #right
    if (isLegalPosition(new_position, 0, 1) and  traveled_maze[new_position[0]][new_position[1] + 1] != "x"):
        possible_next_position.append([new_position[0], new_position[1] + 1])
    
    return possible_next_position

def createMove(current_position):
    possible_positions = possibleNextPositions(current_position)

    num_of_new_moves = len(possible_positions)

    if (num_of_new_moves == 0):
        possible_positions.append(junctions[-1])
        number_of_route = 0
    else:
        number_of_route = random.randrange(num_of_new_moves)

    if (num_of_new_moves > 1 and (position not in junctions)):
        junctions.append(position)
    else:
        if (position in junctions):
            junctions.remove(position)

    return possible_positions[number_of_route]

while 1:
    move = createMove(position)
    traveled_maze[move[0]][move[1]] = "x"

    position = move

    route.append(move)

    if (position == destination):
        print ("went through the maze, final route: ", route)
        break