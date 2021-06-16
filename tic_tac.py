
v_list=["1","2","3","4","5","6","7","8","9"]

s_game=["-","-","-",
        "-","-","-",
        "-","-","-"]

def show_block():
    print(s_game[0]+" | "+s_game[1]+" | "+s_game[2])
    print(s_game[3]+" | "+s_game[4]+" | "+s_game[5])
    print(s_game[6]+" | "+s_game[7]+" | "+s_game[8])
    



def p_input(x):
    print(x+" turn")
    # p = int(input("Enter position where to place (1 to 9): "))
    p = input("Enter position where to place (1 to 9): ")
    p = check_input(p)
    p = int(p)
    p = p-1
    if x=="P1":
        s_game[p]="X"
    else:
        s_game[p]="O"

    show_block()

def c_game():
    #check for row
    check=0
    if s_game[0]==s_game[1]==s_game[2]!="-":
        print("winner is "+s_game[0])
        check=1
    elif s_game[3]==s_game[4]==s_game[5]!="-":
        print("winner is "+s_game[3])
        check=1
    elif s_game[6]==s_game[7]==s_game[8]!="-":
        print("winner is "+s_game[6])
        check=1

    
    #check for column
    if s_game[0]==s_game[3]==s_game[6] != "-":
        print("winner is "+s_game[0])
        check=1
    elif s_game[1]==s_game[4]==s_game[7] != "-":
        print("winner is "+s_game[3])
        check=1
    elif s_game[2]==s_game[5]==s_game[8] != "-":
        print("winner is "+s_game[6])
        check=1

    #check for digonal
    if s_game[0]==s_game[4]==s_game[8] != "-":
        print("winner is "+s_game[0])
        check=1
    elif s_game[2]==s_game[4]==s_game[6] != "-":
        print("winner is "+s_game[2])
        check=1

    return check

    

def check_input(p):
    while p not in v_list:
        print("Invalid Position")
        p = input("Enter valid position where to place (1 to 9): ")
    return p



show_block()
for i in range(5):
    p_input("P1")
    x = c_game()
    if x==1:
        break
    # p_input("P1")

    if i==4 and x==0 :
        print("Game is Tied")
        break

    p_input("P2")
    y=c_game()
    if y==1:
        break
    # p_input("P2")

    


