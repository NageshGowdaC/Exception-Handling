import MySQLdb as ms

print('Program is started')
con=ms.connect('localhost','root','root')

cur=con.cursor()
try:
    info=cur.execute('create database studyAnalytics')
    
    if(info==1):
        print("data base is created successfully")
    else:
        print("data base is not created")
except Exception as e:
    print('Error is occured because db exist:',e)
finally:
    print('finally block is executed')
    con.close()
    
print('Program is terminated')    

    


