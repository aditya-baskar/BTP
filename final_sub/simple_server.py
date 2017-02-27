import subprocess
from bottle import run, post, request, response, get, route

@route('/<path>',method = 'GET')
def process(path):
	f = open('board.txt', 'r')
	lines = f.readlines()
	f.close()
	resp = ""
	for i in lines:
		resp += i
	return resp

run(host='localhost', port=8080, debug=True)