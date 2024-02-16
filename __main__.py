'''
Created on Sep 23, 2023

@author: EnderWolf
'''

from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time

def main():
    print("Please keep in mind that this is only good for dragons that are ALL \n" + 
          "scratchers. Don't have a meditator in your party!")
    print("Mouse over the space between Items, Defend and Flee (Don't click) and press \n" +
          "enter!")
    input("Waiting for Enter...")
    
    keyboard = KeyboardController()
    mouse = MouseController()
    
    mouse.click(Button.left, 1)

    while(True):
        keyboard.press('a')
        time.sleep(0.1)
        keyboard.release('a')
        time.sleep(0.2)
        keyboard.press('e')
        time.sleep(0.1)
        keyboard.release('e')
        time.sleep(0.2)
        keyboard.press('q')
        keyboard.release('q')
        keyboard.press('w')
        keyboard.release('w')
        keyboard.press('e')
        keyboard.release('e')
        keyboard.press('r')
        keyboard.release('r')
        keyboard.press('t')
        keyboard.release('t')
        time.sleep(2)
        mouse.click(Button.left, 1)
        
if __name__ == "__main__":
    main()