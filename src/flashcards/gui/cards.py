import tkinter as tk
from flashcards.gui.navigation import NavigationFrame

class FlashcardDeck:
    def __init__(self, count: int = 5, master=None):
        self.count = count
        self.current = 0
        self.deck = self.initialize_deck()
        self.card = tk.Label(master, text=self.deck[self.current][0], width=100, height=25, relief="raised")
        self.card.pack(fill=tk.BOTH, expand=True)
        self.card.bind("<Button-1>", self.on_click)
        self.card.bind("<ButtonRelease-1>", self.on_release)
        self.click = True
        
        
    def initialize_deck(self) -> list[tuple]: 
        # return [Flashcard(f"{_}", f"{_+1}") for _ in range(self.count)]
        return [
            ("one", "1"), 
            ("two", "2"),
            ("three", "3"),
            ("four", "4"), 
            ("five", "5")
        ]
    
    def get_deck(self) -> list[tuple]:
        return self.deck
    
    def get_current_card(self) -> tuple:
        return self.deck[self.current]
    
    def next_card(self) -> tuple:
        if self.current+1 < self.count:
            self.current += 1
        self.card["text"] = self.deck[self.current][0]
        return self.deck[self.current]
    
    def previous_card(self) -> tuple: 
        if self.current > 0: 
            self.current -= 1
        self.card["text"] = self.deck[self.current][0]
        return self.deck[self.current]
    
    def flip(self, *args) -> None:
        self.card["relief"] = "sunken"
        if self.card["text"] == self.get_current_card()[0]: 
            self.card["text"] = self.get_current_card()[1]
        elif self.card["text"] == self.get_current_card()[1]: 
            self.card["text"] = self.get_current_card()[0]
        
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
    
    
class EditDeck(tk.Frame):
    def __init__(self, count: int, master=None):
        super().__init__(master)
        