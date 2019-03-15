class Hello(Exception):
    def __init__(self,msg=''):
        self.msg=msg
    def __str__(self):
        return repr(self.msg)

try:
    raise Hello
except Hello:
    print('Exception is Handled')
