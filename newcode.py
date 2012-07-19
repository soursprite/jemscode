from random import randint
from sys import exit


class Game(object):

    def __init__(self, name):
	    self.name = name
		#self.fatigue = 0


	def death(self):
		#I dont get it
		death.taunt = ["The last thing you hear is the oddly satisfying crunch as one of them bites through your trachea.",
		               "The taste of metal fills your mouth as your screams turn to mad gurgling. The end comes too slow.",
					   "As you see them ripping flesh from your bones, you scream. Not because of the pain, but because there is nothing else you can do.",
					   "As the pain rips the voice from your lungs, your only comfort is that there will not be enough left of you to rise again."
					   ]
		return death.taunt[randint(0,len(death.taunt)-1]	