import tkinter as tk
from tkinter import filedialog
from flashcards.data.serializer import Serializer
from flashcards.viewmodels.deck import Card, Deck
from flashcards.gui.navigation import NavigationFrame
from flashcards.gui.cards import FlashcardDeck, EditCard

WINDOW_WIDTH = 710
WINDOW_HEIGHT = 485

class Application(tk.Tk):
    def __init__(self, master=None): 
        super().__init__(master)
        self.wm_minsize(775, 450)
        self.focus_set()
        
        self.create_menu_bar()
        self.config(menu=self.menu_bar)
        
        # Frame controlling the flashcard
        self.cardframe = tk.Frame(master=self, width=WINDOW_WIDTH, height=WINDOW_HEIGHT//1.2, padx=5, pady=5)
        self.flashcard_deck = FlashcardDeck(Deck("yay", [Card("one", "1")]), master=self.cardframe)
        self.flashcard_deck.get_current_card()
        self.cardframe.pack(fill=tk.BOTH, expand=True)
        
        self.title(self.flashcard_deck.get_title())
        
        
        # Frame controlling navigation between flashcards
        self.nagivationframe = NavigationFrame(WINDOW_WIDTH, WINDOW_HEIGHT, 1, self.flashcard_deck.get_length(), self)
        
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
        self.file_menu.add_command(label="New", command=self.create_new_deck)
        self.file_menu.add_command(label="Open", command=self.open_deck)
        self.file_menu.add_command(label="Import")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Add a card", command=self.add_new_card)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        
    def add_new_card(self): 
        self.new_window = tk.Toplevel(self, padx=5, pady=5)
        self.new_window.title("Add New Card")
        self.frame = EditCard(self.new_window)
        self.frame.pack(fill=tk.BOTH, expand=True)
        save = tk.Label(master=self.new_window, text="Save", relief="groove")
        save.pack(fill=tk.BOTH, expand=True)
        save.bind("<ButtonRelease-1>", self._add_new_card)
        
    def _add_new_card(self, *args):
        question = self.frame.get_question_text()
        answer = self.frame.get_answer_text()
        self.flashcard_deck.add_new_card(question, answer)
        self.frame.destroy()
        self.new_window.destroy()
        self.nagivationframe.set_count(self.flashcard_deck.get_current_index(), self.flashcard_deck.get_length())
        Serializer.write(self.flashcard_deck.get_title(), self.flashcard_deck.get_deck())
        
    def create_new_deck(self):
        self.new_window = tk.Toplevel(self, padx=5, pady=5)
        self.new_window.title("Create New Deck")
        frame = tk.Frame(master=self.new_window)
        frame.pack(fill=tk.BOTH, expand=True)
        title = tk.Label(master=frame, text="Title: ")
        title.pack(fill=tk.BOTH, expand=True, side="left")
        self.entry = tk.Text(master=frame, width=25, height=1)
        self.entry.pack(fill=tk.BOTH, expand=True, side="right")
        self.entry.bind("<Key-Return>", self._create_new_deck)
    
    def _create_new_deck(self, *args):
        title = self.entry.get("1.0", "end-1c")
        if Serializer.create_new(title):
            self.entry.destroy()
            self.new_window.destroy()
            self.title(title)
            self.flashcard_deck.load_new_deck(title, [Card("", "")])
            self.nagivationframe.set_count(0, 0)
        else:
            self.entry.destroy()
            self.new_window.destroy()
            self.create_new_deck()
            frame2 = tk.Frame(master=self.new_window)
            frame2.pack(fill=tk.BOTH, expand=True)
            warning = tk.Label(master=frame2, text="That title already exists", fg="red")
            warning.pack(fill=tk.BOTH, expand=True)
            
    def open_deck(self, *args): 
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if path: 
            try: 
                title, cards = Serializer.open(path)
                self.flashcard_deck.load_new_deck(title, cards)
                self.title(title)
                self.nagivationframe.set_count(1, self.flashcard_deck.get_length())
            except:
                print("open failed")
        # print(path)
        
    def left_arrow_release(self, *args):
        if self.nagivationframe.left_arrow_release(): 
            self.flashcard_deck.previous_card()
            
    def right_arrow_release(self, *args):
        if self.nagivationframe.right_arrow_release():
            self.flashcard_deck.next_card()


if __name__ == "__main__":
    app = Application()
    app.mainloop()