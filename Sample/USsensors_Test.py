"""
###############################################################################################
*	USsensors_Test.py
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

from init import *

# Start the programme
if __name__ == '__main__':
	_init_ = init(_mqtt_)
	_init_.start()