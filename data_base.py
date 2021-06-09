import sqlite3
from sqlite3.dbapi2 import Cursor, connect
# from tkinter import *
# from PIL import ImageTk, Image

# root=Tk()
# # root.title('Code')

conn=sqlite3.connect('paitent_database.db')
# # # create Database 
c=conn.cursor()  # sends command
def drop_table():
    # # commit changes
    c.execute('DROP TABLE information')
    # create table
    c.execute("""CREATE TABLE information ( 
        full_name text,
        image_date date,
        age integer,
        sex text,
        blod_type text,
        cronic_diseas text
    )
     """)
    conn.commit()

    # # close connection 
    # conn.close()

    # insert into table 

def save_in_db(full_name,age,cronic_diseas,gender,blood_type,image_date,result,img):
    conn=sqlite3.connect('paitent_database.db')
    # # # create Database 
    c=conn.cursor()  # sends command
    c.execute("INSERT INTO information VALUES(:full_name,:image_date,:age,:sex,:blod_type,:cronic_diseas)",

    {
        'full_name':full_name,
        'image_date':image_date,
        'age':age,
        'gender':gender,
        'blod_type':blod_type,
        'cronic_diseas':cronic_diseas
    }

    )

    
    conn.commit()

    # # close connection 
    conn.close()





def load_from_db():
    # query data
    c.execute("SELECT * ,oid FROM information")
    recoreds=c.fetchall()
    for rec in recoreds:
        print(rec)  

def query_by_name(full_name_p):
    conn=sqlite3.connect('paitent_database.db')
    # # # create Database 
    c=conn.cursor()  # sends command
    # c.execute("SELECT * ,oid FROM information")
    x=c.execute("SELECT * from information WHERE full_name="+'\''+full_name_p+'\'')
    print(x.fetchall())



# query_by_name("Raneem")

drop_table()
save_info_in_db('Raneem','10/5/2021',23,'F','B+','none')
save_info_in_db('Sami','10/5/2021',23,'F','B+','none')

# save_info_in_db('Sami','10/5/2021',23,'F','none')
# save_info_in_db('Rami','10/5/2021',23,'F','none')
# Load_data()
query_by_name("Raneem")
