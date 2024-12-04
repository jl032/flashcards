class Card: 
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer
        
    def edit(self, question: str, answer: str) -> None: 
        self.question = question
        self.answer = answer


class Deck:
    def __init__(self, count: int = 5):
        self.count = count
        self.deck = self.initialize_cards()
        self.current = 0
        
    def initialize_cards(self) -> list[Card]: 
        return [Card("", "") for _ in range(self.count)]
    
    def get_current_card(self) -> Card:
        return self.deck[self.current]
    
    def edit_current_card(self, question: str, answer: str) -> None: 
        self.deck[self.current].edit(question, answer)
    
    def get_next_card(self) -> Card:
        if self.current+1 < self.count:
            self.current += 1
        return self.get_current_card()
    
    def get_previous_card(self) -> Card: 
        if self.current-1 >= 0: 
            self.current -= 1
        return self.get_current_card()
    
    def get_deck(self) -> list[Card]: 
        return self.deck
    
    def add_card(self, question: str = "", answer: str = "") -> None: 
        self.count += 1
        self.deck.append(Card(question, answer))