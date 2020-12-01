import webbrowser 
import pyautogui
import time
import keyboard

print("   _____                  __        ")
print("  / ___/____  ____ ______/ /____  __")
print("  \__ \/ __ \/ __ `/ ___/ //_/ / / /")
print(" ___/ / /_/ / /_/ / /  / ,< / /_/ / ")
print("/____/ .___/\__,_/_/  /_/|_|\__, /  ")
print("    /_/                    /____/   ")
print("---------------------------------------------------------------------------")
print("Sparky's Kahoot Flooder - V1.1 - Developed by Sparkyboy")
print("---------------------------------------------------------------------------")
print()
print()

x = 1

code = input("Code: ")
print()
print("---------------------------------------------------------------------------")
print()
name = input("Name: ")
print()
print("---------------------------------------------------------------------------")
print()
amount = int(input("Bots: "))
print()
print("---------------------------------------------------------------------------")
print()
print("! FLODO WARNING !")
print("---------------------------------------------------------------------------")
print("Instructions: Open a new tab and wait")


time.sleep(5)


for i in range(amount):
    pyautogui.moveTo(959, 610)
    webbrowser.open_new('https://kahoot.it/') 
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.typewrite(code)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.click()
    pyautogui.typewrite(name)
    pyautogui.typewrite(str(x))
    pyautogui.press('enter')
    x = x + 1


print("Flood Complete")
time.sleep(95)
print("Terminating Script")
time.sleep(5)
sys.exit()
