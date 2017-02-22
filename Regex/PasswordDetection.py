import re

def password_strength(password):
    strength_detection = re.compile(r'\d+[^0-9a-zA-Z]*[A-Z]+[^0-9a-zA-Z]*[a-z]+')
    password_test = strength_detection.search(password)
    if password_test == None or len(password) < 8:
        print("Password failed")
        return
    print("Strong password")
    return

password_strength('rH6Uk167MNLLnngx')
password_strength('asfasfas')
password_strength('butts')
password_strength('aAs345Sde4')