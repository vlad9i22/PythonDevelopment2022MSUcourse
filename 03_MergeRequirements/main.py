from bullscows import bullscows
from bullscows import ask
from bullscows import inform
from bullscows import gameplay
import sys


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        words = [i.strip() for i in file.readlines()]
        word_size = 5
        if len(sys.argv) >= 3:
            word_size = sys.argv[2]
        words = [word for word in words if len(word) == word_size]
        gameplay(ask, inform, words)