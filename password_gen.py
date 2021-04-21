import random
import pickle
import os
import shutil
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
up_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_chars = ['!','@','#','$','%','^','&','*','~','+','-','_','?']
def password(description,digits):
    password = str()
    times = 0
    digits = int(digits)
    ten = digits
    k = list()
    global works
    works = False
    works1 = False
    works2 = False
    works3 = False
    n = list()
    class my_dictionary(dict):
        def __init__(self):
            self = dict()
        def add(self, key, value):
            self[key] = value
    for l in range(ten):
        o = random.randint(0,9)
        o = str(o)
        k.append(o)
    for l in range(ten):
        choice = random.randint(0,2)
        if choice == 0:
            works = True 
            password += k[times]
            times += 1
            password = str(password) 
        if choice == 1:
            up_low_choice = random.randint(0,1)
            if up_low_choice == 0:
                works1 = True
                alpha_choice = random.choice(alphabets)
                password += alpha_choice
                password = str(password) 
            if up_low_choice == 1:
                works2 = True
                alpha_choicee = random.choice(up_alphabets)
                password += alpha_choicee
                password = str(password) 
            times += 1        
        if choice == 2:
             works3 = True
             special_choice = random.choice(special_chars)
             password += special_choice
             times += 1
             password = str(password) 
    if works == False:
        password = list(password)
        password.pop()
        password += k[times]
        times += 1
        password = str(password)
        works = True
    if works1 == False:
        password = list(password)
        password.pop()
        alpha_choice = random.choice(alphabets)
        password += alpha_choice
        password = str(password)
        works1 = True
    if works2 == False:
        password = list(password)
        password.pop()
        alpha_choicee = random.choice(up_alphabets)
        password += alpha_choicee
        password = str(password)
        works2 = True
    if works3 == False:
        password = list(password)
        password.pop()
        special_choice = random.choice(special_chars)
        password += special_choice
        password = str(password)
        works3 = True
    try:
        password = eval(password)
        if type(password) is list:
            password = "".join(password)
    except Exception:
        pass
    password = str(password)
    print(str(password))
    print('save the password?')
    answer = input('>>>')
    answer = answer.upper()
    dictt = dict()
    dictt.update({description : password})
    try:
        with open('passwords.pickle', 'rb') as handle:
            b = pickle.load(handle)
            dictt += b
    except:
        pass
    if answer == 'YES':
        with open(description, 'wb') as handle:
            pickle.dump(dictt, handle, protocol=pickle.HIGHEST_PROTOCOL)
    if answer == 'NO':
        pass  
def find(descrip):
    with open(descrip, 'rb') as handle:
        b = pickle.load(handle)
    print(b.get(descrip))
    
