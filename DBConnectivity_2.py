import MySQLdb as mdb

conn=mdb.connect('localhost','root','root','studyanalytics')

cur=conn.cursor()
try:
    st=cur.execute("insert into customer values(4,'Pretz',9876543329,'nagesha@dupli.com')")
    if st>0:
        print(st,' record(s) inserted successfully')
    else:
        print('insertion has problem')
    conn.commit()
except Exception as e:
    print('Exception is occured ',e) 
    conn.rollback()
except :
    print('Exception is occured by non-matching')
    conn.rollback()
finally :
    print('Finally block is entered')
    conn.close()
    print('Finally block is ended')
    






