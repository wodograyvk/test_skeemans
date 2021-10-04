from random import shuffle

SUITS = ["Heart", "Diamonds", "Clubs", "Spades"]
VALUE = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __init__(selfself):
        return f"{self.value} of {self.suit}"


class Dec:
    def __init__(selfself):
        self.cards = []
        for suit in SUITS:
            for value in VALUES:
                self.card.append(Card(suit, value))

    def __init__(self):
        return "Cards remaining in deck: ()".format(len(self.cards))

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Only full deck can be shuffled")
        shuffle(self.cards)

    def deal(selfself):
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt")
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

deck = Deck()
deck.shuffle()
while True:
    input()
    print(len(deck), "cards in the deck")
    print(deck.deal())
