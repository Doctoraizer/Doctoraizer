import sqlite3
from sqlite3.dbapi2 import Cursor, connect
from encryption import *
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
    # full_name,age,cronic_diseas,gender,blood_type,image_date,result,img
    c.execute("""CREATE TABLE information ( 
        full_name text,
        age text,
        cronic_diseas text,
        gender text,
        blood_type text,
        image_date text,
        result text,
        img BLOB
    )
     """)
    conn.commit()


def save_in_db(full_name,age,cronic_diseas,gender,blood_type,image_date,result,img_data):
    conn=sqlite3.connect('paitent_database.db')
    # # # create Database 
    c=conn.cursor()  # sends command
    # with open(img,rb)as f:
    #     img_data=f.read()

    c.execute("INSERT INTO information VALUES(:full_name,:age,:cronic_diseas,:gender,:blood_type,:image_date,:result,:img_data)",

    {
       'full_name':full_name,
       'age':age,
       'cronic_diseas':cronic_diseas,
       'gender':gender,
       'blood_type':blood_type,
       'image_date':image_date,
       'result':result,
       'img_data':img_data,


    }

    )

    
    conn.commit()

    # # close connection 
    conn.close()





def load_from_db():

    # query data
    y=c.execute("SELECT * ,oid FROM information")
    recoreds=c.fetchall()
    decrypt_blocks(recoreds,encrpted_data[1])

    for i in recoreds:
        image=i[7]
        name=i[0]
        # print(image)
        with open(f'{i[0]}','wb') as f:
            f.write(image)
        
  

def query_by_name(full_name_p):
    conn=sqlite3.connect('paitent_database.db')
    x=c.execute("SELECT * from information WHERE full_name="+'\''+full_name_p+'\'')



drop_table()
with open('assets/personal_info.png','rb')as f:
    img_data=f.read()    

encrpted_data=encrypt_blocks('Raneem',23,'he is good','F','B+','10/5/2015')
# save_in_db(encrpted_data[0][0],encrpted_data[0][1],encrpted_data[0][2],encrpted_data[0][3],encrpted_data[0][4],encrpted_data[0][5],'postive',img_data)



# for i in encrpted_data:
#     print(i)

load_from_db()
query_by_name("Raneem")




