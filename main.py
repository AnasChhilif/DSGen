from tkinter import *
import db, gui, pdfgen

root = gui.App()
L = db.GetLessons()
root.GuiShowLessons(L)
root.mainloop()
