import random

class Player:

    def choose(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def played(self, outcome, other_played):
        """
        outcome will be 'win', 'draw' or 'loss'
        other_played will be 'rock', 'paper' or 'scissors'
        """
        pass