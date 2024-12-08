import tkinter as tk
from flashcards.viewmodels.deck import Deck, Card

class FlashcardDeck:
    def __init__(self, deck: Deck, master=None):
        self.deck = deck
        self.card = tk.Label(master, text=self.deck.get_current_card().question, width=100, height=25, relief="raised", bg="white")
        self.card.pack(fill=tk.BOTH, expand=True)
        self.card.bind("<Button-1>", self.on_click)
        self.card.bind("<ButtonRelease-1>", self.on_release)
        self.click = True
    
    def get_deck(self) -> Deck:
        return self.deck
    
    def get_current_card(self) -> Card:
        self.card["text"] = self.deck.get_current_card().question
        return self.deck.get_current_card()
    
    def next_card(self) -> Card:
        self.card["text"] = self.deck.get_next_card().question
        return self.deck.get_current_card()
    
    def previous_card(self) -> Card: 
        self.card["text"] = self.deck.get_previous_card().question
        return self.deck.get_current_card()
    
    def flip(self, *args) -> None:
        self.card["relief"] = "sunken"
        if self.card["text"] == self.get_current_card().question: 
            self.card["text"] = self.get_current_card().answer
        elif self.card["text"] == self.get_current_card().answer: 
            self.card["text"] = self.get_current_card().question
            
    def get_title(self) -> str:
        return self.deck.get_title()
    
    def get_length(self) -> int:
        return self.deck.get_length()
    
    def load_new_deck(self, title: str, cards: list[Card]) -> None:
        self.deck = Deck(title, cards)
        try:
            self.card["text"] = self.deck.get_current_card().question
        except:
            self.card["text"] = ""
        
    def on_click(self, *args) -> None:
        if self.click:
            self.flip(*args)
            self.click = False
            
    def on_release(self, *args) -> None:
        self.card["relief"] = "raised"
        self.click = True
        


class EditCard(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.question_frame = tk.Frame(master=self, relief="groove", padx=10, pady=10)
        self.question_frame.pack(side="left", fill=tk.BOTH, expand=True)
        self.question_label = tk.Label(master=self.question_frame, text="Question: ")
        self.question_label.pack(fill=tk.BOTH, expand=True)
        self.question_entry = tk.Text(master=self.question_frame, width=25, height=3)
        self.question_entry.pack(fill=tk.BOTH, expand=True)
        
        self.answer_frame = tk.Frame(master=self, relief="groove", padx=10, pady=10)
        self.answer_frame.pack(side="right", fill=tk.BOTH, expand=True)
        self.answer_label = tk.Label(master=self.answer_frame, text="Answer: ")
        self.answer_label.pack(fill=tk.BOTH, expand=True)
        self.answer_entry = tk.Text(master=self.answer_frame, width=25, height=3)
        self.answer_entry.pack(fill=tk.BOTH, expand=True)
        
        
    def get_question_text(self, *args):
        return self.question_entry.get("1.0", "end-1c")
    
    def get_answer_text(self, *args): 
        return self.answer_entry.get("1.0", "end-1c")