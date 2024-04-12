import tkinter as tk
from tkinter import ttk
from user_data import user_data
from tooltip import ToolTip

class LoginScreen(tk.Frame):
    def __init__(self, master=None, login_callback=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.login_callback = login_callback

        # To display
        self.label = ttk.Label(self, text="Select user:")
        self.user_options = ttk.Combobox(self, values=["Sara Norman", "Greg Norman"])
        self.login_button = ttk.Button(self, text="Login", command=self.login_button_clicked)
        self.help_button = ttk.Button(self, text="Help")
        tooltip_help_button = ToolTip(self.help_button, "Select a user from the drop down menu\n then click the login button you. You can return to this \npage by logging out if you accidently \nselect the wrong user.")


        self.label.pack(pady=10)
        self.user_options.pack(pady=10)
        self.login_button.pack(pady=10)
        self.help_button.pack(pady=20)

    def login_button_clicked(self):
        # Get user that was selected
        user_selected = self.user_options.get()
        if self.login_callback:
            self.login_callback(user_selected)
        
    



