#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
import sys
from colorama import init
from colorama import Fore, Back, Style
print(Fore.RED, Style.DIM + "Are you ready to play ROCK, PAPER, SCISSORS?"'\n')
print(Style.RESET_ALL)
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class AllRocker(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            chose = input("whatcha u gonna play?:"'\n')
            if chose in moves:
                return chose


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
            print(Fore.BLUE + "YOU Have won!")
        elif beats(move2, move1):
            self.score2 += 1
            print(Fore.RED + "JOHNNY5 Has won!")
        else:
            print(Fore.YELLOW + "DRAW!!")
#        print(f"Player 1: {self.score1} Player 2: {self.score2}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def more_rounds(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.score1 += 1
            print(Fore.BLUE + "YOU Have won!")
        elif beats(move2, move1):
            self.score2 += 1
            print(Fore.RED + "JOHNNY5 Has won!")
        else:
            print(Fore.YELLOW + "DRAW!!")
#        print(f"Player 1: {self.score1} Player 2: {self.score2}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!"'\n')
        for round in range(1):
            print(f"Round {round}:")
            self.play_round()
        print(Fore.WHITE + f"YOU: {self.score1} JOHNNY5: {self.score2}")
        if self.score1 > self.score2:
            print(Fore.GREEN + "YOU ARE TRIUMPHANT!")
        elif self.score1 < self.score2:
            print(Fore.BLUE + "JOHNNY5 is VICTORIOUS!")
        else:
            print(Fore.YELLOW + "Outta breath?-DRAW!!")
        print('\n'"Game over!")

        mode = input("play longer?[yes,no]"'\n')
        while True:
            if mode == 'no':
                print("Until next time...")
                sys.exit(0)
            elif mode == 'yes':
                for round in range(5):
                    print(f"Round {round}:")
                    self.more_rounds()
                print(Fore.WHITE + f"YOU:{self.score1} JOHNNY5:{self.score2}")
                if self.score1 > self.score2:
                    print(Fore.GREEN + "YOU ARE TRIUMPHANT!")
                elif self.score1 < self.score2:
                    print(Fore.BLUE + "JOHNNY5 is VICTORIOUS!")
                else:
                    print(Fore.YELLOW + "Outta breath?-DRAW!!")
                print('\n'"Game over!")
                break
#                sys.exit(0)
            else:
                print("YOU should have chosen wisely - GOODBYE!!!")
                sys.exit(0)


if __name__ == '__main__':
    behaviors = [AllRocker(), RandomPlayer(), CyclePlayer()]
    behavior = random.choice(behaviors)
    human = HumanPlayer()
    game = Game(human, behavior)
    game.play_game()

#    game.play_game()
#    print(help())
