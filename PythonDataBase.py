 # Assignment 171 Python   
import sqlite3

# Create and make connection to database.
conn = sqlite3.connect('files.db')

# With connection create table.
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT)")
    conn.commit()
conn.close()

# File list to read in to database
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('files.db')

# Insert file names in the database that end in .txt and print them to screen
with conn:
    cur = conn.cursor()
    for file in fileList:
        if '.txt' in file:
            cur.execute("INSERT INTO tbl_files(col_file) VALUES (?)", (file,))
            print(file)
    conn.commit()
conn.close()   
