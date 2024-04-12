import tkinter as tk
from login_screen import LoginScreen
from monitoring_screen import MonitoringScreen
from header import Header
from user_data import user_data

class DiabetesMonitoringApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Diabetes Monitoring System")
        self.geometry("1000x1000")

        # Stores current user once picked
        self.current_user = None

        self.login_screen = LoginScreen(self, login_callback=self.login)
        self.header = Header(self, logout_callback=self.logout)
        self.monitoring_screen = None
        # Used to keep user's name and ID displayed

        # Initally hide header until user is logged in
        self.header.pack_forget()



        # Initial screen rendered
        self.load_login_screen()


    def load_login_screen(self):
        # Do not display header yet
        self.header.pack_forget()
        # Show only login screen
        self.login_screen.pack(fill = tk.BOTH, expand = True)

    def load_monitoring_screen(self):
        # Forget login screen
        self.login_screen.pack_forget()
        # Display header
        self.header.pack(fill=tk.X)
        # Set header values
        self.header.set_patient_data(self.current_user, user_data.get(self.current_user, {}).get("ID", ""))
        # Show only monitoring screen
        self.monitoring_screen = MonitoringScreen(self, current_user=self.current_user)
        self.monitoring_screen.pack(fill = tk.BOTH, expand = True)


    def login(self, user_selected):
        self.current_user = user_selected
        print("Logging In...", user_selected)
        self.load_monitoring_screen()
        self.update()

    def logout(self):
        print("Logging out...")
        self.current_user = None  
        self.monitoring_screen.pack_forget()
        self.update()
        self.load_login_screen()
        self.update()

        


if __name__ == "__main__":
    app = DiabetesMonitoringApp()
    app.mainloop()

