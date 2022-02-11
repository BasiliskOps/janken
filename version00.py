import random, sys

print('ROCK, PAPER, SCISSORS')

wins = 0
losses = 0
ties = 0
#variables for score keeping

#Main game loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # player input loop
        print('Make your move: (r)ock (p)aper (s)cissors or (q)uit')
        