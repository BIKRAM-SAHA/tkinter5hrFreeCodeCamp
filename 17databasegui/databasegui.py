from tkinter import *
import sqlite3

root=Tk()
root.title("GUI")
root.resizable(False,False)

# curr.execute("CREATE TABLE addresses(first_name text, last_name text, address text, city text, state text, zipcode integer)")    #create a table

f_name= Entry(root, width=30)
f_name.grid(row=0,column=1, padx=20)
l_name= Entry(root, width=30)
l_name.grid(row=1,column=1, padx=20)
address= Entry(root, width=30)
address.grid(row=2,column=1, padx=20)
city= Entry(root, width=30)
city.grid(row=3,column=1, padx=20)
state= Entry(root, width=30)
state.grid(row=4,column=1, padx=20)
zipcode= Entry(root, width=30)
zipcode.grid(row=5,column=1, padx=20)

f_name_label=Label(root,text="first name")
f_name_label.grid(row=0,column=0, sticky=W)
last_name_label=Label(root,text="last name")
last_name_label.grid(row=1,column=0, sticky=W)
address_label=Label(root,text="address name")
address_label.grid(row=2,column=0, sticky=W)
city_label=Label(root,text="city name")
city_label.grid(row=3,column=0, sticky=W)
state_label=Label(root,text="state name")
state_label.grid(row=4,column=0, sticky=W)
zipcode_label=Label(root,text="zipcode name")
zipcode_label.grid(row=5,column=0, sticky=W)

def submit():
    conn=sqlite3.connect("database.db")
    curr=conn.cursor()
    # curr.execute("CREATE TABLE addresses(first_name text, last_name text, address text, city text, state text, zipcode integer)")
    curr.execute(f"INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",{
        "f_name":f_name.get(),
        "l_name":l_name.get(),
        "address":address.get(),
        "city":city.get(),
        "state":state.get(),
        "zipcode":zipcode.get()
    })
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)
    conn.commit()
    conn.close()
def query():
    conn=sqlite3.connect("database.db")
    curr=conn.cursor()
    curr.execute("SELECT *,oid FROM addresses")
    records=curr.fetchall()
    print_records=''
    for record in records:
        print_records+=str(record) +'\n'
    query_label=Label(root,text=print_records)
    query_label.grid(row=9,column=0,columnspan=2,sticky=W+E+N+S)
    conn.commit()
    conn.close()
def delete(oid):
    if(oid):
        conn=sqlite3.connect("database.db")
        curr=conn.cursor()
        curr.execute(f"DELETE FROM addresses WHERE oid={oid}")
        conn.commit()
        conn.close()
#update:
#curr.execute("UPDATE addresses SET first_name=:first,last_name=:last, address=:address,city=:city,state=:state,zipcode=:zipcode WHERE oid=:oid",{
#   "first"=...
#   "last"=...
#   "address"=...
#   "city"=...
#   "state"=...
#   "zipcode"=...
#   "oid"=...
# })

submitBtn= Button(root, text="Submit", command=submit)
submitBtn.grid(row=6, column=1, pady=10,padx=10, sticky=W)
queryBtn= Button(root,text="Query",command=query)
queryBtn.grid(row=7, column=1, pady=10, padx=15, sticky=W)
deleteBtn=Button(root, text="DELETE",command=lambda:delete(deleteEntry.get()))
deleteBtn.grid(row=8, column=1, pady=5, padx=10, sticky=W)
deleteEntry=Entry(root, width=20)
deleteEntry.grid(row=8, column=0, pady=5, padx=10)

root.mainloop()