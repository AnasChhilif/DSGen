import sqlite3 as sq
DATABASEFILE = "Lesson.db"

# Getting all lesson from  the Lesson table
# @returns {List} a List containing all Lesson names in database
# GetLessons() => [('Lesson1',), ('Lesson2',), ('Lesson3',)]
def GetLessons():
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    cur.execute("""SELECT Name FROM Lesson""")
    res = cur.fetchall()
    return res

# Adding lesson to the Lesson table
# @param {string} name : the lessons name
# @param {int} order : the lessons order in the syllabus
# AddLesson("multivariable calculus", 7) puts the lesson "multivariable calculus" as the 7th lesson
def AddLesson(name, order):
    print(name, order)
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    thing = (order, name);
    Rq = """INSERT INTO Lesson(Ord, Name) VALUES(?, ?)"""
    cur.execute(Rq, thing)
    con.commit()
    con.close()

# Deleteing a lesson from the Lesson table
# @param {string} name : the name of the lesson to be deleted
# DeleteLesson(('multivariable calculus',)) deletes the lesson "multivariable calculus" from the Lesson table
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

# Getting all Exercises from Exo table
# @returns {List} a list containing all Exercises in Exo table
# GetExos() => [('integrating a multivariable function',), ('partial derivatives application',)]
def GetExoName():
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    Rq = """SELECT Id FROM Exo"""
    cur.execute(Rq)
    res = cur.fetchall()
    return res

# Getting all Exercises that have the lesson specified from Exo table
# @params {string} name : the lesson name
# @returns {List} a list containing all Exercises in Exo table
# GetExos() => [('integrating a multivariable function',), ('partial derivatives application',)]
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

# Adds exercise to the Exo table
# @param {string} Id: Exo Id
# @param {string} Tags : a comma seperated string of all lessons the exo treats
# @param {string} Path : the exo path relative to this file
def AddExo(Id, Tags, Path, Lesson):
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    thing = (Id, Tags, Path, Lesson);
    Rq = """INSERT INTO Exo(Id, Tags, Path, Lesson) VALUES(?, ?, ?, ?)"""
    cur.execute(Rq, thing)
    con.commit()
    con.close()

# Deletes Exercise from the Exo table
# @param {string} Id: Exo Id to delete
# DeleteExo(('partial derivatives application'),) deletes the exo in the argument
def DeleteExo(Id):
    con = sq.connect(DATABASEFILE)
    cur = con.cursor()
    Rq = """DELETE FROM Exo WHERE Id = ?;"""
    cur.execute(Rq, Id)
    con.commit()
    con.close()
