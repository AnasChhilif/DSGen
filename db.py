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

def GetExos():
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    Rq = """SELECT * FROM Exo"""
    cur.execute(Rq)
    res = cur.fetchall()
    print(res)
    return res

def GetExoFromName(name):
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    Rq = """SELECT * FROM Exo WHERE Id = ?"""
    cur.execute(Rq, (name,))
    res = cur.fetchall()
    print(res)
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
    print(res)
    return res

def AddExo(Id, Tags):
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    thing = (Id, Tags);
    Rq = """INSERT INTO Exo(Id, Tags) VALUES(?, ?)"""
    cur.execute(Rq, thing)
    con.commit()
    con.close()

def DeleteExo(Id):
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    Rq = """DELETE FROM Exo WHERE Id = ?;"""
    cur.execute(Rq, (Id,))
    con.commit()
    con.close()

GetLessons()
GetExos()
GetExoFromTag('biton')
