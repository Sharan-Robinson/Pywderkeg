import sqlite3


class game():
    def __int__(self, nation, savedbefore, timeelapsed):
        self.nation = nation
        self.savedbefore = savedbefore
        self.timeelapsed = timeelapsed

    def startgame(self):
        print("Please select a nation to play as!")
        gamenation = input(
            "1. Austria-Hungary\n"
            "2.Serbia\n"
            "3. Greece\n"
            "4. Turkey\n"
            "5. Bulgaria\n"
        )

        savegamename = input("What would you like to call this game?")
        self.createsavegame(self.game())

        

    def createnations(self, name):
        austria = nation('Austria', 50000, 50)
        serbia = nation('Serbia', 10000, 13)
        greece = nation('Greece', 15000, 5)
        albania = nation('Albania', 5000, 3)
        bulgaria = nation('Bulgaria', 10000, 10)
        romania = nation('Romania', 20000, 5)


    def createsavegame(self, savegamename):
        conn = sqlite3.connect('savegame1.db')

        c = conn.cursor()

        c.execute("""
        CREATE TABLE IF NOT EXISTS savegame(
        nation TEXT, 
        armysize INT,
        unrest INT
        )
        """)
        c.execute("""
        INSERT INTO savegame VALUES(
        "Austria",
        50000,
        50
        )""")
        conn.commit()
        conn.close()


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
