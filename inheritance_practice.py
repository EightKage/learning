import random


print("before")

try:
    random.randint(10, 50) / random.randint(20, 60)
    
except:
    print(random.randint(5, 15))



try:
    4 / 0
    print("age")
except NameError:
    print("this was a name issue")
    print(3)


except ZeroDivisionError:
   
    print("Void")
    
except Exception as e:
    print("something is wrong")

class cheesyError(Exception):
    pass

def upper_fun(word):
    if len(word) <= 0:
        raise cheesyError("The word has to have atleast one letter")

    return word.upper()

print(upper_fun(""))


print("after")





