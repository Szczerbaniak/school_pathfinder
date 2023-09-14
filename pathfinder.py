import random

maze_size = 8 - 1
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

start_num = 2
finish_num = 3
junctions = []

start_position = []
destination = []

for count, line in enumerate(maze):
    try:
        start = line.index(start_num)
        start_position = [count, start]
        break
    except:
        print("no start point in ")
print(start_position)

for count, line in enumerate(maze):
    try:
        start = line.index(finish_num)
        destination = [count, start]
        break
    except:
        print("no start point in ")


position = start_position

def isMoveInMatrix(position, yMove, xMove):
    # print(position[0] + yMove)
    if not (0 <= position[0] + yMove and position[0] + yMove <= 7):
        return False
    if not(0 <= position[1] + xMove and position[1] + xMove <= 7):
        return False
    return True

def isLegalPosition(position, yMove, xMove):

    if (isMoveInMatrix(position, yMove, xMove)):
        return maze[position[0] + yMove][position[1] + xMove] != 1
    return False


def possibleNextPositions(position):

    possible_next_position = []
    # up
    if (isLegalPosition(position, -1, 0)):
        possible_next_position.append([position[0] -1, position[1]])
    # down
    if (isLegalPosition(position, 1, 0)):
        possible_next_position.append([position[0] + 1, position[1]])

    # left
    if (isLegalPosition(position, 0, -1)):
        possible_next_position.append([position[0], position[1] - 1])

    #right
    if (isLegalPosition(position, 0, 1)):
        possible_next_position.append([position[0], position[1] + 1])
    
    return possible_next_position

def wasAlreadyMove(move):
    if (traveled_maze[move[0]][move[1]] == "x"):
        return True
    return False



def createMove(current_position):
    possible_positions = possibleNextPositions(current_position)

    for possible_positon in possible_positions:
        if (wasAlreadyMove(possible_positon)):
            possible_positions.remove(possible_positon)

    num_of_new_moves = len(possible_positions)

    if (num_of_new_moves == 0):
        possible_positions = junctions[-1]
        number_of_way = 0
    else:
        number_of_way = random.randrange(num_of_new_moves)



    if (num_of_new_moves > 1):
        junctions.append([position])
        print("added junction")
    else:
        try:
            junctions.remove([position])
            print("removed junction")
        except:
            print("not junction")

    return possible_positions[number_of_way]


# print(possibleNextPositions(start_position))

while True:
    move = createMove(position)
    print("m", move)
    traveled_maze[move[0]][move[1]] = "x"

    position = move

    # position = move(position)
    print(position)

    if (position == destination):
        print ("koniec")
        break
# position = [7, 1]
# print(maze[position[0]][position[1]])
print(junctions)


# position = [2, 4]
# print(isPositionInMatrix(start_position))