import os
from flashcards.viewmodels.deck import Card, Deck

class Serializer: 
    @classmethod
    def write(cls, path: str, flashcards: Deck) -> bool: 
        path = "src/flashcards/data/" + path + ".txt"
        with open(path, mode="w") as file:
            for card in flashcards.get_deck(): 
                file.write(f"{card.question} ~`|+<&$>/||`=_# {card.answer}\n")
        return True
        
    @classmethod
    def open(cls, path: str) -> tuple[str, list[Card]]:
        # path = "src/flashcards/data/" + path
        title = path[path.index("src/flashcards/data/")+20:-4]
        deck = []
        if os.path.isfile(path):
            with open(path, mode="r") as file: 
                for line in file: 
                    index = line.index(" ~`|+<&$>/||`=_# ")
                    question = line[:index]
                    answer = line[index+17:]
                    deck.append(Card(question, answer))
            return (title, deck)
        
    @classmethod
    def create_new(cls, title: str) -> bool:
        path = "src/flashcards/data/" + title + ".txt"
        if os.path.isfile(path):
            return False
        else:
            with open(path, mode="w") as file:
                file.write("")
            return True