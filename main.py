from tkinter import *
import db, gui, pdfgen

root = gui.App()
L = db.GetLessons()
print(L)
root.GuiShowLessons(L)
root.mainloop()
