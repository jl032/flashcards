import tkinter as tk
from flashcards.data.serializer import Serializer
from flashcards.viewmodels.deck import Card, Deck
from flashcards.gui.navigation import NavigationFrame
from flashcards.gui.cards import FlashcardDeck, EditCard

WINDOW_WIDTH = 710
WINDOW_HEIGHT = 485

class Application(tk.Tk):
    def __init__(self, master=None): 
        super().__init__(master)
        self.title("Flashcards")
        self.wm_minsize(775, 450)
        self.focus_set()
        
        self.create_menu_bar()
        self.config(menu=self.menu_bar)
        
        # Frame controlling the flashcard
        self.cardframe = tk.Frame(master=self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT//1.2, padx=5, pady=5)
        self.flashcard_deck = FlashcardDeck(5, master=self.cardframe)
        self.flashcard_deck.get_current_card()
        self.cardframe.pack(fill=tk.BOTH, expand=True)
        
        
        # Frame controlling navigation between flashcards
        self.nagivationframe = NavigationFrame(WINDOW_WIDTH, WINDOW_HEIGHT, 1, 5, self)
        
        # Bindings
        self.bind("<Key-space>", self.flashcard_deck.on_click)
        self.bind("<KeyRelease-space>", self.flashcard_deck.on_release)
        self.bind("<Key-Left>", self.nagivationframe.left_arrow.on_click)
        self.bind("<KeyRelease-Left>", self.left_arrow_release)
        self.bind("<Key-Right>", self.nagivationframe.right_arrow.on_click)
        self.bind("<KeyRelease-Right>", self.right_arrow_release)
        
    def create_menu_bar(self) -> None:
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
        
    def create_new_card(self): 
        new_window = tk.Toplevel(self)
        new_window.title("Create New Card")
        frame = EditCard(new_window)
        frame.pack(fill=tk.BOTH, expand=True)
        
    def left_arrow_release(self, *args):
        if self.nagivationframe.left_arrow_release(): 
            self.flashcard_deck.previous_card()
            
    def right_arrow_release(self, *args):
        if self.nagivationframe.right_arrow_release():
            self.flashcard_deck.next_card()


if __name__ == "__main__":
    app = Application()
    app.mainloop()