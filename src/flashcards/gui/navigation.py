import tkinter as tk

class Arrow(tk.Label):
    def __init__(self, direction, master=None):
        self.direction = direction
        self.click = True
        
        super().__init__(master, text=self.get_arrow(), relief="groove")
        self.pack(fill=tk.BOTH, side=direction, expand=True)
        
        self.bind("<Button-1>", self.on_click)
        self.bind("<ButtonRelease-1>", self.get_release)
        
    def get_arrow(self) -> str:
        """Gets string representation of arrow based on self.direction"""
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
        
    def get_release(self, *args) -> None:
        if self.direction == "left":
            self.master.left_arrow_release(*args)
        else: 
            self.master.right_arrow_release(*args)
        

class NavigationFrame(tk.Frame):
    def __init__(self, width, height, current, total, master=None):
        self.current = current
        self.total = total
        
        super().__init__(master=master, width=width, height=height//6.5, padx=5, pady=5)
        self.pack(fill=tk.BOTH, expand=True)
        
        self.left_arrow = Arrow("left", master=self)
        self.right_arrow = Arrow("right", master=self)
        self.counter = tk.Label(master=self, text=self.get_label(), relief="groove")
        self.counter.pack(fill=tk.BOTH, side="left", expand=True)

    def get_label(self) -> str:
        """Returns string representation of self.counter label"""
        return f"{self.current}/{self.total}"
    
    def next(self, *args) -> bool:
        if self.current < self.total:
            self.current += 1
            self.counter["text"] = self.get_label()
            return True
        else: 
            return False
        
    def previous(self, *args) -> bool:
        if self.current > 1: 
            self.current -= 1
            self.counter["text"] = self.get_label()
            return True
        else: 
            return False
        
    def left_arrow_release(self, *args):
        if self.previous(): 
            self.left_arrow.on_release()
        else: 
            self.left_arrow.on_fail_release()

    def right_arrow_release(self, *args):
        if self.next(): 
            self.right_arrow.on_release()
        else:
            self.right_arrow.on_fail_release()