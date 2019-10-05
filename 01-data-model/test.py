from frenchdeck import FrenchDeck, Card
from random import choice

def get_first_card(deck: FrenchDeck) -> Card:
	 return deck[0]

def get_last_card(deck: FrenchDeck) -> Card:
	 return deck[len(deck)-1]	 

def get_suite(suite: str, deck: FrenchDeck) -> Card:
	return [card for card in deck if card[1]==suite]

def get_same_card(card_name: str, deck: FrenchDeck) -> Card:
	return [card for card in deck if card[0]==card_name]

def get_random_card_from_suite(suite: str, deck: FrenchDeck) -> Card:
	return choice([card for card in deck if card[1]==suite])

def spades_high(card):
	rank_value = FrenchDeck.ranks.index(card.rank)
	print(rank_value)
	print(len(suit_values))
	print(suit_values[card.suit])
	return rank_value * len(suit_values) + suit_values[card.suit]

if __name__ == '__main__':
	deck = FrenchDeck()
	suit_values = dict(пики=3, бубна=2, трефа=1, черви=0)
	print(spades_high(Card('K', 'пики')))

	# print(f'Deck contains {len(deck)} cards')
	# print(get_first_card(deck))
	# print(get_last_card(deck))
	# print(get_suite('пики', deck))
	# print(get_same_card('J', deck))
	# print(get_random_card_from_suite('черви', deck))

