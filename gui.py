from tkinter import *
from tkinter import ttk

class App(Frame):

    def __init__(self):
        root = Tk()
        super().__init__(root)
        root.title("DSGen")

        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        TopMenu = ttk.Frame(self.mainframe, height = 64, width = 1920)
        TopMenu.grid(column=0, row=0,sticky=(W,E))
        TopMenu['borderwidth'] = 2
        TopMenu['relief'] = 'sunken'
        TopMenu.grid_propagate(0)

        Gen = ttk.Frame(self.mainframe, height = 920, width = 700)
        Gen.grid(column=0,row=1,sticky=(N,W,E,S))
        Gen['borderwidth'] = 2
        Gen['relief'] = 'sunken'
        Gen.grid_propagate(0)

        self.Lessons = ttk.Frame(Gen, height =900, width =640)
        self.Lessons.grid(column=0,row=1,sticky=(N,W,S))
        self.Lessons['borderwidth'] = 2
        self.Lessons['relief'] = 'sunken'
        self.Lessons.grid_propagate(0)

        Options = ttk.Frame(Gen, height =900, width =640)
        Options.grid(column=1,row=1,sticky=(N,W,S))
        Options['borderwidth'] = 2
        Options['relief'] = 'sunken'
        Options.grid_propagate(0)

        Exos = ttk.Frame(Gen, height =900, width =640)
        Exos.grid(column=2,row=1,sticky=(N,W,S))
        Exos['borderwidth'] = 2
        Exos['relief'] = 'sunken'
        Exos.grid_propagate(0)

        ShowGen = ttk.Button(TopMenu, text='Generator').grid(column = 0, row = 0, sticky=(N,W,E,S))
        ShowDB = ttk.Button(TopMenu, text='Database').grid(column = 1, row = 0,sticky = (N,W,E,S))


        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def GuiShowLessons(self, L):
        T = []
        for i in range(len(L)):
            T.append(ttk.Checkbutton(self.Lessons, text = L[i]).grid(column = 0))
        return T
