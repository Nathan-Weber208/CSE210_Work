class Deck:
    """
    A collection of 52 cards with an unpulled deck and a discard pile.
        self.unpulled - all cards that have not been pulled yet
        self.discard - all pulled cards
        self.topcard - the most recently pulled card
    methods
        self.pull - choose a random card from unpulled card, 
                    make self.topcard = that card, remove it from unpulled 
                    and add it to discard
    """
    def __init__(self):
        pass
    
    def pull(self):
        pass

def main():
    pass

if __name__ == "__main__":
    main()

class Card:
    """
    A single card with a suit and a deck.
    attributes:
        self.suit
        self.number
    
    """
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def is_lower(self, card):
        pass

    def is_higher(self, card):
        pass
