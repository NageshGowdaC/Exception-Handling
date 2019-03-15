import MySQLdb as mdb

conn=mdb.connect('localhost','root','root','studyanalytics')

cur=conn.cursor()
try:
    st=cur.execute('create table customer(\
            cid int primary key,\
            name varchar(20) not null,\
            phone decimal(10),\
            emailId varchar(25) )')
    if st==0:
        print('created database table successfully')
    else:
        print('db is not created')
except Exception as e:
    print('Exception is occured ',e) 
except :
    print('Exception is occured by non-matching')
finally :
    print('Finally block is entered')
    conn.close()
    print('Finally block is ended')
    






