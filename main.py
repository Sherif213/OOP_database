from register import *
from product import *
from tqdm import tqdm
import matplotlib.pyplot as plt
from playsound import playsound 
import numpy as np
import time
import os


y=True
while(y):
    enter=int(input("Login 1 or Register 2\n"))
    if(enter==2):
        personOne.register()
    elif(enter==1):
        admin=int(input("Login admin 1 or Login Customer 2?\n"))
        if(admin==2):
            if(personOne.login()):
                choose=int(input("""What do you wanna buy \n1.Fortnite \n2.PlayStation Plus \n """))
                if(choose==1):
                    productOne.showingPrices()
                    productOne.FortniteInterface()
                elif (choose==2):
                    productTwo.PlayStationInterface()
                    
                else:
                    print(f"Invalid input. Please enter a number from 1 to 2.")
        elif(admin==1):
            if(personOne.login()):
                choose=int(input("What do you wanna do? \n1.Show profits for Fortnite\n2.Show profits for PlayStation Plus\n"))
                if(choose==1):
                    productOne.adminSettings()
                elif(choose==2):
                    productTwo.adminSettings()
                else:
                    print(f"Invalid input. Please enter a number from 1 to 2.")
    
    here2=int(input("Are u still here y=1 no =0\n"))
    if(here2==1):
        y=True
        os.system('cls')
    elif(here2==0):
        y=False
        print("<3 Thank you for choosing our services :)")
    else:
        print("choose between 1 or 0")