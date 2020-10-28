# DATABASES AND PYTHON CHALLENGE Step 257

import sqlite3

speciesValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ("Ak'not", "Mangalor", -5))
conn = sqlite3.connect(":memory:")

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
    cur.executemany("INSERT INTO Roster VALUES(?,?,?)", speciesValues)
    cur.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")
    cur.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    for row in cur.fetchall():
        print(row)
