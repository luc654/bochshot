import random

class Player:
    def __init__(self, lives, name):
        self.lives = lives
        self.name = name
        
    def removeLive(self):
        if self.lives > 0:
            self.lives -= 1
        else:
            return "Dead"
            
    def getName(self):
        return self.name
    
    def getLives(self):
        return self.lives

def generateShells():
    blanks = random.randint(1, 6)
    live = random.randint(1, 6)
    total = blanks + live
    listValue = {"blanks": blanks, "live": live, "total": total}
    return listValue

def showShells(shellList):
    blank = "◯"
    live = "⬤"
    display_string = ""

    # Add blanks (◯)
    for _ in range(shellList['blanks']):
        display_string += blank

    # Add lives (⬤)
    for _ in range(shellList['live']):
        display_string += live

    return display_string
shellList = generateShells()

def updatelist(shell_type):
    shellList[shell_type] -= 1  

def shoot():
    total = shellList['blanks'] + shellList['live']  
    shot = random.randint(1, total)  

    if shot <= shellList['live']:  
        updatelist('live')
        return 'live'
    else:  
        updatelist('blanks')
        return 'blank'


print(showShells(shellList))

player1 = Player(3, "player 1")
player2 = Player(3, "player 2")

print(shoot())
print(showShells(shellList))

# Main game loop
ongoing = player1.getLives() > 0 and player2.getLives() > 0
while ongoing:
    # Player one 
    choice = 1
    while choice == 1:
        print(player1.getName() + "....")
        print("(Shoot yourself)[1]")
        print("(Shoot "+player2.getName()+")[2]")
        print()
        try:
            choice = int(input(">"))
        except:
            choice = 1
    print("----------")
