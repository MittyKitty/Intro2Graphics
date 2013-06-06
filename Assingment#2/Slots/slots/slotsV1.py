# Source File Name: slotsV1.py
#Author's name: Morgan Crunkleton
#Last Modified By: Morgan Crunkleton
#Date Last Modified: Friday May 31, 2012
# Version 1 of a simple slot machine, currently only has the gui set up
# No functinality has been added yet

from Tkinter import *
from PIL import ImageTk, Image
import os
import random

root = Tk()
Slot = ImageTk.PhotoImage(Image.open("Slots.jpg"))
blank = ImageTk.PhotoImage(Image.open("blank.jpg"))


myContainer = Frame(root)
myContainer.pack()

labelFrame = Frame(root)
labelFrame.pack()

backGround = Label(myContainer, image = Slot)
backGround.pack()

wheel1 = Label(myContainer, height = "65", width = '50', image = blank)
wheel1.pack()
wheel1.place(x = 29, y = 125)

wheel2 = Label(myContainer, height = "65", width = "50", image = blank)
wheel2.pack()
wheel2.place(x = 87, y = 125)

wheel3 = Label(myContainer, height = "65", width = "50", image = blank)
wheel3.pack()
wheel3.place(x = 145, y = 125)

jackpot = Label(labelFrame, text ="Jackpot")
jackpot.pack()

money = Label(labelFrame, text="Money")
money.pack()

currentBet = Label(labelFrame, text="Current Bet")
currentBet.pack()

spinButton = Button(myContainer, text = "spin")
spinButton.pack()

bet100Button = Button(myContainer, text = "Bet 100")
bet100Button.pack()

bet50Button = Button(myContainer, text = "Bet 50")
bet50Button.pack()
bet50Button.place( x = 47, y = 255)

bet500Button = Button(myContainer, text = "Bet 500")
bet500Button.pack()
bet500Button.place( x = 139, y = 255)

quitButton = Button(labelFrame, text = "Quit")
quitButton.pack()
root.mainloop()
