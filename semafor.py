import time
from form import*
from players import*
from sport import *


from xml.etree.ElementTree import XML

class Semafor():
    def __init__(self, sport):
        super().__init__()

        Display = sport.generateDisplay()
        self = Display

        self.title('Semafor')
        self.configure(bg="black")

        self.mainloop()