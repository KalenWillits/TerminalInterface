#This code was written by Kalen Willits
import os #Uses the operating system's clear screen funtion to refresh the terminal
import time #Allows the use of time.sleep funtion to delay a refresh
import keyboard #Listens to keyboard events -> Also can generate keyboard events
from colorama import init, deinit, Fore, Back, Style #Allows the use of different colors
init() #Initializes colorama, this is only required for windows OS.
print(Fore.BLACK + Back.BLACK) #Sets the default color to all black. This hides keyboard inputs
import cursor
cursor.hide()#hides the blinking cursor
##################################Variable Library##############################
menu = ['Option Zero', 'Option One', 'Option Two', 'Exit']
################################################################################
def navigate(idx):
    key = keyboard.read_key()
    key = keyboard.read_key()

    if key == 'up':
        idx -= 1

    if key == 'down':
        idx += 1

    if key == 'enter':
        page_fuction(idx)



    return idx#listens to keyboard inputs and changes the index(idx).
    #Which page is displayed depends on the selected index
def page_fuction(idx):
    if idx == 0:
        refresh(0)
        xyprint(20,10, Fore.GREEN + '\tOption Zero Selected!' + Style.NORMAL + Fore.BLACK)
        refresh(1)

    if idx == 1:
        refresh(0)
        xyprint(20,10, Fore.GREEN + '\tOption One Selected!' + Style.NORMAL + Fore.BLACK)
        refresh(1)

    if idx == 2:
        refresh(0)
        xyprint(20,10, Fore.GREEN + '\tOption Two Selected!' + Style.NORMAL + Fore.BLACK)
        refresh(1)

    if idx == 3:
        print(Style.RESET_ALL)
        cursor.show()
        deinit()
        refresh(0)
        return exit()#This is where the funtions for selected index's are stored.

def refresh(delay):
    time.sleep(delay)
    os.system('clear')#Clears the entire screen.

def xyinput(x, y, prompt):
    y_fill = '\n'
    x_fill = ' '
    y = y*y_fill
    x = (x-len(prompt))*x_fill
    return input(str(y)+str(x)+prompt)#prints an input to the corresponding x y coordinates

def xyprint(x, y, string):
    y_fill = '\n'
    x_fill = ' '
    y = y*y_fill
    x = x*x_fill
    return print(str(y)+str(x)+string)#prints a string to the corresponding x y coordinates
#############################Pages to be printed################################

#Labeled as (camel case name)_(index indentifier)
def pageMenu_idx0():
            refresh(0)
            xyprint(10,10,(Style.BRIGHT + Fore.GREEN +'>' + menu[0]  + Style.NORMAL + Fore.BLACK))
            xyprint(11, 0,(Fore.WHITE + ' ' + menu[1] + Fore.BLACK))
            xyprint(12, 0,(Fore.WHITE + ' ' + menu[2] + Fore.BLACK))
            xyprint(13, 0,(Fore.WHITE + ' ' + menu[3] + Fore.BLACK))

def pageMenu_idx1():
            refresh(0)
            xyprint(10,10,(Fore.WHITE + ' ' + menu[0] + Fore.BLACK))
            xyprint(11, 0,(Style.BRIGHT + Fore.GREEN +'>' + menu[1] + Style.NORMAL + Fore.BLACK))
            xyprint(12, 0,(Fore.WHITE + ' ' + menu[2] + Fore.BLACK))
            xyprint(13, 0,(Fore.WHITE + ' ' + menu[3] + Fore.BLACK))

def pageMenu_idx2():
            refresh(0)
            xyprint(10,10,(Fore.WHITE + ' ' + menu[0] + Fore.BLACK))
            xyprint(11, 0,(Fore.WHITE + ' ' + menu[1] + Fore.BLACK))
            xyprint(12, 0,(Style.BRIGHT + Fore.GREEN +'>' + menu[2]  + Style.NORMAL + Fore.BLACK))
            xyprint(13, 0,(Fore.WHITE + ' ' + menu[3] + Fore.BLACK))

def pageMenu_idx3():
            refresh(0)
            xyprint(10,10,(Fore.WHITE + ' ' + menu[0] + Fore.BLACK))
            xyprint(11, 0,(Fore.WHITE + ' ' + menu[1] + Fore.BLACK))
            xyprint(12, 0,(Fore.WHITE + ' ' + menu[2] + Fore.BLACK))
            xyprint(13, 0,(Style.BRIGHT + Fore.GREEN +'>' + menu[3]  + Style.NORMAL + Fore.BLACK))
#####################################Page Wrappers##############################
def alpha(idx):
    print(Fore.WHITE)

    while True:
        refresh(0)


        if idx <= 0:
            pageMenu_idx0()
            idx = 0

        if idx == 1:
            pageMenu_idx1()

        if idx == 2:
            pageMenu_idx2()

        if idx >= 3:
            pageMenu_idx3()
            idx = 3

        idx = navigate(idx)#Main page that holds tells which page is displayed based on the index

################################################################################
alpha(0)#Must pass starting index

print(Style.RESET_ALL)
cursor.show()
deinit()
refresh(0)
