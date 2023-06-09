from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter.messagebox import askokcancel
import DataGatherer as dg
import csv

img_path = 'img.png'
log_path = 'log.png'


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        # Initalize and set up the style
        self.geometry('1000x700')
        self.resizable(False,False)
        self.title("OAKNUT")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # Creating the frames and frame switcher
        mainframe = Frame(self, width=1000, height=700, bg='#e5e5e5')
        mainframe.pack(expand=True)
        self.frames = {}
        for side in (LoginPage, MainWindow, CourseWindow,
                     CalcWindow, GraphWindow, StudentWindow):
            frame = side(mainframe, self)
            self.frames[side] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(LoginPage)
        # Quit button with askokcancel function
        self.button = ttk.Button(self, text="Quit", command=self.confirm_quit)
        self.button.place(x=775, y=20)

    def show_frame(self, count):
        frame = self.frames[count]
        frame.tkraise()

    def confirm_quit(self):
        answer = askokcancel(title='OAKNUT',
                             message='Are you sure that you want to quit?')
        if answer == True:
            dg.quit_database
            self.destroy()


class LoginPage(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        img = ImageTk.PhotoImage(Image.open(log_path))
        label = Label(self, image=img)
        label.image = img
        label.place(x=0, y=10)
        self.controller = controller
        # Creates Label to indicate the data that the app takes
        self.frame1 = Frame(self, width=325, height=300, bg="#e5e9ee")
        self.frame1.place(x=25, y=140)
        self.label = Label(self.frame1, text="USAUid/ENROLLid",
                           fg="#002f65", bg="#e5e9ee",
                           font=('TkDefaultFont', 11, 'bold'))
        self.label.place(x=30, y=30)
        # Creates entry box for user input
        self.entry = ttk.Entry(self.frame1, width=30)
        self.entry.place(x=30, y=55)
        # Creates Label to indicate the data that the app takes
        self.label1 = Label(self.frame1, text="Password",
                            fg="#002f65", bg="#e5e9ee",
                            font=('TkDefaultFont', 11, 'bold'))
        self.label1.place(x=30, y=100)
        # Creates entry box for user input
        self.entry1 = ttk.Entry(self.frame1, width=30, show="*")
        self.entry1.place(x=30, y=125)
        # Creates button to trigger a login
        self.button = Button(self.frame1, width=10, text="log in",
                             command=self.verify_login,
                             fg='white', bg='#002a5c')
        self.button.place(x=30, y=180)

        self.label2 = Label(self,
                            text="The default Login is \nstudent \npassword",
                            justify=LEFT)
        self.label2.place(x=40, y=475)

        self.label3 = Label(self.frame1, text="", bg="#e5e9ee")
        self.label3.place(x=30, y=235)

        # Default Login
        self.DEFAULT_USER = "student"
        self.DEFAULT_PASSWORD = "password"

    def get_login(self):
        user = self.entry.get()
        passw = self.entry1.get()
        return [user, passw]

    # Function that checks of the inputted values are correct
    def verify_login(self):
        # Grabs the inputted values
        logininfo = self.get_login()
        # Verifies the username and  password
        if (logininfo[0] == self.DEFAULT_USER
                and logininfo[1] == self.DEFAULT_PASSWORD):
            self.label3.config(text="Success.")
            self.controller.show_frame(MainWindow)
            return
        else:
            self.label3.config(text="Invalid Credentials. Please try again.")
            return


class MainWindow(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.config(bg='#f0f0f0')
        img = ImageTk.PhotoImage(Image.open(img_path))
        label = ttk.Label(self, image=img)
        label.image = img
        label.place(x=0)

        # Creates Frame and Button to go to records screen
        self.frame1 = Frame(self, width=350, height=235, bg='white')
        self.frame1.place(x=25, y=100)
        self.label = Label(self.frame1, text="Manage Records", bg='white',
                           font=('TkDefaultFont', 18, 'bold'))
        self.label.place(x=30, y=30)
        self.text = Label(self.frame1,
                          text="Input your Grades/GPA and update your database",
                          bg='white')
        self.text.place(x=30, y=70)
        self.recordbutton = Button(self.frame1, text="Enter Form", command=lambda:
                                   controller.show_frame(StudentWindow))
        self.recordbutton.config(fg='white', bg='#002a5c')
        self.recordbutton.place(x=255, y=185)

        # Creates Frame and Button to go to graph screen
        self.frame2 = Frame(self, width=350, height=235, bg='white')
        self.frame2.place(x=435, y=100)
        self.label2 = Label(self.frame2, text="Compare Requirements", bg='white',
                            font=('TkDefaultFont', 18, 'bold'))
        self.label2.place(x=30, y=30)
        self.text2 = Label(self.frame2,
                           text="Compare standings with the requirement of programs",
                           bg='white')
        self.text2.place(x=30, y=70)
        self.graphbutton = Button(self.frame2, text="View Graph",
                                  command=lambda:
                                  controller.show_frame(GraphWindow))
        self.graphbutton.config(fg='white', bg='#002a5c')
        self.graphbutton.place(x=255, y=185)

        # Creates Frame and Button to go to self.calculator screen
        self.frame3 = Frame(self, width=350, height=235, bg='white')
        self.frame3.place(x=25, y=385)
        self.label3 = Label(self.frame3, text="cGPA Calculator", bg='white',
                            font=('TkDefaultFont', 18, 'bold'))
        self.label3.place(x=30, y=30)
        self.text3 = Label(self.frame3,
                           text="Calculate your cGPA using this tool",
                           bg='white')
        self.text3.place(x=30, y=70)
        self.calculatorbutton = Button(self.frame3, text="Calculate cGPA",
                                       command=lambda:
                                       controller.show_frame(CalcWindow))
        self.calculatorbutton.config(fg='white', bg='#002a5c')
        self.calculatorbutton.place(x=235, y=185)

        # Creates Frame and Button to go to course database screen
        self.frame4 = Frame(self, width=350, height=235, bg='white')
        self.frame4.place(x=435, y=385)
        self.label4 = Label(self.frame4, text="Course Database", bg='white',
                            font=('TkDefaultFont', 18, 'bold'))
        self.label4.place(x=30, y=30)
        self.text4 = Label(self.frame4,
                           text="View the course database containing course medians",
                           bg='white')
        self.text4.place(x=30, y=70)
        self.databasebutton = Button(self.frame4, text="View Courses",
                                     command=lambda:
                                     controller.show_frame(CourseWindow))
        self.databasebutton.config(fg='white', bg='#002a5c')
        self.databasebutton.place(x=245, y=185)


class CourseWindow(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.label = Label(self, text="", font=('TkDefaultFont', 85, 'bold'))
        self.label.grid(row=0, column=0)
        img = ImageTk.PhotoImage(Image.open(img_path))
        label = ttk.Label(self, image=img)
        label.image = img
        label.place(x=0)
        self.title = Label(self, text="Course Database", fg='#38a7c0',
                           font=('TkDefaultFont', 18, 'bold'))
        self.title.place(x=115, y=85)

        # Setting up the scrollbar for the treeview
        self.scroll = ttk.Scrollbar(self, orient="vertical")
        self.scroll.grid(row=1, column=1, sticky="ns")

        # Setting up the treeview for the course database
        self.tree = ttk.Treeview(self, columns=("code", "name", "median"), height=25)
        self.tree.grid(row=1, column=0)

        # Setting up the treeview headings and columns
        self.tree.heading('#0', text="Program")
        self.tree.heading('code', text="Course Code")
        self.tree.heading('name', text="Course Name")
        self.tree.heading('median', text="Course Median")
        self.tree.column('#0')
        self.tree.column("code", anchor=CENTER)
        self.tree.column("name", anchor=CENTER)
        self.tree.column("median", anchor=CENTER)

        # Setting up the treeview headings and columns
        self.tree.insert('', 0, 'sta', text='Statistics')
        self.tree.insert('', 0, 'rlg', text='Religion')
        self.tree.insert('', 0, 'pol', text='Political Science')
        self.tree.insert('', 0, 'mat', text='Mathematics')
        self.tree.insert('', 0, 'his', text='History')
        self.tree.insert('', 0, 'ggr', text='Geography (GGR)')
        self.tree.insert('', 0, 'eng', text='English')
        self.tree.insert('', 0, 'csc', text='Computer Science')
        self.tree.insert('', 0, 'cct', text='CCIT')
        self.tree.insert('', 0, 'bio', text='Biology')
        self.tree.insert('', 0, 'ant', text='Anthorpology')

        # Open the courses csv file and add the courses to the treeview
        with open('Courses.csv') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if "ANT" in row[0]:
                    self.tree.insert("ant", "end", values=row)
                if "BIO" in row[0]:
                    self.tree.insert("bio", "end", values=row)
                if "CCT" in row[0]:
                    self.tree.insert("cct", "end", values=row)
                if "CSC" in row[0]:
                    self.tree.insert("csc", "end", values=row)
                if "ENG" in row[0]:
                    self.tree.insert("eng", "end", values=row)
                if "GGR" in row[0]:
                    self.tree.insert("ggr", "end", values=row)
                if "HIS" in row[0]:
                    self.tree.insert("his", "end", values=row)
                if "MAT" in row[0]:
                    self.tree.insert("mat", "end", values=row)
                if "POL" in row[0]:
                    self.tree.insert("pol", "end", values=row)
                if "RLG" in row[0]:
                    self.tree.insert("rlg", "end", values=row)
                if "STA" in row[0]:
                    self.tree.insert("sta", "end", values=row)

        # Connecting the scrollbar with the treeview
        self.scroll.config(command=self.tree.yview)
        self.tree.config(yscrollcommand=self.scroll.set)

        self.label1 = Label(self, text=" ", height=15)
        self.label1.grid(row=2, column=0)
        self.button = ttk.Button(self, text="Back", command=lambda:
                                 controller.show_frame(MainWindow))
        self.button.place(x=20, y=85)


class CalcWindow(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        img = ImageTk.PhotoImage(Image.open(img_path))
        label = ttk.Label(self, image=img)
        label.image = img
        label.place(x=0)
        self.title = Label(self, text="Calculate cGPA", fg='#38a7c0',
                           font=('TkDefaultFont', 18, 'bold'))
        self.title.place(x=115, y=85)
        self.frame1 = Frame(self, width=600, height=500)
        self.frame1.place(x=225, y=225)

        # Initalize the options for the drop down menus
        self.options = ("A+", "A", "A-", "B+", "B", "B-",
                        "C+", "C", "C-", "D+", "D", "D-", "F")

        select = StringVar()
        select2 = StringVar()
        select3 = StringVar()
        select4 = StringVar()
        select5 = StringVar()
        self.dflt = StringVar()
        self.dflt.set('0')
        self.dflt2 = StringVar()
        self.dflt2.set('0')
        self.dflt3 = StringVar()
        self.dflt3.set('0')
        self.dflt4 = StringVar()
        self.dflt4.set('0')
        self.dflt5 = StringVar()
        self.dflt5.set('0')

        # Create the labels, entryboxes and comboboxes for the user to input
        # their grades and course weights
        self.t1 = Label(self.frame1, text="Courses")
        self.t1.grid(row=1, column=0, sticky=W, pady=(3, 3))
        self.t2 = Label(self.frame1, text="Weight")
        self.t2.grid(row=1, column=1, sticky=W, pady=(3, 3))
        self.t3 = Label(self.frame1, text="Grade")
        self.t3.grid(row=1, column=2, sticky=W, pady=(3, 3))

        self.l1 = Label(self.frame1, text="Course 1: ")
        self.l1.grid(row=2, column=0, sticky=W, pady=(3, 3))
        self.e1 = Entry(self.frame1, textvariable=self.dflt)
        self.e1.grid(row=2, column=1, pady=(3, 3))
        self.l2 = Label(self.frame1, text="Course 2: ")
        self.l2.grid(row=3, column=0, sticky=W, pady=(3, 3))
        self.e2 = Entry(self.frame1, textvariable=self.dflt2)
        self.e2.grid(row=3, column=1, pady=(3, 3))
        self.l3 = Label(self.frame1, text="Course 3: ")
        self.l3.grid(row=4, column=0, sticky=W, pady=(3, 3))
        self.e3 = Entry(self.frame1, textvariable=self.dflt3)
        self.e3.grid(row=4, column=1, pady=(3, 3))
        self.l4 = Label(self.frame1, text="Course 4: ")
        self.l4.grid(row=5, column=0, sticky=W, pady=(3, 3))
        self.e4 = Entry(self.frame1, textvariable=self.dflt4)
        self.e4.grid(row=5, column=1, pady=(3, 3))
        self.l5 = Label(self.frame1, text="Course 5: ")
        self.l5.grid(row=6, column=0, sticky=W, pady=(3, 3))
        self.e5 = Entry(self.frame1, textvariable=self.dflt5)
        self.e5.grid(row=6, column=1, pady=(3, 3))

        self.drop1 = ttk.Combobox(self.frame1, textvariable=select)
        self.drop1['values'] = self.options
        self.drop1['state'] = 'readonly'
        self.drop1.grid(row=2, column=2, padx=(4, 4), pady=(3, 3))

        self.drop2 = ttk.Combobox(self.frame1, textvariable=select2)
        self.drop2['values'] = self.options
        self.drop2['state'] = 'readonly'
        self.drop2.grid(row=3, column=2, padx=(4, 4), pady=(3, 3))

        self.drop3 = ttk.Combobox(self.frame1, textvariable=select3)
        self.drop3['values'] = self.options
        self.drop3['state'] = 'readonly'
        self.drop3.grid(row=4, column=2, padx=(4, 4), pady=(3, 3))

        self.drop4 = ttk.Combobox(self.frame1, textvariable=select4)
        self.drop4['values'] = self.options
        self.drop4['state'] = 'readonly'
        self.drop4.grid(row=5, column=2, padx=(4, 4), pady=(3, 3))

        self.drop5 = ttk.Combobox(self.frame1, textvariable=select5)
        self.drop5['values'] = self.options
        self.drop5['state'] = 'readonly'
        self.drop5.grid(row=6, column=2, padx=(4, 4), pady=(3, 3))

        # Create a label that displays the cGPA when the
        # calculate button is pressed
        self.gpa_label = Label(self.frame1, text=" ")
        self.gpa_label.grid(columnspan=3, row=7)

        self.update_button = ttk.Button(self.frame1, text="Calculate",
                                        command=self.calculate)
        self.update_button.grid(row=8, column=1)

        self.reset_button = ttk.Button(self.frame1, text="Reset",
                                       command=self.reset)
        self.reset_button.grid(row=8, column=2)

        self.button = ttk.Button(self, text="Back", command=lambda:
                                 controller.show_frame(MainWindow))
        self.button.place(x=20, y=85)

    # Method that resets all options for the user
    def reset(self):
        self.drop1.set('')
        self.drop2.set('')
        self.drop3.set('')
        self.drop4.set('')
        self.drop5.set('')
        self.dflt.set('0')
        self.dflt2.set('0')
        self.dflt3.set('0')
        self.dflt4.set('0')
        self.dflt5.set('0')
        self.gpa_label.config(text=" ")

    # Method that calculates the cGPA
    def calculate(self):
        if self.e1.get() == '0' and self.drop5.get() == "":
            self.gpa_label.config(text="Please enter a grade and weight!")

        # Convert the individual grade values to individual course GPAs
        if self.drop1.get() == "":
            self.d1_gpa = 0
        if self.drop1.get() == "A+" or "A":
            self.d1_gpa = 4.0
        if self.drop1.get() == "A-":
            self.d1_gpa = 3.7
        if self.drop1.get() == "B+":
            self.d1_gpa = 3.3
        if self.drop1.get() == "B":
            self.d1_gpa = 3.0
        if self.drop1.get() == "B-":
            self.d1_gpa = 2.7
        if self.drop1.get() == "C+":
            self.d1_gpa = 2.3
        if self.drop1.get() == "C":
            self.d1_gpa = 2.0
        if self.drop1.get() == "C-":
            self.d1_gpa = 1.7
        if self.drop1.get() == "D+":
            self.d1_gpa = 1.3
        if self.drop1.get() == "D":
            self.d1_gpa = 1.0
        if self.drop1.get() == "D-":
            self.d1_gpa = 0.7
        if self.drop1.get() == "F":
            self.d1_gpa = 0

        if self.drop2.get() == "":
            self.d2_gpa = 0
        if self.drop2.get() == "A+" or "A":
            self.d2_gpa = 4.0
        if self.drop2.get() == "A-":
            self.d2_gpa = 3.7
        if self.drop2.get() == "B+":
            self.d2_gpa = 3.3
        if self.drop2.get() == "B":
            self.d2_gpa = 3.0
        if self.drop2.get() == "B-":
            self.d2_gpa = 2.7
        if self.drop2.get() == "C+":
            self.d2_gpa = 2.3
        if self.drop2.get() == "C":
            self.d2_gpa = 2.0
        if self.drop2.get() == "C-":
            self.d2_gpa = 1.7
        if self.drop2.get() == "D+":
            self.d2_gpa = 1.3
        if self.drop2.get() == "D":
            self.d2_gpa = 1.0
        if self.drop2.get() == "D-":
            self.d2_gpa = 0.7
        if self.drop2.get() == "F":
            self.d2_gpa = 0

        if self.drop3.get() == "":
            self.d3_gpa = 0
        if self.drop3.get() == "A+" or "A":
            self.d3_gpa = 4.0
        if self.drop3.get() == "A-":
            self.d3_gpa = 3.7
        if self.drop3.get() == "B+":
            self.d3_gpa = 3.3
        if self.drop3.get() == "B":
            self.d3_gpa = 3.0
        if self.drop3.get() == "B-":
            self.d3_gpa = 2.7
        if self.drop3.get() == "C+":
            self.d3_gpa = 2.3
        if self.drop3.get() == "C":
            self.d3_gpa = 2.0
        if self.drop3.get() == "C-":
            self.d3_gpa = 1.7
        if self.drop3.get() == "D+":
            self.d3_gpa = 1.3
        if self.drop3.get() == "D":
            self.d3_gpa = 1.0
        if self.drop3.get() == "D-":
            self.d3_gpa = 0.7
        if self.drop3.get() == "F":
            self.d3_gpa = 0

        if self.drop4.get() == "":
            self.d4_gpa = 0
        if self.drop4.get() == "A+" or "A":
            self.d4_gpa = 4.0
        if self.drop4.get() == "A-":
            self.d4_gpa = 3.7
        if self.drop4.get() == "B+":
            self.d4_gpa = 3.3
        if self.drop4.get() == "B":
            self.d4_gpa = 3.0
        if self.drop4.get() == "B-":
            self.d4_gpa = 2.7
        if self.drop4.get() == "C+":
            self.d4_gpa = 2.3
        if self.drop4.get() == "C":
            self.d4_gpa = 2.0
        if self.drop4.get() == "C-":
            self.d4_gpa = 1.7
        if self.drop4.get() == "D+":
            self.d4_gpa = 1.3
        if self.drop4.get() == "D":
            self.d4_gpa = 1.0
        if self.drop4.get() == "D-":
            self.d4_gpa = 0.7
        if self.drop4.get() == "F":
            self.d4_gpa = 0

        if self.drop5.get() == "":
            self.d5_gpa = 0
        if self.drop5.get() == "A+" or "A":
            self.d5_gpa = 4.0
        if self.drop5.get() == "A-":
            self.d5_gpa = 3.7
        if self.drop5.get() == "B+":
            self.d5_gpa = 3.3
        if self.drop5.get() == "B":
            self.d5_gpa = 3.0
        if self.drop5.get() == "B-":
            self.d5_gpa = 2.7
        if self.drop5.get() == "C+":
            self.d5_gpa = 2.3
        if self.drop5.get() == "C":
            self.d5_gpa = 2.0
        if self.drop5.get() == "C-":
            self.d5_gpa = 1.7
        if self.drop5.get() == "D+":
            self.d5_gpa = 1.3
        if self.drop5.get() == "D":
            self.d5_gpa = 1.0
        if self.drop5.get() == "D-":
            self.d5_gpa = 0.7
        if self.drop5.get() == "F":
            self.d5_gpa = 0

        # Calculate cGPA
        result = round((((float(self.e1.get()) * self.d1_gpa) +
                         (float(self.e2.get()) * self.d2_gpa)
              + (float(self.e3.get()) * self.d3_gpa)
              + (float(self.e4.get()) * self.d4_gpa)
              + (float(self.e5.get())*self.d5_gpa))
            / (float(self.e1.get()) + float(self.e2.get()) +
             float(self.e3.get()) + float(self.e4.get()) +
               float(self.e5.get()))), 2)

        self.gpa_label.config(text="Your cGPA is: " + str(result))


class GraphWindow(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        img = ImageTk.PhotoImage(Image.open(img_path))
        label = ttk.Label(self, image=img)
        label.image = img
        label.place(x=0)
        self.title = Label(self, text="Compare Requirements", fg='#38a7c0',
                           font=('TkDefaultFont', 18, 'bold'))
        self.title.place(x=115, y=85)
        # Creates combo box for user choices
        self.options = dg.list_program()
        self.select = StringVar()
        self.drop = ttk.Combobox(self, textvariable=self.select, width=38)
        self.drop['values'] = self.options
        self.drop['state'] = 'readonly'
        self.drop.current(0)
        self.drop.place(x=350, y=130)
        # Creates button that starts the graphing process
        self.button = ttk.Button(self, text="Select", command=self.get_name)
        self.button.place(x=290, y=165)
        # Creates button that clears the graph in order to create a new one
        self.button1 = ttk.Button(self, text="Reset", command=self._clear)
        self.button1.place(x=450, y=165)
        # Creates label indicating input status
        self.label = Label(self, text="Select the program here:")
        self.label.place(x=190, y=130)
        # Creates figure where graph goes in
        # self.plot = plt
        self.figure = plt.figure()
        self.axes = self.figure.add_subplot()
        # Creates canvas where to place the figure
        self.figure_canvas = FigureCanvasTkAgg(self.figure, self)

        self.button = ttk.Button(self, text="Back", command=lambda:
                                 controller.show_frame(MainWindow))
        self.button.place(x=20, y=85)

    # Method that graphs the data based on user input
    def plot_grades(self, records, m):
        y = [records[0][0], records[0][1]]
        student = ['Personal AVG'] + [m[0][0]]
        self.axes.bar([student[0], y[0]], (student[1], y[1]))
        self.figure_canvas.draw()
        self.figure_canvas.get_tk_widget().place(x=90, y=205)

    # Method that gets data from the user and matches it with
    # the one on the database. Sends it to the graphing method
    def get_name(self,):
        s = self.drop.get()
        if dg.check_program(s) is False:
            self.label.config(text="Invalid entry, try again. Examples: Biology MSc, Biology PhD")
        else:
            records, m = dg.select_program(s)
            self.plot_grades(records, m)

    # Method that clears the canvas
    def _clear(self):
        self.axes.clear()
        self.figure_canvas.draw()


class StudentWindow(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        img = ImageTk.PhotoImage(Image.open(img_path))
        label = ttk.Label(self, image=img)
        label.image = img
        label.place(x=0)
        self.title = Label(self, text="Manage Records", fg='#38a7c0',
                           font=('TkDefaultFont', 18, 'bold'))
        self.title.place(x=115, y=85)
        # Creates Label to indicate the data that the app takes
        self.label = Label(self, text="Enter a grade, mark or GPA:")
        self.label.place(x=200, y=250)
        self.label2 = Label(self, text="NOTE: Inputting the GPA will round your mark to the lowest value in the range based on the UofT grading table.")
        self.label2.place(x=135, y=500)
        # Creates entry box for user input
        self.entry = ttk.Entry(self, width=30)
        self.entry.place(x=400, y=250)
        # Creates button to trigger the record update
        self.button = ttk.Button(self, text="Update Records",
                                 command=self.get_data)
        self.button.place(x=400, y=280)

        self.button2 = ttk.Button(self, text="Back", command=lambda:
                                  controller.show_frame(MainWindow))
        self.button2.place(x=20, y=85)

        self.label3 = Label(self, text=" ")
        self.label3.place(x=350, y=350)

        self.errorflag = False

    # Method that checks the input and enter the corresponding values from the input
    def update_data(self, s):
        grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+",
                  "D", "D-", "F"]
        marks = [(90, 101), (85, 89), (80, 84), (77, 79), (73, 76),
                 (70, 72), (67, 69), (63, 66), (60, 62), (57, 59),
                 (53, 56), (50, 52), (0, 49)]
        GPAs = [4.0, 4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]
        self.errorflag = False
        try:
            if s.isdigit() or isinstance(s, str) or s.replace(".", "").isnumeric():
                if s in grades:
                    n = 0
                    while n < len(grades):
                        if grades[n] == s:
                            t = [grades[n], marks[n][0], GPAs[n]]
                            dg.edit_student(t)
                        n += 1
                    return
                elif "." not in s and int(s) in range(0, 101):
                    n = 0
                    while n < len(marks):
                        if int(s) in range(marks[n][0], marks[n][1]):
                            t = [grades[n], s, GPAs[n]]
                            dg.edit_student(t)
                        n += 1
                    return
                elif float(s) in GPAs:
                    n = 0
                    while n < len(GPAs):
                        if GPAs[n] == float(s):
                            t = [grades[n], marks[n][0], s]
                            dg.edit_student(t)
                        n += 1
                    return
            # If none of the if statements are entered, the input must be invalid
            self.errorflag = True
        # If there is a ValueError, set an error flag
        except ValueError:
            self.errorflag = True


# Method to get the data from the user. Calls the update_data function
    def get_data(self):
        # Provide a message for the user if error flag is true
        s = self.entry.get()
        self.update_data(s)
        if self.errorflag:
            self.label3.config(text="Invalid Input: Please enter a grade, mark or GPA")
            return
        self.label3.config(text="Marks successfully updated.")


App().mainloop()
