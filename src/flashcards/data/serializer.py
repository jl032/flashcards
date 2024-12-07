import os
from flashcards.viewmodels.deck import Card, Deck

class Serializer: 
    @classmethod
    def write(cls, path: str, flashcards: Deck) -> bool: 
        path = "data/" + path
        if not os.path.isfile(path): 
            with open(path, mode="w") as file:
                for card in flashcards.get_deck(): 
                    file.write(f"{card.question} - {card.answer}\n")
            return True
        else:
            return False
        
    @classmethod
    def open(cls, path: str) -> Deck:
        path = "data/" + path
        deck = Deck(0)
        if os.path.isfile(path):
            with open(path, mode="r") as file: 
                for line in file: 
                    index = line.index(" - ")
                    question = line[:index]
                    answer = line[index+1:]
                    deck.add_card(question, answer)
            return deck