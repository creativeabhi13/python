class Card:
    suit_names=["clubs","diamond","hearts","spades"]
    rank_names=["None","Ace","2","3","4","5","6","7","8","9","jack","Queen","King"]
    def __init__(self,suit=0,rank=2):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
c=Card(1,12)
print(c)
