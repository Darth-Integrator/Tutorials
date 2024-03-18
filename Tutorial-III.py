from tkinter import *

class body:
	def __init__(self):
		# Application
		self.top = Tk()

		# Variable initialisation
		self.iNpUt = ""

		# Labelling
		self.L1 = Label(self.top, text = "User Name")
		self.E1 = Entry(self.top, bd = 5)
		self.B1 = Button(text = "Get", command = lambda:self.buttonOutput())

		# Alignment
		self.L1.pack(side = LEFT)
		self.E1.pack(side = RIGHT)
		self.B1.pack(side = RIGHT)

	def buttonOutput(self):
		self.iNpUt = self.E1.get()
		print(self.iNpUt)

if __name__ == '__main__':
	hand = body()
	hand.top.mainloop()

#variabel = E1.get()
#print(variabel)

#

#1938460912386541902836549827364----- aDD --- iewsdfut yw3874yt bkwjrht49
#http://ww2.jkflamingoofgoogilceo.com/organ/shady/transplant.ckjrebf-20021-hisnameisabdullah?ad-23890?ok