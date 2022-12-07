from tkinter import *
from tkinter import ttk
import db, gui, pdfgen

root = gui.App()
L = db.GetLessons()
Lessons = root.GuiShowLessons(L)
T = root.DBShowLessons(L)
root.DelLesButton.configure(command = lambda : root.DelSelected(T))
root.SelectButton.configure(command = lambda : pdfgen.GetDS(Lessons, root.exnum))
root.mainloop()
