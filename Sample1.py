print('program is started')
try:
    a=10
    b=0
    c=a/b
except ZeroDivisionError as e:
    print("Can't divide number by 0",e)
    print('Done in ZDE')
    
print('program is terminated')

