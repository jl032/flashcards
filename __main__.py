import tkinter as tk
# import tkinter.ttk as ttk

# from deck import Card, Deck

WINDOW_WIDTH = 710
WINDOW_HEIGHT = 485

class Application(tk.Frame):
    def __init__(self, master=None): 
        super().__init__(master)
        self.pack(fill=tk.BOTH, expand=True)
        self.focus_set()
        
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


class Arrow(tk.Label):
    def __init__(self, direction, master=None):
        self.direction = direction
        super().__init__(master, text=self.get_arrow(), relief="groove")
        self.pack(fill=tk.BOTH, side=self.direction, expand=True)
        self.get_arrow()
        self.click = True
        self.bind("<Button-1>", self.on_click)
        self.bind("<ButtonRelease-1>", self.on_release)
        
    def get_arrow(self) -> str:
        if self.direction == "left":
            return "<-"
        else: 
            return "->"
            
    def on_click(self, *args) -> None:
        if self.click: 
            self["relief"] = "solid"
            print("go " + self.direction)
            self.click = False
        
    def on_release(self, *args) -> None:
        self["relief"] = "groove"
        self.click = True
        
        
class Counter(tk.Label):
    def __init__(self, current, total, master=None): 
        self.current = current
        self.total = total
        super().__init__(master, text=self.get_label(), relief="groove")
        self.pack(fill=tk.BOTH, side="left", expand=True)
        
    def get_label(self) -> str:
        return f"{self.current}/{self.total}"
    
        
app = Application()
app.master.title("Flashcards")
app.mainloop()