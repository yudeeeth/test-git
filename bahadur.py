cd  i=0
game_on=1
def assign_alternate():
    global i
    x=int(input("whcih pos? (0-9)\n"))
    x=3
    if(i==0):
        list[x]='X'
        i=1
    else:
        list[x]='O'
        i=0

while game_on:
    assign_alternate()
    list
    if(input("endgame?")=='y'):
        game_on = 0
