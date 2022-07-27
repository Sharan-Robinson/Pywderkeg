import sqlite3


class game():
    def __int__(self, nation, savedbefore=False, timeelapsed=None):
        self.nation = nation
        self.savedbefore = savedbefore
        self.timeelapsed = timeelapsed

    def createnations(self, name):
        austria = nation('austria', 50000, 50.0)
        serbia = nation('Serbia', 10000, 13.0)
        greece = nation('Greece', 15000, 5.0)
        albania = nation('Albania', 5000, 3.1)
        bulgaria = nation('Bulgaria', 10000, 10.0)
        romania = nation('Romania', 20000, 5.0)
        pass

    def createsavegame(self, savegamename):
        conn = sqlite3.connect(f'{savegamename}.db')

        pass


class nation():
    def __init__(self, name, armysize, unrest):
        self.name = name
        self.armysize = armysize
        self.unrest = unrest

    def getarmysize(self):
        return self.armysize

    def setarmysize(self, size):
        self.armysize = size

    def getname(self):
        return self.name

    def getunrest(self):
        return self.unrest

    def setunrest(self, unrest):
        self.unrest = unrest
