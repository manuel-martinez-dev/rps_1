from flask import Flask, render_template, request, jsonify, session
import random
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from game import Game, HumanPlayer, RandomPlayer, CyclePlayer, ReflectPlayer, RockPlayer

app = Flask(
    __name__,
    template_folder='../templates',
    static_folder='../static'
)
app.secret_key = os.environ.get('SECRET_KEY', 'change-me-in-production')

moves = ['rock', 'paper', 'scissors']


def get_opponent():
    behaviors = [RockPlayer(), RandomPlayer(), CyclePlayer(), ReflectPlayer()]
    return random.choice(behaviors)


@app.route('/')
def index():
    session.clear()
    session['score_player'] = 0
    session['score_ai'] = 0
    session['round'] = 0
    session['opponent'] = random.choice(['RockPlayer', 'RandomPlayer', 'CyclePlayer', 'ReflectPlayer'])
    session['last_ai_move'] = random.choice(moves)
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    data = request.get_json()
    player_move = data.get('move', '').lower()

    if player_move not in moves:
        return jsonify({'error': 'Invalid move'}), 400

    opponent_type = session.get('opponent', 'RandomPlayer')
    last_ai_move = session.get('last_ai_move', random.choice(moves))

    ai_move = get_ai_move(opponent_type, last_ai_move, player_move)

    result = resolve(player_move, ai_move)

    if result == 'win':
        session['score_player'] = session.get('score_player', 0) + 1
    elif result == 'lose':
        session['score_ai'] = session.get('score_ai', 0) + 1

    session['round'] = session.get('round', 0) + 1
    session['last_ai_move'] = ai_move

    current_round = session['round']
    game_over = current_round >= 10

    final_result = None
    if game_over:
        if session['score_player'] > session['score_ai']:
            final_result = 'YOU ARE TRIUMPHANT!'
        elif session['score_ai'] > session['score_player']:
            final_result = 'JOHNNY5 is VICTORIOUS!'
        else:
            final_result = 'DRAW!'

    return jsonify({
        'player_move': player_move,
        'ai_move': ai_move,
        'result': result,
        'score_player': session['score_player'],
        'score_ai': session['score_ai'],
        'round': current_round,
        'game_over': game_over,
        'final_result': final_result,
    })


def get_ai_move(opponent_type, last_ai_move, player_move):
    if opponent_type == 'RockPlayer':
        return 'rock'
    elif opponent_type == 'RandomPlayer':
        return random.choice(moves)
    elif opponent_type == 'ReflectPlayer':
        return last_ai_move
    elif opponent_type == 'CyclePlayer':
        idx = moves.index(last_ai_move) if last_ai_move in moves else 0
        return moves[(idx + 1) % len(moves)]
    return random.choice(moves)


def resolve(player, ai):
    if player == ai:
        return 'draw'
    if (
        (player == 'rock' and ai == 'scissors') or
        (player == 'scissors' and ai == 'paper') or
        (player == 'paper' and ai == 'rock')
    ):
        return 'win'
    return 'lose'


if __name__ == '__main__':
    app.run(debug=False)
