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
        player_move = input()
        if player_move == 'q':
            sys.exit() # Terminate the program
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break
        print('Enter r, p, s, or q.')

    # conditional logic to display player choice:
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # conditional statements to display randomized computer:
    rando_num = random.randint(1, 3)
    if rando_num == 1:
        com_move = 'r'
        print('ROCK')
    elif rando_num == 2:
        com_move = 'p'
        print('PAPER')
    elif rando_num == 3:
        com_move = 's'
        print('SCISSORS')

    # outcome and record
    if player_move == com_move:
        print('TIE')
        ties = ties + 1
    elif player_move == 'r' and com_move == 's':
        print('JANKEN')
        wins = wins + 1
    elif player_move == 'p' and com_move == 'r':
        print('JANKEN')
        wins = wins + 1
    elif player_move == 's' and com_move == 'p':
        print('JANKEN')
        wins = wins + 1
    elif player_move == 'r' and com_move == 'p':
        print('DEFEATED')
        losses = losses + 1
    elif player_move == 'p' and com_move == 's':
        print('DEFEATED')
        losses = losses + 1
    elif player_move == 's' and com_move == 'r':
        print('DEFEATED')
        losses = losses + 1
