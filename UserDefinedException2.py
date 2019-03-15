class LengthZeroException(Exception):
    pass


def validate(name):
    if(len(name)==0):
        raise LengthZeroException()
    else:
        print('Length is non zero')

try:
    validate('')
except LengthZeroException as e:
    print('length is zero',e)
