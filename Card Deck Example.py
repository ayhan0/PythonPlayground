from collections import namedtuple
_suits = ('Spades','Hearths','Diamonds','Clubs')
_ranks = tuple(range(2,11))+tuple('JKQA')
Card = namedtuple('Card','rank suit')
class CardDeck:
    def __init__(self):
        self.length= len(_suits)*len(_ranks)
    
    def __len__(self):
        return self.length
    def __iter__(self):
        return self.CardDeckIterator(self.length)
    class CardDeckIterator:
        def __init__(self,length):
            self.length = length
            self.i=0
        def __iter__(self):
            return self
        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                suit = _suits[self.i //len(_ranks)]
                rank = _ranks[self.i % len(_ranks)]
                self.i+=1
                return Card(rank,suit)
deck = CardDeck()
for card in deck:
    print(card)

# ********* EASİER WAY WİTH YİELD *****
from collections import namedtuple
suits = ('Spades','Hearths','Diamonds','Clubs')
Ranks = tuple(range(2,11))+tuple('JKQA')
Card = namedtuple('Card','rank suit')
def card_gen():
    for suit in suits:
        for rank in ranks:
            yield(Card(rank,suit))
for card in card_gen():
    print(card)
