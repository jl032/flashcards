import tkinter as tk

class Flashcard(tk.Label):
    def __init__(self, question, answer, width=100, height=25, master=None):
        self.master = master
        self.question = question
        self.answer = answer
        super().__init__(master, text=self.question, width=width, height=height, relief="raised")
        self.pack(fill=tk.BOTH, expand=True)
        self.click = True
        self.bind("<Button-1>", self.on_click)
        self.bind("<ButtonRelease-1>", self.on_release)
        
    def flip(self, *args) -> None:
        self["relief"] = "sunken"
        if self["text"] == self.question: 
            self["text"] = self.answer
        elif self["text"] == self.answer: 
            self["text"] = self.question
        
    def on_click(self, *args) -> None:
        if self.click:
            self.flip(*args)
            self.click = False
            
    def on_release(self, *args) -> None:
        self["relief"] = "raised"
        self.click = True
        
        
class FlashcardDeck:
    def __init__(self, count: int = 5):
        self.count = count
        self.deck = self.initialize_cards()
        self.current = 0
        
    def initialize_cards(self) -> list[Flashcard]: 
        return [Flashcard("", "") for _ in range(self.count)]
        


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
        