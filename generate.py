from ast import main
import random

cards = ["jack","queen","king"]

def main():
    print(random.choices(cards, weights=[100, 0, 0], k=2))


if __name__ == "__main__":
    main()
    