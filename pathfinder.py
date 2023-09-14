import random

maze_size = 8 - 1
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
traveled_maze[position[0]][position[1]] = "x"


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

# def wasAlreadyMove(move):
#     if (traveled_maze[move[0]][move[1]] == "x"):
#         return True
#     return False



def createMove(current_position):
    possible_positions = possibleNextPositions(current_position)

    # for possible_position in possible_positions:
    #     if (wasAlreadyMove(possible_position)):
    #         possible_positions.remove(possible_position)
    #         print("rem", possible_position)
    #         # for i in traveled_maze:
    #         #     print('\t'.join(map(str, i)))
            

    num_of_new_moves = len(possible_positions)
    # print("num of moves", num_of_new_moves)

    # print("moves", num_of_new_moves, possible_positions)

    if (num_of_new_moves == 0):
        # print("j", junctions[-1])
        possible_positions.append(junctions[-1])
        number_of_way = 0
        
    else:
        number_of_way = random.randrange(num_of_new_moves)

    # print("p", possible_positions, num_of_new_moves)

    if (num_of_new_moves > 1 and (position not in junctions)):
        junctions.append(position)
        # print(junctions, position in junctions)
        print("added junction", position)
        # print("p", position)
    else:
        try:
            junctions.remove(position)
            print("removed junction", position)
            # for i in traveled_maze:
            #     print('\t'.join(map(str, i)))
        except:
            # print("not junction")
            pass

    return possible_positions[number_of_way]


# print(possibleNextPositions(start_position))
# position = [7, 1]
# print(maze[position[0]][position[1]])
# print(junctions)


# position = [2, 4]
# print(isPositionInMatrix(start_position))

t = 0
while True:
    move = createMove(position)
    # print("m", move)
    traveled_maze[move[0]][move[1]] = "x"

    position = move

    # position = move(position)
    # print(position)
    # for i in traveled_maze:
    #         print('\t'.join(map(str, i)))``
    # print("\n")

    if (position == destination):
        print ("koniec")
        break
    if (position == [3,2]):
        t+=1
    if (t == 4):
        # for i in traveled_maze:
        #     print('\t'.join(map(str, i)))
        break