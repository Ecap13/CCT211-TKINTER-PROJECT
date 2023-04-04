from tkinter import *
import tkinter.ttk as ttk
import csv

root = Tk()
root.title(" ")
root.geometry('900x600')

scroll = Scrollbar(root)
scroll.pack(side=RIGHT, fill=Y)

label = ttk.Label(root, text="Course View")
label.pack()

tree = ttk.Treeview(root, columns=("code", "name", "median"), height=25)
tree.pack()

tree.heading('#0', text="Program")
tree.heading('code', text="Course Code")
tree.heading('name', text="Course Name")
tree.heading('median', text="Course Median")

tree.column('#0')
tree.column("code", anchor=CENTER)
tree.column("name", anchor=CENTER)
tree.column("median", anchor=CENTER)

tree.insert('', 0, 'sta', text='Statistics')
tree.insert('', 0, 'rlg', text='Religion')
tree.insert('', 0, 'pol', text='Political Science')
tree.insert('', 0, 'mat', text='Mathematics')
tree.insert('', 0, 'his', text='History')
tree.insert('', 0, 'ggr', text='Geography (GGR)')
tree.insert('', 0, 'eng', text='English')
tree.insert('', 0, 'csc', text='Computer Science')
tree.insert('', 0, 'cct', text='CCIT')
tree.insert('', 0, 'bio', text='Biology')
tree.insert('', 0, 'ant', text='Anthorpology')

with open('Courses.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if "ANT" in row[0]:
            tree.insert("ant", "end", values=row)
        if "BIO" in row[0]:
            tree.insert("bio", "end", values=row)
        if "CCT" in row[0]:
            tree.insert("cct", "end", values=row)
        if "CSC" in row[0]:
            tree.insert("csc", "end", values=row)
        if "ENG" in row[0]:
            tree.insert("eng", "end", values=row)
        if "GGR" in row[0]:
            tree.insert("ggr", "end", values=row)
        if "HIS" in row[0]:
            tree.insert("his", "end", values=row)
        if "MAT" in row[0]:
            tree.insert("mat", "end", values=row)
        if "POL" in row[0]:
            tree.insert("pol", "end", values=row)
        if "RLG" in row[0]:
            tree.insert("rlg", "end", values=row)
        if "STA" in row[0]:
            tree.insert("sta", "end", values=row)

scroll.config(command=tree.yview)
tree.config(yscrollcommand=scroll.set)

root.mainloop()
