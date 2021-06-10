import sqlite3
from sqlite3.dbapi2 import Cursor, connect
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
    # decrypt_blocks(recoreds,encrpted_data[1])
    # for i in y:
    #     image=i[7]
    #     name=i[0]
    #     # print(image)
    #     with open(f'{i[0]}','wb') as f:
    #         f.write(image)
def query_by_name(full_name_p):
    print('helllo')
    # conn=sqlite3.connect('paitent_database.db')
    x=c.execute("SELECT * from information WHERE full_name="+'\''+full_name_p+'\'')

    return x.fetchall()
    for i in x:
        image=i[7]
        # print(image)
        name=i[0]
        print(name)
        with open(f'{name}'+'.png','wb') as f:
            f.write(image)
    # x.fetchall())
# encrpted_data=encrypt_blocks('Raneem',23,'he is good','F','B+','10/5/2015')
if __name__=="__main__":
    with open('assets/personal_info.png','rb')as f:
        img_data=f.read()
    drop_table()
    save_in_db('Raneem',23,'he is good','F','B+','10/5/2015','result,',img_data)
    print(query_by_name("Raneem"))
