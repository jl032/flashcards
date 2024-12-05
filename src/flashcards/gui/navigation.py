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
            self.click = False
        
    def on_release(self, *args) -> None:
        self["relief"] = "groove"
        print("go " + self.direction)
        self.click = True
        
    def on_fail_release(self, *args) -> None:
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
    
    def next(self, *args) -> bool:
        if self.current < self.total:
            self.current += 1
            self["text"] = self.get_label()
            return True
        else: 
            return False
        
    def previous(self, *args) -> bool:
        if self.current > 1: 
            self.current -= 1
            self["text"] = self.get_label()
            return True
        else: 
            return False
    
class NavigationFrame(tk.Frame):
    def __init__(self, width, height, current, total, master=None):
        super().__init__(master=master, width=width, height=height//6.5, padx=5, pady=5)
        self.left_arrow = Arrow("left", master=self)
        self.right_arrow = Arrow("right", master=self)
        self.counter = Counter(current, total, master=self)
        self.pack(fill=tk.BOTH, expand=True)