SUITS = "\u2663 \u2665 \u2666 \u2660".split()
VALUES = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

deck = []
for suit in SUITS:
  for face in VALUES:
    deck.append(face+suit)

print(deck)

# How can we shuffle the deck?

# How can we deal the top two cards from the deck?
