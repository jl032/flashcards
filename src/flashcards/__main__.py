import tkinter as tk
from flashcards.data.serializer import Serializer
from flashcards.viewmodels.deck import Card, Deck
from flashcards.gui.navigation import Arrow, Counter

WINDOW_WIDTH = 710
WINDOW_HEIGHT = 485

class Application(tk.Tk):
    def __init__(self, master=None): 
        super().__init__(master)
        self.title("Flashcards")
        self.wm_minsize(775, 450)
        self.focus_set()
        
        self.menu_bar = tk.Menu()
        
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New")
        self.file_menu.add_command(label="Open")
        self.file_menu.add_command(label="Open from File")
        self.file_menu.add_command(label="Import")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Add a card", command=self.create_new_card)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        
        self.config(menu=self.menu_bar)
        
        # Frame controlling the flashcard
        self.cardframe = tk.Frame(master=self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT//1.2, padx=5, pady=5)
        self.test = Flashcard("hello", "hi", master=self.cardframe)
        self.cardframe.pack(fill=tk.BOTH, expand=True)
        
        # Frame controlling navigation between flashcards
        self.nagivationframe = tk.Frame(master=self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT//6.5, padx=5, pady=5)
        self.left_arrow = Arrow("left", master=self.nagivationframe)
        self.right_arrow = Arrow("right", master=self.nagivationframe)
        self.counter = Counter(1, 1, master=self.nagivationframe)
        self.nagivationframe.pack(fill=tk.BOTH, expand=True)
        
        # Bindings
        self.bind("<Key-space>", self.test.on_click)
        self.bind("<KeyRelease-space>", self.test.on_release)
        self.bind("<Key-Left>", self.left_arrow.on_click)
        self.bind("<KeyRelease-Left>", self.left_arrow.on_release)
        self.bind("<Key-Right>", self.right_arrow.on_click)
        self.bind("<KeyRelease-Right>", self.right_arrow.on_release)
        
    def create_new_card(self): 
        new_window = tk.Toplevel(self)
        new_window.title("Create New Card")
        frame = EditCard(new_window)
        frame.pack(fill=tk.BOTH, expand=True)

        
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
            print(*args)
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
    

if __name__ == "__main__":
    app = Application()
    app.mainloop()