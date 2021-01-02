import random
def draw():
    for i in range(N):
        print ( " ".join("{0:2d}".format(board[i,j]) for j in range(N)) )

def allowable(x, y):
    return 0 <= x < N and 0 <= y < N and board[x, y] == 0

def save(step, x, y):
    board[x, y] = step

def clear(x, y):
    board[x, y] = 0

def tryThere(step, x, y):
    successful = False
    candidate = 0
    while (not successful) and (candidate < knight_steps):
        u = x + delta_x[candidate]
        v = y + delta_y[candidate]
        if allowable(u, v):
            save(step, u, v)
            if step < N * N:
                successful = tryThere(step+1, u, v)
                if not successful:
                    clear(u, v)
            else:
                successful = True
        candidate += 1
    return successful

N = 7
knight_steps = 8

board = {}
for i in range(N):
    for j in range(N):
        board[i, j] = 0

delta_x = [2,1,-1,-2,-2,-1,1,2]
delta_y = [1,2,2,1,-1,-2,-2,-1]

(x0, y0) = (3, 3)

save(1, x0, y0)

if tryThere(2, x0, y0):
    print ( "We have solution:" )
    draw()
else:
    print ( "Solution does not exists" )

for i in range(N):
    for j in range(N):
        print('For x0 = :',i, 'and y0 = ', j, ":")
        save(1, i, j)
        if tryThere(2, i, j):
            print ( "We have solution:" )
            draw()
        else:
            print ( "Solution does not exists" )
