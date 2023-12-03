import re

games = []
ID_sum = 0

class Game:
    def __init__(self, game_string) -> None:
        self.possible = True
        self.game_num = int(re.findall("Game (\d{1,3}): ", game_string)[0])
        self.red = 0
        self.blue = 0
        self.green = 0
        cubes = re.findall("(\d{1,2}) ([a-z]{1,})", game_string)
        for cube in cubes:
            if cube[1] == "blue":
                if int(cube[0]) > self.blue:
                    self.blue = int(cube[0])
            elif cube[1] == "red":
                if int(cube[0]) > self.red:
                    self.red = int(cube[0])
            elif cube[1] == "green":
                if int(cube[0]) > self.green:
                    self.green = int(cube[0])
        
    def add(self):
        if self.possible == True:
            return self.game_num
        else:
            return 0
        
    def power(self):
        return self.red * self.blue * self.green
        
inputfile = open("Input.txt", "r")
gamelines = inputfile.readlines()

for gameline in gamelines:
    games.append(Game(gameline))

for game in games:
    ID_sum += game.power()
    
    
print(ID_sum)