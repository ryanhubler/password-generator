'''A basic password generator using python '''

#importing modules
import os
import string
import random

#taking user input for the length of their desired password
def inputs():
    length = int(input("How long would you like you password "))
    return length


def gen():
    #defining password elements
    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase
    characters = ["!","2","$","%","*","@","#","^","&"]
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]

    pre_password = []
    
    count = 0
    length = inputs() 
    
    while count <= length:
        #generates a new random number to create a list of the mixed password elements 
        a_low = random.randint(0,25)
        a_upper = random.randint(0,25)
        c_special = random.randint(0,8)
        num = random.randint(0,9)
        #appending the random elements into a list to be used by random.choices
        pre_password.append(alpha_lower[a_low])
        pre_password.append(alpha_upper[a_upper])
        pre_password.append(characters[c_special])
        pre_password.append(numbers[num])
        
        #used for counting
        count = count + 1
    #uses random.choices to pick from list pre password that contains 4 * length number of random password elements     
    password = random.sample(pre_password, k = length)
    #uses .join to create list password into the string final_pass 
    final_pass = ''.join([str(item) for item in password])
    return final_pass


print(gen())


