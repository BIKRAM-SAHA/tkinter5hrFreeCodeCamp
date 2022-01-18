#using SQLite database which comes with python
import sqlite3
from tkinter import *

conn= sqlite3.connect('address.db')    #connect to already created or create and connect to database
cur= conn.cursor()  #cursor instance that does all stuff to the database
#sqlite has only 5 datatypes: text, integer, real, null, blob
curr.execute("CREATE TABLE addresses(first_name text, last_name text, address text, city text, state text, zipcode integer)")    #create a table



conn.commit()   #commit all changes to the database
conn.close()    #close connection to the database




root=Tk()



root.mainloop()