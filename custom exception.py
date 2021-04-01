class Input_str_Error(Exception) :
    def __init__(self,msg) :
        super().__init__(msg)
class Input_bool_Error(Exception) :
    def __init__(self,msg):
        super().__init__(msg)

k = input("Enter a number :")

if type(k) == type('k') :
    raise Input_str_Error('error')
if type(k) == type(True) :
    raise Input_bool_Error(f"Expected int received a Boolean Input - {k}")