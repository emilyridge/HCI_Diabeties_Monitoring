import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from user_data import user_data
from tooltip import ToolTip


class MonitoringScreen(tk.Frame):
    def __init__(self, master=None, current_user = None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.current_user = current_user

        self.tell_label = ttk.Label(self, text="Have you taken your blood sugar today? If not, please do so and enter your results below.")
        self.tell_label.pack(pady=5)
        self.label = ttk.Label(self, text="Enter blood sugar reading(0-999): ")
        self.label.pack(pady=5)
        self.entry = ttk.Entry(self)
        tooltip_entry = ToolTip(self.entry, "You should submit one value at a time.")
        self.entry.pack(pady=5)
        self.button = ttk.Button(self, text="Submit Reading", command=self.check_reading)
        tooltip_button = ToolTip(self.button, "Click this button once you have entered a number")
        self.button.pack(pady=5)
        self.help_button = ttk.Button(self, text="Help")
        tooltip_help_button = ToolTip(self.help_button, "Check the information at the top to make sure\n you are logged in as the correct person.\n Then you can enter in a blood sugar reading\n one at a time and get the results from that reading\n based on your own personal values.\n You can logout at any time by clicking\n the logout button.")
        self.help_button.pack(pady=10)


 

    def check_reading(self):
        user_input = self.entry.get()
        user_low_val = int(user_data.get(self.current_user, {}).get("LowReading", "0"))
        user_high_val = int(user_data.get(self.current_user, {}).get("HighReading", "0"))
        user_dr_name = user_data.get(self.current_user, {}).get("DoctorName", "")
        user_dr_num = user_data.get(self.current_user, {}).get("DoctorPhone", "")


        try:
            user_input = int(user_input)
            if user_input >= 0 and user_input <= 999:
                if user_input < user_low_val:
                    messagebox.showinfo("Message", "Your reading is low. To fix this you should: eat a sugar souce, take your medicine, and eat meals and snacks as described by you doctor.")
                    # ask user for reason for value
                    self.explain_reason()

                elif user_input > user_high_val:
                    messagebox.showinfo("Message", "Your reading is high. You should call your doctor immedietly: " + user_dr_name + ": " + user_dr_num + ". You should check if there is a presence of ketones in your urine.")
                    # ask user for reason for value
                    self.explain_reason()

                else:
                    messagebox.showinfo("Message", "Your reading is in the healthy range!")



            else:
                messagebox.showerror("Error", "Value must be between 0-999.")
                self.entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Invalid input, you must enter a number.")
            self.entry.delete(0, tk.END)


        


    def explain_reason(self):
        if not hasattr(self, 'text_label'):
            self.text_label = ttk.Label(self, text="Reason for reading: ")
            self.text_label.pack(pady=5)
            self.text_box = tk.Text(self, height=5, width=30)
            self.text_box.pack(pady=5)
            self.submit_button = ttk.Button(self, text="Submit", command=self.submit_reason)
            self.submit_button.pack(pady=5)


    def submit_reason(self):
        self.text_label.destroy()
        self.text_box.destroy()
        self.submit_button.destroy()
        self.entry.delete(0, tk.END)
        