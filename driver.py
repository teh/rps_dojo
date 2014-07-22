import itertools
import argparse
import collections

ITERATIONS = 10000
DEADLOCK = int(1e6)

def win(me, other):
    if me == other:
        return 'draw'
    if (me, other) in [('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')]:
        return 'win'
    return 'loss'


def play(player1, player2):
    outcomes = []
    i, deadlock = 0, DEADLOCK

    while i < ITERATIONS:
        choice1 = player1.choose()
        choice2 = player2.choose()

        assert choice1 in ('rock', 'paper', 'scissors')
        assert choice2 in ('rock', 'paper', 'scissors')

        player1.played(win(choice1, choice2), choice2)
        player2.played(win(choice2, choice1), choice1)

        if win(choice1, choice2) != 'draw':
            i += 1

        outcomes.append(win(choice1, choice2))

        deadlock -= 1
        if deadlock == 0:
            raise Exception("Bots drew for {} iterations.".format(DEADLOCK))

    return outcomes


def summarize(outcomes):
    return collections.Counter(outcomes)
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', nargs='+')
    args = parser.parse_args()

    players = []
    for path in args.paths:
        vars = {}
        execfile(path, vars)
        
        player = vars.get('Player')
        if player is None:
            parser.error("Could not find 'Player' class in {}".format(path))
        players.append((player, path))

    if len(players) < 2:
        parser.error("Not enough players (need more than one).")

    for (p1_class, p1_name), (p2_class, p2_name) in itertools.combinations(players, 2):
        p1, p2 = p1_class(), p2_class()

        print p1_name, p2_name, summarize(play(p1, p2))

if __name__ == '__main__':
    main()
