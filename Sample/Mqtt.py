"""
###############################################################################################
*	Mqtt.py
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

import paho.mqtt.client as mqtt
import simplejson as json
from tkinter import *

class Mqtt:
	# Constructor
	def __init__(self):
		# Creating an object for the mqtt protocol
		#self.VERSION = bioxVer
		self.client = mqtt.Client()
		self.client.connected_flag = False
		self.mqtt_callbacks = []

		# BIO X VERSIONS
		self.BIO_X = 1
		self.BIO_X2 = 2
		self.BIO_X6 = 6

	def add_handler(self, mqtt_callback_handler):
		self.mqtt_callbacks.append(mqtt_callback_handler)

	# Enabling connection & subscriptions to the printer
	def setup_mqtt(self):
		#self.client.connect('cellink-bio-x.local', 1883, 60)
		self.client.on_connect = self.on_connect

		for handler in self.mqtt_callbacks:
			self.client.subscribe(handler.topic)
			self.client.message_callback_add(handler.topic, handler.callback)

		# Toggling the torskechoall ON
		self.client.publish('/control/debug/torskechoall', "1")
		self.client.subscribe('/control/debug/echo/all')
		self.client.on_message = self.on_message
		self.client.loop_start()

	# Checks connectivity with printer
	def on_connect(self, client, userdata, flags, rc):
		if(rc == 0):
			# Connected
			self.client.connected_flag = True
			print("Printer connected: OK")
		else:
			# Not connected
			self.client.connected_flag = False
			print("Bad connection, Return code = ", rc)

	# Activates the abilitiy to receive inputs from the NC
	def on_message(self, client, userdata, message):
		# The subscribed topic is the input
		self.topic = str(message.topic)
		self.line = str(message)
		self.message =  str(message.payload.decode('utf-8'))

		if (self.topic.endswith('/echo/all')):
			self.json_Message = json.loads(self.message)
			#print("OM - Message: " + self.message)

			if (self.json_Message["key"].startswith("USV")):
				if (self.json_Message["key"].endswith("X")):
					print("X distance: " + str(self.json_Message["value"]))
				#elif (self.json_Message["key"].endswith("Y")):
				#	print("Y distance: " + str(self.json_Message["value"]))

	# Detecting the error
	def error_update(self, message):
		print("Error update")

	# Activates G&M codes to the NC
	def commandNC(self, the_input, comparison = "NONE"):
		self.client.publish('/control/debug/gcode', the_input)
		self.comparison = comparison