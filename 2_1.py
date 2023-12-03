import re

games = []
ID_sum = 0

class Game:
    def __init__(self, game_string) -> None:
        self.possible = True
        self.game_num = int(re.findall("Game (\d{1,3}): ", game_string)[0])
        cubes = re.findall("(\d{1,2}) ([a-z]{1,})", game_string)
        for cube in cubes:
            if cube[1] == "blue":
                if int(cube[0]) > 14:
                    self.possible = False
            elif cube[1] == "red":
                if int(cube[0]) > 12:
                        self.possible = False
            elif cube[1] == "green":
                if int(cube[0]) > 13:
                        self.possible = False
        
    def add(self):
        if self.possible == True:
            return self.game_num
        else:
            return 0
        
inputfile = open("Input.txt", "r")
gamelines = inputfile.readlines()

for gameline in gamelines:
    games.append(Game(gameline))

for game in games:
    ID_sum += game.add()

print(ID_sum)