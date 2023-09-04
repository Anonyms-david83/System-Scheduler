import os

def shutdown(second):
    return os.system(f'shutdown /s /t {second}')


def restart(second):
    return os.system(f'shutdown /r /t {second}') #if user tiks the now checkbox the second returns 1 second

def logout():
    return os.system(f'shutdown -l') #imidietly logout the windows 

def cancel():
     os.system('shutdown /a') #cancels the oprtaion



