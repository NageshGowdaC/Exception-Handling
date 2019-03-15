print('program is started')
try:
    a=10
    b=0
    c=a/b
    d=a[2]
except Exception as e:
    print("generic exception is occured:",e)
print('program is terminated')