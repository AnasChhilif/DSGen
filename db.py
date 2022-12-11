import sqlite3 as sq
DATABASEFILE = "Lesson.db"

def GetLessons():
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    cur.execute("""SELECT Name FROM Lesson""")
    res = cur.fetchall()
    return res

def AddLesson(name, order):
    print(name, order)
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
    cur.execute(Rq, name)
    con.commit()
    con.close()

def GetExos():
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    Rq = """SELECT * FROM Exo"""
    cur.execute(Rq)
    res = cur.fetchall()
    return res

def GetExoName():
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    Rq = """SELECT Id FROM Exo"""
    cur.execute(Rq)
    res = cur.fetchall()
    return res

def GetExoFromLesson(name):
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    Rq = """SELECT Id,Path FROM Exo WHERE Lesson = ?"""
    cur.execute(Rq, name)
    res = cur.fetchall()
    return res

def GetExoFromTag(tag):
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    Rq = """SELECT *
    FROM Exo
    WHERE (',' + RTRIM(Tags) + ',') LIKE '%,' + ? + ',%'
    """
    cur.execute(Rq, (tag,))
    res = cur.fetchall()
    return res

def AddExo(Id, Tags, Path, Lesson):
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    thing = (Id, Tags, Path, Lesson);
    Rq = """INSERT INTO Exo(Id, Tags, Path, Lesson) VALUES(?, ?, ?, ?)"""
    cur.execute(Rq, thing)
    con.commit()
    con.close()

def DeleteExo(Id):
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    Rq = """DELETE FROM Exo WHERE Id = ?;"""
    cur.execute(Rq, Id)
    con.commit()
    con.close()
