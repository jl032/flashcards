import tkinter as tk
from flashcards.data.serializer import Serializer
from flashcards.viewmodels.deck import Card, Deck
from flashcards.gui.navigation import Arrow, NavigationFrame
from flashcards.gui.cards import Flashcard, FlashcardDeck, EditCard

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
        self.test = Flashcard("hello", "hi", master=self.cardframe)
        self.cardframe.pack(fill=tk.BOTH, expand=True)
        
        # Frame controlling navigation between flashcards
        self.nagivationframe = NavigationFrame(WINDOW_WIDTH, WINDOW_HEIGHT, 1, 5, self)
        
        # Bindings
        self.bind("<Key-space>", self.test.on_click)
        self.bind("<KeyRelease-space>", self.test.on_release)
        self.bind("<Key-Left>", self.nagivationframe.left_arrow.on_click)
        self.bind("<KeyRelease-Left>", self.nagivationframe.left_arrow_release)
        self.bind("<Key-Right>", self.nagivationframe.right_arrow.on_click)
        self.bind("<KeyRelease-Right>", self.nagivationframe.right_arrow_release)
        # self.bind("<Button-1>", self.on_click)
        # self.bind("<ButtonRelease-1>", self.on_release)
        # make arrows child objects of counter
        
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


if __name__ == "__main__":
    app = Application()
    app.mainloop()