from sets import Set
from helper import RepresentsInt
import operator
import astar
import numpy

def dist(pos1, pos2):
    return (pos1[0]-pos2[0])*(pos1[0]-pos2[0]) + (pos1[1]-pos2[1])*(pos1[1]-pos2[1])

def change_board(vision, board, previous_pos, exit_pos):
    for i in xrange(max(previous_pos[0]-vision, 0), min(previous_pos[0]+vision, 19)+1):
        for j in xrange(max(previous_pos[1]-vision, 0), min(previous_pos[1]+vision, 19)+1):
            if board[i][j] == 'o' or board[i][j] == 'e':
                board[i][j] = dist((i, j), exit_pos)
            else:
                board[i][j] = 9999999999999
    return board

def get_min(board, vision, pos):
    cur_min = 9999999999999
    final_pos = (-1, -1)
    for i in xrange(max(pos[0]-vision, 0), min(pos[0]+vision, 19)+1):
        for j in xrange(max(pos[1]-vision, 0), min(pos[1]+vision, 19)+1):
            if board[i][j] <= cur_min:
                cur_min = board[i][j]
                final_pos = (i, j)
    return final_pos

def create_astar_board(board, vision, pos):
    for i in xrange(20):
        for j in xrange(20):
            flag = 1
            if i in range(max(pos[0]-vision, 0), min(pos[0]+vision, 19)+1):
                if j in range(max(pos[1]-vision, 0), min(pos[1]+vision, 19)+1):
                    if board[i][j] == 'o' or board[i][j] == 'e':
                        flag = 0
            board[i][j] = flag 
    board[pos[0]][pos[1]] = 0
    return board


def move(previous_pos, exit_pos, speed, vision, board):
    original_board = []
    for i in range(len(board)):
        original_board.append([])
        for j in range((len(board[i]))):
            original_board[i].append(board[i][j])
    #print original_board
    new_board = change_board(vision, board, previous_pos, exit_pos)
    target_pos = get_min(new_board, vision, previous_pos)
    new_board = create_astar_board(original_board, vision, previous_pos)
    for i in new_board:
        print i
    path = astar.astar(numpy.array(new_board), previous_pos, target_pos)
    path.reverse()
    print path
    #print path
    return path[min(speed, len(path)-1)]
    """
    Q = Set([])
    dist = {}
    prev = {}
    for i in xrange(max(previous_pos[0]-vision, 0), min(previous_pos[0]+vision, 19) + 1):
        for j in xrange(max(previous_pos[1]-vision, 0), min(previous_pos[1]+vision, 19) + 1):
            Q.add((i, j))
            dist[(i,j)] = 9999999999999
            prev[(i,j)] = (-1, -1)
    dist[(previous_pos)] = 0

    #print str(target_pos) + " : " + str(dist[target_pos])
    while len(Q) > 0:
        #print len(Q)
        index = 0
        u = (-1,-1)
        min_val = 9999999999999
        for node in Q:
            if dist[node] <= min_val:
                min_val = dist[node]
                u = node
        Q.remove(u)
        
        for i in xrange(max(u[0]-1, 0), min(u[0]+2, 20)):
            for j in xrange(max(u[1]-1, 0), min(u[1]+2, 20)):
                if (i,j) != u:
                    v = (i,j)
                    if new_board[v[0]][v[1]] >= 9999999999999:
                        alt = dist[u] + 9999999999999
                    else:
                        alt = dist[u] + 1
                        
                    if len(Q.intersection(Set([v]))) > 0:
                        if alt < dist[v]:
                            dist[v] = alt
                            prev[v] = u

    path = []
    v = target_pos
    while v != previous_pos:
        path.append(v)
        v = prev[v]
    path.append(v)
    path.reverse()
    #print "here"
    if target_pos == exit_pos and dist[exit_pos] >= 9999999999999:
        return (-1,-1)
    if speed >= len(path):
        speed = len(path)-1
    while dist[path[speed]] >= 9999999999999 and speed > 0:
        speed -= 1
    if path[speed] >= 9999999999999:
        print "cant_move"
    return path[speed]"""