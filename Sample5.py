print('program is started')

try:
    a=10
    b=0
   
except ZeroDivisionError as e:
    print("Can't divide number by 0",e)
except TypeError as e:
    print("Type error",e)
    print('Done in TE')
finally:
    print('Finally block is entered')
    
print('program is terminated')