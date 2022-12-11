from tkinter import *
from tkinter import ttk
import db, gui, pdfgen

root = gui.App()
L = db.GetLessons()
Lessons = root.GuiShowLessons(L)
T = root.DBShowLessons(L)
root.DelLesButton.configure(command = lambda : root.DelSelected(T))
ExoPaths = []
root.SelectButton.configure(command = lambda : root.DisplayDS(Lessons, ExoPaths))
root.GenButton.configure(command = lambda : pdfgen.GeneratePDF(ExoPaths, root.binary))
ExosDB = root.DisplayExos()
root.DelExoButton.configure(command = lambda : root.DelSelectedExos(ExosDB))
root.mainloop()
