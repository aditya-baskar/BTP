from helper import *
from move import *
import spade
import random
import sys

global blocked_exits, exits, agent_id, speed, vision
blocked_exits = set()

class MyAgent(spade.Agent.Agent):
	class MoveBehav(spade.Behaviour.PeriodicBehaviour):		
		def onStart(self):
			#print "Starting behaviour . . ."
			#set the initial exit time to 0.
			global speed, vision
			global agent_id
			speed = random.randrange(3) + 1
			#print "agent" + str(agent_id) + ": " + str(speed)
			vision = 20
			self.exit_time = 0

		def _onTick(self):
			global board, agent_id, blocked_exits, speed, vision
			prev_pos = get_position(agent_id)
			e = get_closest_exit(prev_pos, blocked_exits)
			visited = []
			for i in xrange(20):
				visited.append([])
				for j in xrange(20):
					visited[i].append(0)
			print "agent" + str(agent_id) + ": "
			board = get_board()
			pos = move(prev_pos, e, speed, vision, board)
			if pos == (-1,-1):
				blocked_exits.add(e)
			else:
				board = get_board()
				board[prev_pos[0]][prev_pos[1]] = 'o'
				if pos != e:
					board[pos[0]][pos[1]] = str(agent_id)
				print_board(board)
			self.exit_time = self.exit_time + 1
			if pos == e:
				print "agent " + str(agent_id) + ": " + str(exit_time)
				self.stop()

	class SendExitsBehav(spade.Behaviour.PeriodicBehaviour):
		"""
		class for sending current time to client agent
		"""

		def onStart(self):
			self.receiver = spade.AID.aid(name='receiver@127.0.0.1', addresses=['xmpp://receiver@127.0.0.1'])

		def _onTick(self):
			global agent_id, vision
			pos = get_position(agent_id)
			people = get_people_in_range(pos, vision)
			for person in people:
				msg = spade.ACLMessage.ACLMessage()
				msg.setPerformative('inform')
				msg.setOntology('blocked')
				msg.addReceiver(spade.AID.aid(name='person'+str(person)+'@127.0.0.1', addresses=['xmpp://person'+str(person)+'@127.0.0.1']))
				msg.setContent("Any blocked exits?")
				#print "Sending msg to person"+str(person)
				self.myAgent.send(msg)

	class ReceiveExitsBehav(spade.Behaviour.Behaviour):
		def _process(self):
			self.msg = None
			self.msg = self._receive(True, 10)
			if self.msg:
				if self.msg.content != '':
					exits = self.msg.content.split('.')
					if len(exits) != 0:
						exits = map(lambda x: tuple(map(int, x.split(','))), exits)
						global blocked_exits
						blocked_exits.add(exit)
						#print blocked_exits
				#print "got a message from exits ontology!! Content: {0}".format(self.msg.content)

	class ReceiveBlockedBehav(spade.Behaviour.Behaviour):
		def _process(self):
			self.msg = None
			self.msg = self._receive(True, 10)
			if self.msg:
				content = ""
				if (len(list(blocked_exits)) != 0):
					content = reduce(lambda x,y: x+'.'+y, map((lambda x: str(x[0])+','+str(x[1])), list(blocked_exits)))
				
				self.resp = spade.ACLMessage.ACLMessage()
				self.resp.setPerformative('inform')
				self.resp.setOntology('exits')
				self.resp.addReceiver(self.msg.getSender)
				self.resp.setContent(content)

				self.myAgent.send(self.msg)
			#print "got a message from blocked ontology!! Content: {0}".format(self.msg.content)



	def _setup(self):
		#print "MyAgent starting . . ."
		move_behav = self.MoveBehav(1)
		self.addBehaviour(move_behav, None)

		msg_send_behav = self.SendExitsBehav(1)
		self.addBehaviour(msg_send_behav, None)

		exit_template = spade.Behaviour.ACLTemplate()
		exit_template.setOntology('exits')
		emt = spade.Behaviour.MessageTemplate(exit_template)
		exit_behav = self.ReceiveExitsBehav()
		self.addBehaviour(exit_behav, emt)

		blocked_template = spade.Behaviour.ACLTemplate()
		blocked_template.setOntology('blocked')
		bmt = spade.Behaviour.MessageTemplate(blocked_template)
		block_behav = self.ReceiveBlockedBehav()
		self.addBehaviour(block_behav, bmt)

if __name__ == "__main__":
	global agent_id, exits
	exits = get_exits()
	agent_id = sys.argv[1]
	a = MyAgent("person" + agent_id + "@127.0.0.1", "secret")
	agent_id = int(agent_id)
	get_position(agent_id)
	a.start()