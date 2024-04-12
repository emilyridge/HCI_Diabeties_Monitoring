# Used https://www.w3resource.com/python-exercises/tkinter/python-tkinter-custom-widgets-and-themes-exercise-9.php
# as resource for building this class

import tkinter as tk

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip_visible = False

        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        if not self.tooltip_visible:
            x, y, _, _ = self.widget.bbox("insert")
            x += self.widget.winfo_rootx() + 25
            y += self.widget.winfo_rooty() + 25

            self.tooltip_label = tk.Label(text=self.text, background="lightyellow", foreground="black", relief="solid", borderwidth=1)
            self.tooltip_label.place(x=x, y=y)
            self.tooltip_visible = True

    def hide_tooltip(self, event=None):
        if self.tooltip_visible:
            self.tooltip_label.place_forget()
            self.tooltip_visible = False

    
