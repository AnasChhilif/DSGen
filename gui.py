from tkinter import *
from tkinter import ttk
import db


class App(Frame):

    def __init__(self):
        root = Tk()
        super().__init__(root)
        root.title("DSGen")

        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        notebook = ttk.Notebook(self.mainframe, height = 1080, width = 1830)
        notebook.grid(column=0, row=0, sticky=(W,E))
        notebook.grid_propagate(0)

        Gen = ttk.Frame(notebook, height = 1080, width = 700)
        Gen.grid(column=0,row=1,sticky=(N,W,E,S))
        Gen['borderwidth'] = 2
        Gen['relief'] = 'sunken'
        Gen.grid_propagate(0)

        DB = ttk.Frame(notebook, height = 1080, width = 700)
        DB.grid(column=0,row=1,sticky=(N,W,E,S))
        DB['borderwidth'] = 2
        DB['relief'] = 'sunken'
        DB.grid_propagate(0)
        DB.grid_forget()

        notebook.add(Gen, text = "Gen")
        notebook.add(DB, text = "DB")

        self.Lessons = ttk.Frame(Gen, height =970, width =610)
        self.Lessons.grid(column=0,row=1,sticky=(N,W,S))
        self.Lessons['borderwidth'] = 2
        self.Lessons['relief'] = 'sunken'
        self.Lessons.grid_propagate(0)

        Options = ttk.Frame(Gen, height =970, width =610)
        Options.grid(column=1,row=1,sticky=(N,W,S))
        Options['borderwidth'] = 2
        Options['relief'] = 'sunken'
        Options.grid_propagate(0)

        Exos = ttk.Frame(Gen, height =970, width =610)
        Exos.grid(column=2,row=1,sticky=(N,W,S))
        Exos['borderwidth'] = 2
        Exos['relief'] = 'sunken'
        Exos.grid_propagate(0)

        self.DBLessons = ttk.Frame(DB, height =970, width =915)
        self.DBLessons.grid(column=1,row=1,sticky=(N,W,S))
        self.DBLessons['borderwidth'] = 2
        self.DBLessons['relief'] = 'sunken'
        self.DBLessons.grid_propagate(0)

        DBExos = ttk.Frame(DB, height =970, width =915)
        DBExos.grid(column=2,row=1,sticky=(N,W,S))
        DBExos['borderwidth'] = 2
        DBExos['relief'] = 'sunken'
        DBExos.grid_propagate(0)

# Generator Content
        textchoose = ttk.Label(Options, text = "Select DS or TD").grid()

        binary = StringVar()
        DS = ttk.Radiobutton(Options, text="DS", variable=binary, value = "ds").grid(row = 1)
        TD = ttk.Radiobutton(Options, text="TD", variable=binary, value = "td").grid(row = 1, column = 1)

        textchoose = ttk.Label(Options, text = "Enter number of exercises to generate").grid()

        self.exnum = StringVar()
        NofEx = ttk.Entry(Options, textvariable=self.exnum).grid()

        self.SelectButton = ttk.Button(Options, text = "Select")
        self.SelectButton.grid(row=5, pady = 15)
        GenButton = ttk.Button(Options, text = "Generate pdf").grid(row=5, column = 1)
# DB Content

        self.DelLesButton = ttk.Button(self.DBLessons, text = "Delete Selected")
        self.DelLesButton.grid(row = 420, column = 6)

        Lessoso = ttk.Label(self.DBLessons, text = "Select Name of Lesson to add").grid(row = 421)

        LessoName = StringVar()
        LessoSpace = ttk.Entry(self.DBLessons, textvariable = LessoName).grid(row = 422)

        Orderoo = ttk.Label(self.DBLessons, text = "Select Order of Lesson to add").grid(column = 2, row = 421)

        LessoOrd= IntVar()
        LessoOrdSpace = ttk.Entry(self.DBLessons, textvariable = LessoOrd).grid(column = 2, row = 422)

        AddLesButton = ttk.Button(self.DBLessons, text = "Add Lesson", command = lambda : db.AddLesson(LessoName.get(), LessoOrd.get())).grid(row = 422, column = 3)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        for child in self.mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def GuiShowLessons(self, L):
        self.T = []
        for i in range(len(L)):
            buffer = IntVar()
            ttk.Checkbutton(self.Lessons, text = L[i], variable = buffer).grid(column = 0)
            self.T.append((L[i], buffer))
        return self.T

    def DBShowLessons(self, L):
        self.T = []
        for i in range(len(L)):
            buffer = IntVar()
            ttk.Checkbutton(self.DBLessons, text = L[i], variable = buffer).grid(row = i, column = 0)
            self.T.append((L[i], buffer))
        return self.T

    def DelSelected(self, L):
        for i in L:
            if(i[1].get()==1):
                db.DeleteLesson(i[0])
