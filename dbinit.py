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
                Id INTEGER PRIMARY KEY,
                Ord INT NOT NULL,
                Name VARCHAR(255) NOT NULL
            ); """

    cursor_obj.execute(table)

    table = """ CREATE TABLE Exo(
                Id INT PRIMARY KEY NOT NULL,
                Tags VARCHAR(255),
                Lesson INT,
                FOREIGN KEY(Lesson) REFERENCES Lesson(Id)
            ); """

    cursor_obj.execute(table)

    cursor_obj.execute('''INSERT INTO Lesson(Id, Ord, Name) VALUES(1337, 1,"biton")''')
    cursor_obj.execute('''INSERT INTO Lesson(Ord, Name) VALUES(2,"shmiton")''')
    cursor_obj.execute('''INSERT INTO Lesson(Ord, Name) VALUES(3,"sliton")''')

    connection_obj.commit()
    print("Table is Ready")

    # Close the connection
    connection_obj.close()
main()
