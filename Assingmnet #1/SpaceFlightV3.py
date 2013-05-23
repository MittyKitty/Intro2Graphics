#Name: Space Flight
#Author: Morgan Crunkleton
#Last Modified By: Morgan Crunkleton
#Date Last Modified: May 20, 2012
#Program Description: A simple text based game
#Revision History: Version 3.0 Both paths are now fully coded
#               As well as additional comments


# Importing programs to use certain functions                  
import random
import time

#Displays the intro to the game
def displayIntro():
        print ("The year is 2XXX, with Earth's resources becoming dangerously")
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
                destination = raw_input()
        return destination

#function that will run if player desides to continue drilling
def detour():
        detourDesision = ''

        print("")
        print("A month into your return trip, you have several comanders come to you")
        print("'sir, the men grow restless, there is talk of mutiny if they don't")
        print("get out and stretch their legs so to speak, there is a weigh station")
        print("2 days from here, a few days there will give them the chance they need")
        print("to unwind")
        print("Wonderful, you think, stopping a whole day to drill through the ice already put")
        print("us behind schedule, spending a few days on 'shore leave' won't help matters.")
        print("However, I can't risk a mutiny, and the men did work hard during the dig,")
        print("they deserve some R&R. What do i do?")
        print("Continue home (1) Stop at the weigh station and enjoy a few days off (2)")
        detourDesision = raw_input()

        if detourDesision == '1':
                print("'I'm afriad I can't do that, we're behind schedule as is")
                print("we continue our present course'")
                time.sleep(2)
                print("you wake up in the middle of the night with a hand over")
                print("your mouth, being dragged to the air lock")
                print("'I'm sorry sir, I did try to warn you' he says.")
                print("He presses the button and you're shot out into space")
                print("Well, at least in space, no one can hear you scream...")
                time.sleep(5)
        elif detourDesision == '2':
                print("'Very well men, we'll make the stop, infact...")
                print("the whole trip is on me")
                time.sleep(2)
                print("You return to your ship three days later and make the journy")
                print("home. Sure you're a few days later, but you had a great time")
                print("and are returning home with a full cargo bay, which is sure")
                print("to please your higher ups")

#Function that will run if player chooses not to drill the ice, which will lead to death
#Regardless of choice made
def otherOption():
        otherDesision = ''

        print("'We could fire our laser at the ice from a safe distance, melting it.")
        print("'Are there any risks?' you ask")
        print("None what I'm aware of, besides, we'll be a at a safe distance should")
        print("something go wrong'")
        print("Sounds reasonable right? What do you have to lose?")
        print("Fire the laser (1) Continue on your way (2)")
        otherDesision = raw_input()

        if otherDesision == '1':
                print("'Bring the laser online'. Once the laser")
                print("heats up it fires direct hit! However,")
                print("the blast creates far more debris then")
                print("anticipated.Remind me to fire that engineer, you")
                print("think to yourself as a huge chunk of rock")
                print("crashes into the cockpit")
        elif otherDesision =='2':
                print("'There are too many unknown variables, I'm")
                print("not going to risk it, continue packing up'")
                print("The last line comes in with no trouble")
                print("Little do you realize, it brought along an")
                print("uninvited guess, who is incredibly hungry...")
                
        
# Function that will run if player picks asteroid belt
# This is the path that leads to winning
def asteroidBelt():
        desision = ''

        print("The engines hum to life as you set out toward the Asteroid Belt")
        print("The few week journy is uneventful, nothing too major required your attention,")
        print("and was rather relaxing, even got caught up on some reading")
        print("'Captain, we've arived at our destination', you hear on the P.A one morning")
        print("'Launch the lines and begin the anchor process'")
        print("The asteroid you were about to mine was huge and if the scanners were to be believed,")
        print("full of raw materials, this was going to be a huge pay off")
        print("")
        print("About 2 weeks into the process you hit a snag")
        print("'We've hit a huge block of ice sir'")
        print("Ice was incredably difficult and dangerous to cut through,")
        print("dig too fast and you run the risk of losing control of your drill and slaming the entire")
        print("ship into the asteroid, dig too slow and the steam form the ice could damage the equipment")
        print("'Why didn't our scans pick this up?' You ask, annoyed")
        print("'The ice was too far inside the asteroid and surrounded by iorn deposits sir,")
        print("there was no way we could have forseen this'")
        print("Great, you think to yourself, what do I do now? The ship's cargo bay is just over half full,")
        print("so I could return early and still make a profit, or we could risk digging")
        print("through and collect the rest of the materials")
        print("What do you do?")
        print("Stay and mine (1) Turn around and return home(2)")
        desision = raw_input()

        if desision == '1':
                print("'Fire up the drill, we're going to rip apart this ice block'")
                print("Drilling takes several hours but goes along smoothly and before the end")
                print("of the day you make your way through the ice")
                print("The next morning, digging resumes, the amount of iron and nickel you")
                print("uncover is ridiculous, MineU will be most pleased")
                print("The ship's cargo bay reaches mass capacity in a few short weeks")
                print("You bring in your lines and begin to reutrn home, feeling very pleased with")
                print("yourself...")
                time.sleep(2)
                detour()
        elif desision == '2':
                print("'I'm not going to risk our crew, we have a substantial load already,")
                print("enough to trun a profit anyway, pack up the operation, we're heading home'")
                print("And so begin to pack up the operation, however, thoughts")
                print("of all the money you're leaving behind linger in your mind...")
                time.sleep(2)
                print("Your head engineer approaches you")
                print("'sir', he says calmly,'there is another option'")
                otherOption()
                        
##########################################################################################################################
#All functions regarding Kupitor belt path are below here

#function that runs if the play follows the alien ship
def followShip():
        followDesision = ''

        print("'We need to follow that ship, it may be hostile. And")
        print("if thats the case, earth may be at risk'")
        print("So you race after the alien space craft")
        print("Eventually, you come across some wreckage left beind,")
        print("presumably from the craft. There is a chance that")
        print("there are some survivors, do you stay and search?")
        print("or do you continue following the ship?")
        print("Stay (1) Continue (2)")
        followDesision = raw_input()
        
        if followDesision =='1':
                print("The next few hours consist of a desperate search")
                print("for survivors, but hope of finding any was low,")
                print("how could anything live through this?")
                print("You eventually come across what you assume")
                print("is a probe left behind by the alien craft")
                print("It spots you and before you can react")
                print("it launches it's defensive lasers that cut through your")
                print("vessel like butter.Its like what they say")
                print("'No good deed goes unpunished'....")
        elif followDesision =='2':
                print("'This isn't a desision I make likely, we don't stop'")
                print("As you pass by the destroyed ships, you can't wonder")
                print("if there are people still alive. No, as tragic as this is")
                print("it is more important to track the ship and warn Earth as")
                print("soon as possible. Eventually you get close enough to")
                print("the ship to attempt contact. Once you do, the ship returns")
                print("the favor by hacking your ship, disabling your life support")
                print("systems. Its only a matter of time before you run out of air")
                print("suffocating to death...")

def ignoreShip():
        ignoreDesision = ''

        print("'That ship is none of our concern, we are out here to mine rocks")
        print("and thats what we will do'")
        print("The scanners locate the optimal asteroid for mining")
        print("However, this asteroid is occupied by a rival company")
        print("The asteroid is loaded with raw materials and its likely that")
        print("you won't find another one remotly as rich")
        print("anywhere reasonably close by. Do you attempt to")
        print("take the asteroid by force? Or do you leave them")
        print("in hopes of finding another suitable asteroid?")
        print(" Fight (1) Flight (2) ")
        ignoreDesision = raw_input()

        if ignoreDesision =='1':
                print("'We're the bigger ship, we'll cut their lines and ram them,the")
                print("if we aim it right, the force of the impact will")
                print("knock them loose and our shields can handle whatever defences they")
                print("may have'")
                print("The lasers effortlessly cut through thier lines and you")
                print("ram their ship, sending them floating away")
                print("They turn around and flee, almost as if they're eger to leave")
                print("You ride in to claim your prize, however, just as you're getting settled in")
                print("you realize too late that they rigged the asteriod with mines")
                print("incase an event such as this would occur")
                print("The ship bumps into one and sets its off, causing a chain")
                print("reaction, your ship's armor didn't stand a chance")
        elif ignoreDesision =='2':
                print("'If we were to attack a rival company, think of")
                print("the bad press we'd get. No, we find somewhere else'")
                print("You discover another asteroid, not as pleniful as")
                print("the one you abandoned, and is uncomfortably close to a star")
                print("but it will have to do. The mining set up is quick")
                print("and smooth but soon after the star near the asteroid")
                print("goes super nova, incinerating your ship instantly...")
                
#function that runs if player goes to the kupior belt, this path will always lead to player death
def kupitorBelt():
        desision = ''
        
        print("The engines hum to life as you head towards the Kupitor belt")
        print("The journy is long but uneventful, gives you the chance to")
        print("catch up on some paper work. A month into the trip")
        print("you get a call form the navigator.'sir, we've picked up")
        print("something strange on the long range scanner'")
        print("'What is it?', you ask.")
        print("'Well, its a large ship like object")
        print("twice the size of us and traveling at almost light speed'")
        print("'But light speed is impossible, what are we dealing with here?'")
        print("'Well, if I had to guess, I'd say it is indeed a space craft")
        print("and since no man made ship and move anywhere close to that")
        print("speed, I'd say we're dealing with an alien vessel'")
        print("'Wonderful.... What are our options?")
        print("'We don't know its intent, I suggest we follow close enough")
        print("where we can collect intel and not be noticed'")
        print("'Its almost going the speed of light, how can we do that?")
        print("'Thats the thing sir, its decelerating, by our calcuations")
        print("it will reach its destination within 3 weeks.'")
        print("'And wheres that?'")
        print("'Earth, sir'")
        print("")
        print("Follow the ship (1) Not my problem, ignore it (2)")
        desision = raw_input()

        if desision == '1':
                followShip()
        elif desision == '2':
                ignoreShip()
# Checks the choice made by the player, and outputs text depending on what was chiosen
def checkDestination(chosenDestination):
        
        
        if chosenDestination == '1':
                print ("'We head to the asteroid belt. We'll mine a rock so big, they'll be bonuses all round!'")
                print ("Your message is met with thunderous applause from the crew")
                asteroidBelt();
        else:
                print ("'We head to the Kupitor belt, I don't want any trouble during this mission'")
                kupitorBelt();

# The main function, or game loop if you will. Where all the functions so far are called.
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
