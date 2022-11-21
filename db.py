import sqlite3 as sq
DATABASEFILE = "Lesson.db"
def GetLessons():
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    cur.execute("""SELECT Name FROM Lesson""")
    res = cur.fetchall()
    print(res)
    return res
def AddLesson(name, order):
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    thing = (order, name);
    Rq = """INSERT INTO Lesson(Ord, Name) VALUES(?, ?)"""
    cur.execute(Rq, thing)
    con.commit()
    con.close()
def DeleteLesson(name):
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    Rq = """DELETE FROM Lesson WHERE Name = ?;"""
    cur.execute(Rq, (name,))
    con.commit()
    con.close()

GetLessons()
