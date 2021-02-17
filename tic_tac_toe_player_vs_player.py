cell=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
turn=1 
result=-1
def create():
    print(" ___ ___ ___")
    print("| %c | %c | %c |" % (cell[0],cell[1],cell[2]))
    print("|___|___|___|")
    print("| %c | %c | %c |" % (cell[3],cell[4],cell[5]))
    print("|___|___|___|")
    print("| %c | %c | %c |" % (cell[6],cell[7],cell[8]))
    print("|___|___|___|")
#create()

def isempty(pos):
    if cell[pos] == ' ':
        return True
    else:
        return False

def isWinner():
    global result
    if cell[0]==cell[1] and cell[1]==cell[2] and cell[0]!=' ':
        result=1
    elif cell[3]==cell[4] and cell[4]==cell[5] and cell[3]!=' ':
        result=1
    elif cell[6]==cell[7] and cell[7]==cell[8] and cell[6]!=' ':
        result=1
    elif cell[0]==cell[3] and cell[3]==cell[6] and cell[0]!=' ':
        result=1
    elif cell[1]==cell[4] and cell[4]==cell[7] and cell[1]!=' ':
        result=1
    elif cell[2]==cell[5] and cell[5]==cell[8] and cell[2]!=' ':
        result=1
    elif cell[0]==cell[4] and cell[4]==cell[8] and cell[0]!=' ':
        result=1
    elif cell[2]==cell[4] and cell[4]==cell[6] and cell[2]!=' ':
        result=1
    elif cell[0]!=' ' and cell[1]!=' ' and cell[2]!=' ' and cell[3]!=' ' and cell[4]!=' ' and  cell[5]!=' ' and cell[6]!=' ' and cell[7]!=' ' and cell[8]!=' ' :
        result=0
    else:
        result=-1

print("Player 1 : X   And Player 2: O\n")

while(result==-1):
    create()
    if turn % 2 != 0:
        print("Player 1's Chance\n")
        symbol='X'
       
    else:
        print("Player 2's Chance\n")
        symbol='O'
    
    choice=int(input("Enter the position betwee 1 and 9 where you want to place your Symbol: \n"))
    if(isempty(choice-1)):
        cell[choice-1]=symbol
        turn+=1
        isWinner()
            
create()
if(result==0):
    print("Game Drawn\n")
elif result==1:
    turn-=1
    if(turn%2!=0):
        print("Player 1 Won\n")
    else:
        print("player 2  Won\n")

        
    