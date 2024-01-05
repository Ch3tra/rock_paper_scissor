from flask import Blueprint, request, jsonify
import random

handle = Blueprint('handle', __name__)


@handle.route('/getresult')
def getresult():
    user_choice = request.args.get('user_choice', default='', type=str)
    choices = ['rock', 'paper', 'scissor']
    com_choice = random.choice(choices)

    # Determine the winner
    if user_choice == com_choice:
        result = 'It\'s a Tie'
    elif (user_choice == 'rock' and com_choice == 'scissor') or \
            (user_choice == 'paper' and com_choice == 'rock') or \
            (user_choice == 'scissors' and com_choice == 'paper'):
        result = 'You Win!'
    else:
        result = 'Computer Wins!'

    return jsonify(result=result, com_choice=com_choice)