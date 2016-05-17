from random import randint,shuffle

"Damn this is hard"


Game=[]
Out=[]
Deck=[]
vis=[0]*7
def init():
    global Game,Out,Deck
    #output piles
    Out=[('H',0),('C',0),('S',0),('D',0)]
    
    #gamePiles
    Game=[[0]*i for i in range(1,8)]
    
    #Cards Decks
    Deck=[]
    Deck=Deck+[('R','H',i) for i in range(1,14)]
    Deck=Deck+[('B','C',i) for i in range(1,14)]
    Deck+=[('B','S',i) for i in range(1,14)]
    Deck+=[('R','D',i) for i in range(1,14)]
    
    
    for i in range(7):
        for j in range(len(Game[i])):
            k=randint(0,len(Deck)-1)
            
            Game[i][j]=Deck[k]
            del(Deck[k])
    shuffle(Deck)
    print "---------------------------------------------------------------------------------------------------------\n\n"      
    print Deck[0],
    print "\t\t\t\t",
    print Out
    print '\n\n'
    print "________________________________________________________________________\n\n"
    for index,pile in enumerate(Game):
        print pile[0],
        print "\t\t\t\t\t\t\t\t\t\t\t<---"+str(index)+" pile\n"
    print "____________________________________________________________________"

init()
print('\n')
while (input("Enter \n1:Reshuffle \n2:play\n"))!=2:
    init()

def nextDeck():
    Deck.append(Deck[::-1].pop())
    del(Deck[0])

while(True):
    fr1,fr2=map(int,raw_input("Enter pile number and index number card to move(first one index is 0)\n\t\tOR\n* (-1 0) for drawing from stock \n* (-2 0) for revealing next card in stock\n* (-4 0) to forfeit Game\n").split())
    if fr1==-4:
            x= raw_input("ARE YOU SURE Y/N :").strip()
            
            if x=='y'or x=='Y':
                print("------------------------------------------------------\n\n\n\n\n\n\n\n\n")
                print("You Lost ")
                print("\n\n\n\n\n\n\n\n\n------------------------------------------------------")
                break
    elif (fr1==-2):
        nextDeck()
    else:
        to=input("Enter pile number to move:\n* [0-7] for Game Piles\n* -1 for output pile\n")
        if fr1!=-1:
            if to==-1:
                
                outp=False
                choice=Game[fr1][fr2]
                dest=choice[1]
                for index,out in enumerate(Out):
                    if out[0]==dest:
                        if out[1]+1==choice[2]:
                            Out[index]=list(Out[index])
                            Out[index][1]=choice[2]
                            Out[index]=tuple(Out[index])
                            del(Game[fr1][fr2])
                            outp=True
                            break
                if outp==False:
                    print "Illegal Move"
            else:
                choice=Game[fr1][:fr2+1]
                if (Game[to]!=[] or choice[-1][2]!=13) and ( Game[to][0][0]==choice[-1][0] or Game[to][0][2]-1!=choice[-1][2]):
                    print "Illegal Move"
                    continue
                Game[fr1]=Game[fr1][fr2+1:]
                Game[to]=choice+Game[to]
                vis[to]+=len(choice)
        else:
            choice=Deck[0]
            if to==-1:
                outp=False
                dest=choice[1]
                for index,out in enumerate(Out):
                    if out[0]==dest:
                        if out[1]+1==choice[2]:
                            Out[index]=list(Out[index])
                            Out[index][1]=choice[2]
                            Out[index]=tuple(Out[index])
                            del(Deck[0])
                            outp=True
                            break
                if outp==False:
                    print "Illegal Move"
                    continue
            elif  (Game[to]!=[] or choice[2]!=13) and ( Game[to][0][0]==choice[0] or Game[to][0][2]-1!=choice[2]):
                print "Illegal Move"
                continue
            else:
                Deck=Deck[1:]
                Game[to]=[choice]+Game[to]
                vis[to]+=1
    
    stat=True
    for pile in Deck:
        if pile!=[]:
            stat=False
            break
    if stat== True:
        print "__________________________________________________________________________________________\n\n\n\n\n\n\n"
        print "\t\t\t\t CONGRATS YOU HAVE WON THE GAME \n\n\n\n\n\n\n\n"
        print "__________________________________________________________________________________________"
        break 
    print "-----------------------------------------------------------------------------------------------------------------\n\n"
    print Deck[0],
    print "\t\t\t\t",
    print Out
    print '\n\n'
    print "________________________________________________________________________\n\n"
    for index,pile in enumerate(Game):
        print pile[:vis[index]+1],
        print "\t\t\t\t\t\t\t\t\t\t\t<---"+str(index)+" pile\n"
    print "________________________________________________________________________"
    
    
    
    
