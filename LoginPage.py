from tkinter import *

# Function that checks of the inputted values are correct
def verify_login(window):
    # Grabs the inputted values
    logininfo = window.get_login()
    # Verifies the username
    if logininfo[0] == window.DEFAULT_USER:
        # Verifies the password
        if logininfo[1] == window.DEFAULT_PASSWORD:
            window.label3.config(text="Success.")
            return
    else:
        window.label3.config(text="Invalid Credentials. Please try again.")
        return

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.geometry("900x600")
        # Creates Label to indicate the data that the app takes
        self.label = Label(self.master, text="Username")
        self.label.place(x=290, y=220)
        # Creates entry box for user input
        self.entry = Entry(master, width=30)
        self.entry.place(x=400, y=220)
        # Creates Label to indicate the data that the app takes
        self.label1 = Label(self.master, text="Password")
        self.label1.place(x=290, y=240)
        # Creates entry box for user input
        self.entry1 = Entry(master, width=30)
        self.entry1.place(x=400, y=240)
        # Creates button to trigger a login
        self.button = Button(self.master, height=2, width=10, text="Login", command=lambda: verify_login(self))
        self.button.place(x=400, y=280)

        self.label2 = Label(master, text="The default Login is Username: student and Password: password")
        self.label2.place(x=265, y=350)

        self.label3 = Label(master, text="")
        self.label3.place(x=350, y=180)

        # Default Login
        self.DEFAULT_USER = "student"
        self.DEFAULT_PASSWORD = "password"

    def get_login(self):
        user = self.entry.get()
        passw = self.entry1.get()
        return [user, passw]


window = Tk()
bro = LoginWindow(window)
window.mainloop()

