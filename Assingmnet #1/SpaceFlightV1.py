#Name: Space Flight(Work in progress)
#Author: Morgan Crunkleton
#Last Modified By: Morgan Crunkleton
#Date Last Modified: May 16, 2012
#Program Description: A simple text based game
#Revision History: Version 1.0 Game only includes one choice with no outcome yet.
                  
import random
import time

#Displays the intro to the game
def displayIntro():
	print ("The year is 20XX, with Earth's resources becoming dangerously")
	print ("low, asteroid mining has becoming necessary, as well as profitable.")
	print ("You are the captain on MineU's largest mining ship, the El Cavador")
	print ("Asteroid mining is an increadably dangerous profession")
	print ("As captain, you are faced with life or death decisions. Do you take bold")
	print ("risks to help your company's bottom line? Or do you play it safe to protect")
	print ("you and your crew? Do you have what it takes to captain the El Cavador?")
	print ("")
	
# The first choice of the game, sets everything else in motion
def chooseDestination():
	destination = ''
	while destination != '1' and destination != '2':
		print ("'Captain, all system checks are good, we are ready to luanch as soon as you give us a destination'")
		print ("You sit and ponder your choices, MineU has never given you a choice as to where you mine,")
		print ("which is very odd but you have no time to mill it over now, the crew needs a heading")
		print ("Do you head to the asteroid belt? Where there are plently of large rocks to mine but")
		print ("there have been recent reports of pirates, or do you head to the Kupitor belt,")
		print ("2 months farther away and has smaller rocks but is relitivly abandoned by other miners")
		print ("Asteroid Belt (1) Kepitor Belt (2)")
		print ("")
		destination = raw_input()
	return destination

def checkDestination(chosenDestination):
	
	
	if chosenDestination == 1 :
		print ("'We head to the asteroid belt. We'll mine a rock so big, they'll be bonuses all round!'")
		print ("Your message is met with thunderous applause from the crew")
	else:
		print ("'We head to the Kupitor belt, I don't want any trouble during this mission'")



def main():
	
	
	playAgain = 'yes'
	while playAgain == 'yes' or playAgain == 'y':
		displayIntro()
		destinationNumber = chooseDestination()
		checkDestination(destinationNumber)
	        print ("")
		print ('Do you want to play again? (yes or no)')
		playAgain = raw_input()


if __name__ == "__main__": main()
