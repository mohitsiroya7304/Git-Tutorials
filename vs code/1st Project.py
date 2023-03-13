import pyautogui as pg
import time

good=(input("Enter the message you want to send:" ))
r=int(input("Enter the quantity you want to send: "))

if(r>0):
    time.sleep(5)
    for i in range(r):
         g=good
         pg.write(g)
         pg.press("enter") 
else:
    print("Please Enter the range value")