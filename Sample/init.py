from tkinter import *
import testPage

class init:
	# Constructor
	def __init__(self):
		self.app = Tk()
		self.app.geometry("350x250")
		self.app.minsize(350, 250)
		self.app.title("Ultrasonic Sensors Test Application")

		# Default style
		self.app.option_add("*Menu.Font", "Lato 11")
		self.app.option_add("*Label.Font", "Lato 11")
		self.app.option_add("*Button.Font", "Lato 11")
		self.app.option_add("*Radiobutton.Font", "Lato 11")
		self.app.option_add("*Checkbutton.Font", "Lato 11")

	# The function that runs the application
	def start(self):
		self.app.mainloop()

	# Calculate blood pressure
	def cal_bp(self):
		self.bp[] = {100, 110, 113, 98}
		

	# Function tha handles closing the window
	def stop (self):
		self.app.quit()