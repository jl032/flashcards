import tkinter as tk

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