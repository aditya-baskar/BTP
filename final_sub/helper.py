global exits

def RepresentsInt(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False

def get_position(id):
	#print "here"
	f = open("board.txt", "r")
	lines = f.readlines()
	f.close()
	r = 0
	c = 0
	for line in lines:
		line = line.strip().split(',')
		for cell in line:
			if RepresentsInt(cell) and (int(cell) == id):
				return (r,c)
			c+=1
		r+=1
		c=0
	return (-1, -1)

def get_board():
	f = open("board.txt", "r")
	lines = f.readlines()
	f.close()
	return map(lambda s: s.strip().split(','), lines)

def get_people_in_range(pos, r):
	people = []
	board = get_board()
	low_x = max((pos[0]-r), 0)
	low_y = max((pos[1]-r), 0)
	high_x = min((pos[0]+r), 19)
	high_y = min((pos[1]+r), 19)
	for i in xrange(low_x, high_x+1):
		for j in xrange(low_y, high_y+1):
			if (i,j) != pos and RepresentsInt(board[i][j]):
				people.append(int(board[i][j]))
	return people

def get_closest_exit(pos, blocked_exits):
	global exits
	e = list(set(exits) - set(blocked_exits))
	dist = map(lambda p: (p[0]-pos[0])*(p[0]-pos[0]) + (p[1]-pos[1])*(p[1]-pos[1]), e)
	return e[dist.index(min(dist))]

def get_exits():
	global exits
	exits = []
	f = open("board.txt", "r")
	lines = f.readlines()
	f.close()
	lines = map(lambda s: s.strip().split(','), lines)
	r = 0
	c = 0
	for row in lines:
		for cell in row:
			if cell == 'e':
				exits.append((r,c))
			c+=1
		r+=1
		c=0
	return exits

def print_board(board):
	f = open("board.txt", "w")
	str_format = reduce((lambda x,y: x+'\n'+y), list(map(lambda row: reduce((lambda x,y: x+','+y), row), board)))
	f.write(str_format)
	f.close()