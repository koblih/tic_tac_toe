# print board

import collections

a = collections.OrderedDict()
a[1] = '*'
a[2] = '*'
a[3] = '*'
b = collections.OrderedDict()
b[4] = '*'
b[5] = '*'
b[6] = '*'
c = collections.OrderedDict()
c[7] = '*'
c[8] = '*'
c[9] = '*'

board = [a,b,c]

def print_legend():
    print 'Legend'
    for row in board:
        print row.keys()
  
def print_board():
    print 'Board:'
    for row in board:
        print row.values()
        
print_legend()
print_board()


# lists of values for winning
# options = []
# 
def winner():
    row_a = dict(a).values()
    row_b = dict(b).values()
    row_c = dict(c).values()
   
    column1 = dict(a)[1],dict(b)[4],dict(c)[7]
    column_1 = []
    for item in column1:
      column_1.append(item)
    column2 = dict(a)[2],dict(b)[5],dict(c)[8]
    column_2 = []
    for item in column2:
      column_2.append(item)
    column3 = dict(a)[3],dict(b)[6],dict(c)[9]
    column_3 = []
    for item in column3:
      column_3.append(item)
    
    diagonal1 = dict(a)[1],dict(b)[5],dict(c)[9]
    diagonal_1 = []
    for item in diagonal1:
      diagonal_1.append(item)
    diagonal2 = dict(a)[3],dict(b)[5],dict(c)[7]
    diagonal_2 = []
    for item in diagonal2:
      diagonal_2.append(item)
    
    options = [row_a,row_b,row_c,column_1,column_2,column_3,diagonal_1,diagonal_2]  
    
    for option in options:
        if all(item == option[0] for item in option) and any(item != '*' for item in option):
            return True
        else:
            return False
        
# get list of keys from the board (list of dictionaries)
positions = []

for row in board:
    for item in row:
        positions.append(item)
#print positions

# Get player's input & reassign the dictionary value
def playera_input():
    while True:
        answer = raw_input('Player A: Please select one of the available positions on the board: ')  
        if not answer.isdigit():
            print 'Please enter a number.'
            continue
        elif int(answer) not in range(1,10):
            print 'Outside of board.'
            continue
        else:
            if int(answer) in positions:
                for row in board:
                    for item in row:
                        if item == int(answer):
                            row[item] = 'X'
                print_board()           
                positions.remove(int(answer))
                print positions
            else:
                print 'Already taken'
                continue
        break
    winner()
    
def playerb_input():
    while True:
        answer = raw_input('Player B: Please select one of the available positions on the board: ')   
        if not answer.isdigit():
            print 'Please enter a number.'
            continue
        elif int(answer) not in range(1,10):
            print 'Outside of board.'
            continue
        else:
            if int(answer) in positions:
                for row in board:
                    for item in row:
                        if item == int(answer):
                            row[item] = 'O'
                print_board()           
                positions.remove(int(answer))
                print positions
            else:
                print 'Already taken'
                continue
        break
    winner()
    
#use built-in function all(x==myList[0] for x in myList)
#def same(items):
    #if all(item == items[0] for item in items) and any(item != '*' for item in items):
        #return True
       
def ttt():
    while not winner():
        playera_input()
        if not winner():
            pass
        else:
            print 'You have won!'
            break
        playerb_input()
        if not winner():
            pass
        else:
            print 'You have won!'
            break
            
    
ttt()


#clear_output()

    




    


