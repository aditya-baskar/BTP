import spade

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

	def _setup(self):
		print "MyAgent starting . . ."
		b = self.MyBehav(1)
		self.addBehaviour(b, None)

if __name__ == "__main__":
	agent_id = raw_input("agent id: ")
	a = MyAgent("person" + agent_id + "@127.0.0.1", "secret")
	a.start()