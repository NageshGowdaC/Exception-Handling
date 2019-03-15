class AgeInSufficientException(Exception):
    
    def __init__(self,msg):
        print('constructor is called')
        print(msg)
        
def check(age):
    if age<18:
        raise AgeInSufficientException('You\'re age is insufficient')
    else:
        print('Welcome to Registration')
    print('exited')    


print('program started')
age=int(input('Enter your age: '))
try:
    check(age)
except AgeInSufficientException as e:
    print("Exception occured, reason :",e)
    
print('program terminated')
     
        
                