import sqlite3 as sq
DATABASEFILE = "lessons.db"
def main():
    # Connecting to sqlite
    # connection object
    connection_obj = sq.connect('Lesson.db')

    # cursor object
    cursor_obj = connection_obj.cursor()

    # Drop the GEEK table if already exists.
    cursor_obj.execute("DROP TABLE IF EXISTS Lesson")
    cursor_obj.execute("DROP TABLE IF EXISTS Exo")

    # Creating table
    table = """ CREATE TABLE Lesson(
                Name VARCHAR(255) NOT NULL PRIMARY KEY,
                Ord INT NOT NULL
            ); """

    cursor_obj.execute(table)

    table = """ CREATE TABLE Exo(
                Id VARCHAR(255) PRIMARY KEY NOT NULL,
                Tags VARCHAR(255),
                Path VARCHAR(255) NOT NULL,
                Lesson VARCHAR(255) NOT NULL,
                FOREIGN KEY(Lesson) REFERENCES Lesson(Name)
            ); """

    cursor_obj.execute(table)

    cursor_obj.execute('''INSERT INTO Lesson(Name, Ord) VALUES("biton", 1)''')
    cursor_obj.execute('''INSERT INTO Lesson(Name, Ord) VALUES("shmiton", 2)''')
    cursor_obj.execute('''INSERT INTO Lesson(Name, Ord) VALUES("sliton", 3)''')

    cursor_obj.execute('''INSERT INTO Exo(Id, Tags, Path, Lesson)VALUES("central2010","biton", "~/DSGen/exos/ex1.tex", "biton")''')
    cursor_obj.execute('''INSERT INTO Exo(Id, Tags, Path, Lesson) VALUES("ccp2021","sliton", "~/DSGen/exos/ex2.tex", "sliton")''')
    cursor_obj.execute('''INSERT INTO Exo(Id, Tags, Path, Lesson) VALUES("cnc2022","biton,shmiton,sliton", "~/DSGen/exos/ex3.tex", "shmiton")''')
    connection_obj.commit()
    print("Table is Ready")

    # Close the connection
    connection_obj.close()
main()
