"""
###############################################################################################
*	testPage.py
*	Coded on: 2021 - 10 - 21
*	Author: Rakesh G Raman
*	Purpose:
	To test the US sensors.
*	The contents of this file are for the internal use at CELLINK only.
*	You are not allowed to distribute the contents of this file without prior written approval
	from CELLINK AB.
*	If you have received this file in error, you are kindly asked to notify us at the
	reception or delete the file.

*	~Copyright (c) CELLINK AB~
###############################################################################################
"""

from tkinter import *
from tkinter import font
import time
import sys

class Test:
	# Constructor
	def __init__(self, app, mqtt):
		self.app = app
		self.mqtt = mqtt

		# Style configuration
		self.headingFont = font.Font(family = "Lato", size = 16, weight = "bold")

		# Initialisation of variables
		self.flag = False
		self.cycle = 0
		self.cycleCount = 0

		#Config
		self.rangeCount = sys.maxsize
		self.sleepTime = 1.0

		# Initialisation of gcodes
		self.GCODE_USY = "M1120 S0"
		self.GCODE_USX = "M1120 S1"
		self.GCODE_READUS = "M1121"
		self.WAIT_UNTIL_COMPLETED = "M400"

		# Labelling
		self.label = Label(self.app, text = "ULTRASONIC SENSORS TEST", font = self.headingFont)
		self.startButton = Button(self.app, text = "Start test", command = self.startTest)

		# Alignment
		self.label.pack(pady = (5, 30))
		self.startButton.pack()

	# Escaping stuck window
	def runTest(self):
		for self.cycleCount in range(self.rangeCount):
			self.mqtt.commandNC(self.GCODE_USX)
			self.mqtt.commandNC(self.GCODE_USY)
			self.mqtt.commandNC(self.WAIT_UNTIL_COMPLETED)
			time.sleep(0.2)
			self.mqtt.commandNC(self.GCODE_READUS)
			self.mqtt.commandNC(self.WAIT_UNTIL_COMPLETED)
			time.sleep(0.5)

	# Function that starts test
	def startTest(self):
		print("Test started")
		time.sleep(self.sleepTime)
		self.app.after(100, self.runTest)