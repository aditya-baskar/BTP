import spade

global blocked_exits
blocked_exits = set()

class MyAgent(spade.Agent.Agent):
	class MyBehav(spade.Behaviour.PeriodicBehaviour):
		def onStart(self):
			print "Starting behaviour . . ."
			file_name = raw_input("Person Details File: ")
			file_obj = open(file_name)
			#set the initial postion of the person and the position of the exits for the movement
			self.x = int(file_obj.readline())
			self.y = int(file_obj.readline())
			self.exit_x = int(file_obj.readline())
			self.exit_y = int(file_obj.readline())
			#set the initial exit time to 0.
			self.exit_time = 0

		def _onTick(self):
			if self.x == self.exit_x and self.y == self.exit_y:
				print "(" + str(self.x) + ", " + str(self.y) + ")" + " At Time: " + str(self.exit_time)
				self.stop()
			if (self.x < self.exit_x):
				self.x = self.x + 1
			if (self.x > self.exit_x):
				self.x = self.x - 1

			if (self.y < self.exit_y):
				self.y = self.y + 1
			if (self.y > self.exit_y):
				self.y = self.y - 1
			#one time instance has passed. Increase the counter
			self.exit_time = self.exit_time + 1

	class ReceiveExitsBehav(spade.Behaviour.Behaviour):
		def _process(self):
			self.msg = None
			self.msg = self._receive(True, 10)
			if self.msg:
				exit = self.msg.content.split(',')
				exit = tuple(map(int, exit))
				if exit[0] != -1:
					global blocked_exits
					blocked_exits.add(exit)
					print blocked_exits
				print "got a message from exits ontology!! Content: {0}".format(self.msg.content)

	def _setup(self):
		print "MyAgent starting . . ."
		b = self.MyBehav(1)
		self.addBehaviour(b, None)

		time_template = spade.Behaviour.ACLTemplate()
		time_template.setOntology('exits')
		tmt = spade.Behaviour.MessageTemplate(time_template)
		rtb = self.ReceiveExitsBehav()
		self.addBehaviour(rtb, tmt)

if __name__ == "__main__":
	agent_id = raw_input("agent id: ")
	a = MyAgent("person" + agent_id + "@127.0.0.1", "secret")
	a.start()