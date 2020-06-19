#!/usr/bin/env python3
import sqlite3
import re
from tkinter import *
#from PIL import Image, ImageTk

root = Tk()
root.geometry("400x400")
root.title("Activity Log")

conn = sqlite3.connect('/home/brandon/GST/Activity.db') #Connect to Database
c = conn.cursor() #Allows you to use SQL commands

#c.execute("""CREATE TABLE activities (   
#title text,
#minutes integer
#)""")

class Activity: # Activity object

	def __init__(self, title, min):
		self.title = title
		self.min = min

	def toString(self):
		print("Activity: ", self.title, "\nMinutes Spent:", self.min)

##### Database Create ###### Functional ######
def CreateActivity():
	newTitle = input('Enter Name of Activity: ')
	newMin = input('Enter Amount of Minutes logged: ')
	d = Activity(newTitle, newMin)
	print(d)
	c.execute("INSERT INTO activities VALUES (?, ?)", (d.title, d.min))

##### Database Update ##### Functional ###### Adds time to Activity #####
def UpdateTime():
	whichTitle = input("What activity do you want to add your time to?")
	addedMin = input('How many minutes do you have to log?')
	newMin = GetPrevMin(whichTitle) + int(addedMin)
	with conn:
		c.execute("""UPDATE activities SET minutes = :newMin WHERE title = :whichTitle""", {"newMin": newMin, "whichTitle": whichTitle}
		)

##### Database Delete ##### Functional ######
def DeleteActivity():
	delTitle = input('What Activity would you like to delete?')
	with conn:
		c.execute("DELETE FROM activities WHERE title = :del", {"del": delTitle})

##### Helper Function for DB Update ##### Functional #####
def GetPrevMin(title):
	for row in c.execute("SELECT minutes FROM activities WHERE title = :tit", {"tit": title}):
		prevMin = row[0]
	return prevMin

def driverFunc():

	### root.mainloop()
	print(('Activity', 'Minutes Spent'))
	for row in c.execute("SELECT title, minutes FROM activities"):
		print(row)
	usrIn = input("Type \"log\" to add time to an activity. \nType \"create\" to create a new activity.\nType \"delete\" to delete  an activity.\n")
	searchForLog = re.search('log', usrIn, re.M|re.I)
	searchForCreate = re.search('create', usrIn, re.M|re.I)
	searchForDel = re.search('delete', usrIn, re.M|re.I)
	print(searchForLog)

	if searchForLog:
		UpdateTime()
	elif searchForCreate:
		CreateActivity()
	elif searchForDel:
		DeleteActivity()
	else:
		print("Invalid Input!")

	conn.commit()

def UIDriver():
	def logShow():
		pass
	def createShow():
		pass
	def deleteShow():
		pass
	def showDB():
		for row in c.execute("SELECT title, minutes FROM activities"):
			myLabel = Label(root, text=row)
			myLabel.pack()

	showDB() # Shows Log


	logButton = Button(root, text="Log Time", command=logShow)
	logButton.pack()

	createButton =  Button(root, text="Create a New Activity", command=createShow)
	createButton.pack()

	createButton =  Button(root, text="Delete an Activity", command=deleteShow)
	createButton.pack()


	root.mainloop()

##### Main Loop #####
#driverFunc()
UIDriver()