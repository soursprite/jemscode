#its an adventure game with zombies.
#Option A, leads to scenario A with options of its own.

from random import randint
from sys import exit

class Player(object):

	
    def __init__(self):
	#player carries fatigue based on choices made, changes outcome of other choices
    #or presents new choices all together. Haven't really decided
        self.fatigue = 0

	
    def death(self):
		#obviously the player can die, and these are some death messages.
        taunt = ["The last thing you hear is the oddly satisfying crunch as one of them bites through your trachea.",
		         "The taste of metal fills your mouth as your screams turn to mad gurgling. The end comes too slow.",
                 "As you see them ripping flesh from your bones, you scream. Not because of the pain, but because there is nothing else you can do.",
                 "As the pain rips the voice from your lungs, your only comfort is that there will not be enough left of you to rise again."
				]
        print taunt[randint(0,len(taunt)-1)]
        print "Game Over"
        exit()
		

class Game(object):

    def __init__(self, start):
        self.start = start
        self.player = Player()
        
    def play(self):
        next_scene = self.start
        #this loop should continuously run the next function unless an 'exit()' is called
        while True:
            print "-"*20
            scene = getattr(self, next_scene)
            next_scene = scene()
            
    def textPrint(self, text):
        #prints out a block of text and caps it to X number of chars per line.
		#Words that go past the char limit start at the next line
        #less buggy now
        #I also want it to ignore new lines in the text
        chars = list(text)
        for char in chars:
            line = []
            while len(line) < 60 and len(chars) > 0:
                if chars
                line[len(line):] = [chars.pop(0)]
                if line[len(line)-1] == " " and len(line) >= 55:
                    break
            print "".join(line)

            
class TheDarkApartment(Game):
    
    def theStreet(self):
        print "Hello"
        self.textPrint("""If I type a bunch of text here, it should work.
                          If I type a bunch of text here, it should work""")
        choice = raw_input("> ")
        exit()
 
new_game = TheDarkApartment('theStreet')
new_game.play()