print('program is started')
try:
    a=10
    b=1
    c=a/b
    d=a[2]
except ZeroDivisionError as e:
    print("Can't divide number by 0",e)
except TypeError as e:
    print("Type error",e)
    print('Done in TE')
except IndexError:
    print("Index out of range")
except IOError:
    print("IO Error occured")
except ValueError:
    print("Value Error")
except KeyError:
    print("Key is not found")
except Exception:
    print("Generic except block")
except :
    print('Default block is started')

print("terminated")
