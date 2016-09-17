import spade

class MyAgent(spade.Agent.Agent):
	class MyBehav(spade.Behaviour.PeriodicBehaviour):
		def onStart(self):
			print "Starting behaviour . . ."
			self.x = 0
			self.y = 0
			self.exit_x = 10
			self.exit_y = 10
			self.exit_time = 0

		def _onTick(self):
			#print "Counter:", self.counter
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
			self.exit_time = self.exit_time + 1

	def _setup(self):
		print "MyAgent starting . . ."
		b = self.MyBehav(1)
		self.addBehaviour(b, None)

if __name__ == "__main__":
	a = MyAgent("person@127.0.0.1", "secret")
	a.start()