class game():
    def __int__(self, nation, savedbefore = False, timeelapsed = None):
        self.nation  = nation
        self.savedbefore = savedbefore
        self.timeelapsed = timeelapsed

    def createnations(self):
        pass
    def createsavegame(self):
        pass



class nation():
    def __init__(self, name, armysize, unrest, international ):
        self.name = name
        self.armysize = armysize
        self.unrest = unrest
        self.international = international
