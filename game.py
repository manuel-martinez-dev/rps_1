import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.chose = random.choice(moves)

    def move(self):
        return self.chose

    def learn(self, my_move, their_move):
        self.chose = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.choices = 0

    def move(self):
        return moves[self.choices]

    def learn(self, my_move, their_move):
        if self.choices == 2:
            self.choices = 0
        else:
            self.choices += 1


class HumanPlayer(Player):
    def move(self):
        while True:
            chose = input("whatcha u gonna play?:\n")
            if chose in moves:
                return chose


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            self.score1 += 1
            print("YOU Have won!")
        elif beats(move2, move1):
            self.score2 += 1
            print("JOHNNY5 Has won!")
        else:
            print("DRAW!!")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
