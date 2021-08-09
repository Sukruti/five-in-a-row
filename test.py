#Validation of room and users
import numpy as np

room = 'Test'
players = ['sukruti' , 'abhi']
game_room = {}
print(game_room)

if len(players) == 2 :
    game_room[room] = players

print(game_room)

'''
room = 'Test'
if room in game_room.keys():
    print('Room is full please select the other room...')

print(game_room)
'''


def is_board_full(board):
    return True

board = np.zeros((6,9), dtype=int)
board[1][2] = 2
print(board)
# Count non zero items in array




