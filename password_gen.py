import random
import pickle
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
up_alphabets = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_chars = ['!','@','#','$','%','^','&','*','~','+','-','_','?']
def password(description):
    def split(word):
        return list(word)
    password = str()
    times = 0
    ten = 10
    k = list()
    global works
    works = False
    works1 = False
    works2 = False
    works3 = False
    n = list()
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
        if choice == 1:
            up_low_choice = random.randint(0,1)
            if up_low_choice == 0:
                works1 = True
                alpha_choice = random.choice(alphabets)
                password += alpha_choice
            if up_low_choice == 1:
                works2 = True
                alpha_choicee = random.choice(up_alphabets)
                password += alpha_choicee
            times += 1        
        if choice == 2:
             works3 = True
             special_choice = random.choice(special_chars)
             password += special_choice
             times += 1
    if works == False:
        password = list(password)
        password.pop()
        works = True 
        password += k[times]
        times += 1
    if works1 == False:
        password = list(password)
        password.pop()
        works1 = True
        alpha_choice = random.choice(alphabets)
        password += alpha_choice
    if works2 == False:
        password = list(password)
        password.pop()
        works2 = True
        alpha_choicee = random.choice(up_alphabets)
        password += alpha_choicee
    if works3 == False:
        password = list(password)
        password.pop()
        works3 = True
        special_choice = random.choice(special_chars)
        password += special_choice
    password = str(password) 
    print(password)
