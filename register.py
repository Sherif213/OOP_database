from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd
import csv

class SignIn:
    
    def register(self):
        with open('login.csv', mode='a', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            email = input('Enter your email: ')
            passw = input('Enter your pass: ')
            passw2 = input('Enter your pass again: ')

            if passw == passw2:
                writer.writerow([email, passw])
                print('registration succesfull')
            else:
                print('try again')


    def login(self):
        email = input('Enter your email: ')
        passw = input('Enter your pass: ')
        with open('login.csv', mode = 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                if row == [email, passw]:
                    print('logged in')
                    return True
            print('try again')
            return False
        

personOne=SignIn()
