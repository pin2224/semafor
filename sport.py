from tkinter import *
from tkinter import ttk

class Sport():

    def __init__(self, player_list):

        self.home_name='HOME'
        self.guest_name='GUEST'
        self.score_home=0
        self.score_guest=0

    def generateDisplay(self):
        frame = Tk()

        Label(frame, name='homename', text=self.home_name, bg='black', fg='white', font= 'digital-7').grid(row=0,column= 0, sticky=N+S+E+W)
        Label(frame, name='time', text='00:00', bg='black', fg='yellow', font= 'digital-7').grid(row=0, column=1, sticky=N+S+E+W),
        Label(frame, name='guestname', text=self.guest_name, bg='black', fg='white', font= 'digital-7').grid(row=0, column=2,sticky=N+S+E+W)

        return frame


class Player():

    def __init__(self, name, number=0):
        self.name = name
        self.number = number
        self.points = 0
        self.misses = 0
        self.height = 0
        self.weight = 0

    def score(self):
        self.points+=1

    def miss(self):
        self.miss+=1

class Kosarkas(Player):

    def __init__(self, name, number=0):
        self.super(name, number)
        self.offensive_rebound = 0
        self.defensive_rebound = 0
        self.field_goal_attempts = [0, 0, 0]
        self.field_goal_made = [0, 0, 0]
        self.fauls = 0
        self.steals = 0

    def score(self, type=1):
        self.points += type
        self.field_goal_made[type] += 1


class Rukometas(Player):

    def __init__(self, name, number=0):
        self.super(name, number)

class Odbojkas(Player):

    def __init__(self, name, number=0):
        self.super(name, number)

class Nogometas(Player):

    def __init__(self, name, number=0):
        self.super(name, number)
