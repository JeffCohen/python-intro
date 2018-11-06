# Game of Blackjack
# https://www.youtube.com/watch?v=TtAipRjRu4E
#
# Basic Version:
#
# - Human player gets the first two cards
# - Human plays the rest of their hand
# - Human can choose to "stand" (stop taking cards) anytime
# - Then computer gets next two cards
# - Computer must take cards score < 17
# - Computer must stand when score >= 17
# - Aces always count as 11
# - A player loses immediately if their score is becomes more than 21
# - Human player wins immediately when their score becomes exactly 21
# - If both human and computer stand with scores less than 21,
#   the winner is the one with the higher score.
#   If scores are equal, nobody wins.

# Deluxe Version:
#
# - Aces only count as 1 if counting as 11 would have made the score > 21
# - Initally, human and dealer both get two cards, with one dealer card face down
# - Dealing cards to the cmputer should have a dramatic, 4-second delay
# - Allow the user to play as many games as they want
