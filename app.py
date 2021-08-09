import json
import re

from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, join_room, leave_room, emit

from flask_session import Session
from create_board import *

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

socketio = SocketIO(app, cors="*", manage_session=False)

op = play_board()
turn = 1
players = []


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        username = request.form['username']
        room = request.form['room']
        # Store the data in session
        session['username'] = username
        session['room'] = room
        return render_template('chat.html', session=session)
    else:
        if session.get('username') is not None:
            return render_template('chat.html', session=session)
        else:
            return redirect(url_for('index'))


@socketio.on('join', namespace='/chat')
def join(message):
    room = session.get('room')
    players.append(session.get('username'))
    print(session.get('username') + ' - Player has entered')
    join_room(room)
    test = display_board(op)

    if len(players) >= 2:
        # board = play_board()
        emit('status', {'msg': session.get('username') + ' Lets Start Playing the Game '}, room=room)
        emit('message', {'msg': test}, room=room)
        emit('message', {'msg': session.get('username') + ' : Please select between 1 and 9 '}, room=room)
    if len(players) == 1:
        emit('status', {'msg': session.get('username') + ' , Please wait for the Player 2 to Join the room. '},
             room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    room = session.get('room')
    inp = (message['msg'])
    print(players)
    # FUnction gaming...

    global op, turn
    x, y, ms = player_move(message['msg'], op, turn)
    op = x
    turn = y
    test = display_board(op)

    if re.search('Player 2', ms):
        ms = ms.replace('Player 2', players[1])

    elif re.search('Player 1', ms):
        ms = ms.replace('Player 1', players[0])

    emit('message', {'msg': inp + ms}, room=room)
    emit('message', {'msg': test}, room=room)

    print('App turn : ', turn)

    if turn % 2 == 0:
        print(ms)

        if ms.find('full') == -1:
            emit('message', {'msg': 'Hey ' + players[0] + ' : Please select between 1 and 9 '}, room=room)
        else:
            emit('message', {'msg': 'Hey ' + players[0] + ' : Please select between 1 and 9 '}, room=room)
    else:
        if ms.find('full') == -1:
            emit('message', {'msg': 'Hey ' + players[1] + ' : Please select between 1 and 9 '}, room=room)
        else:
            emit('message', {'msg': 'Hey ' + players[1] + ' : Please select between 1 and 9 '}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    username = session.get('username')
    leave_room(room)
    session.clear()
    emit('status', {'msg': username + ' has left the room.'}, room=room)


if __name__ == '__main__':
    print('Starting the Game App...')
    socketio.run(app)
