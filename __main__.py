import tkinter as tk
import tkinter.ttk as ttk

WINDOW_WIDTH = 710

class Application(tk.Frame):
    def __init__(self, master=None): 
        super().__init__(master)
        self.grid()
        self.focus_set()
        
        # Frame controlling the flashcard
        self.cardframe = tk.Frame(master=self, width=WINDOW_WIDTH, height=400, padx=5, pady=5)
        self.test = Flashcard("hello", "hi", master=self.cardframe)
        self.cardframe.grid()
        
        # Frame controlling navigation between flashcards
        self.nagivationframe = tk.Frame(master=self, width=WINDOW_WIDTH, height=75, padx=5, pady=5)
        self.nagivationframe.grid()
        
        # Bindings
        self.bind("<Button-1>", self.test.on_click)
        self.bind("<Key-space>", self.test.on_click)
        self.bind("<ButtonRelease-1>", self.test.on_release)
        self.bind("<KeyRelease-space>", self.test.on_release)

        
class Flashcard(tk.Label):
    def __init__(self, question, answer, width=100, height=25, master=None):
        self.master = master
        self.question = question
        self.answer = answer
        super().__init__(master, text=self.question, width=width, height=height, relief="raised")
        self.grid()
        
    def flip(self, *args):
        self["relief"] = "sunken"
        if self["text"] == self.question: 
            self["text"] = self.answer
        elif self["text"] == self.answer: 
            self["text"] = self.question
        
    def on_click(self, *args):
        self.flip(*args)
            
    def on_release(self, *args):
        self["relief"] = "raised"
    
    
        
app = Application()
app.master.title("Flashcards")
app.mainloop()