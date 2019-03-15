import MySQLdb as db

con=db.connect('localhost','root','root','db2')

cur=con.cursor()

try:
    c=cur.execute('select * from customer')

   # Retrieve All records
    tutl=cur.fetchall()
    for record in tutl:
        print(record)
        
# =============================================================================
#    #retrieve one record
#    for i in range(c):
#         print(cur.fetchone())
# =============================================================================
# =============================================================================
#     tutl=cur.fetchmany(2)
#     for i in tutl:
#         print(i)
# =============================================================================
# =============================================================================
#     res=cur.fetchone()
#     print(res)
# =============================================================================
except Exception as e:
    print('In default block',e)
    
finally:
    con.close()





