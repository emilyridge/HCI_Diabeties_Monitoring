import tkinter as tk
from tkinter import ttk
from user_data import user_data
from tooltip import ToolTip

class Header(tk.Frame):
    def __init__(self, master = None, logout_callback=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        
        self.logout_callback = logout_callback

        self.selected_user = None

        # Variables to keep displayed in header
        self.patient_name_label = ttk.Label(self, text="Current Logged in Patient: ")
        self.patient_id_label = ttk.Label(self, text="Patient ID: ")

        self.patient_name_display = ttk.Label(self, text="")
        self.patient_id_display = ttk.Label(self, text="")
    

        self.logout_button = ttk.Button(self, text="Log out", command=self.logout_button_clicked)
        tooltip_button = ToolTip(self.logout_button, "You can logout at anytime.")


        # Layout
        self.patient_name_label.pack(side="left", padx=10, pady=5)
        self.patient_name_display.pack(side="left", padx=10, pady=5)
        self.patient_id_label.pack(side="left", padx=10, pady=5)
        self.patient_id_display.pack(side="left", padx=10, pady=5)
        self.logout_button.pack(side="left", padx=10, pady=5)


    
    def set_patient_data(self, selected_user, patient_id):
        # Set variables
        self.selected_user = selected_user
        self.patient_name_display.config(text=selected_user)
        self.patient_id_display.config(text=patient_id)


    def logout_button_clicked(self):
        if self.logout_callback:
            self.logout_callback()


