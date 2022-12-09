import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
root.title('Screenshot')


canvas = tk.Canvas(root, width = 300 , heigh = 300)
canvas.pack()

def takeScreenShort():
    myScreenShot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myScreenShort.save(save_path + "screenshot.png")


myButton = tk.Button(text = "Taka ScreenShot", command = takeScreenShort, font = 5)
canvas.create_window(150,150, window =  myButton)

root.mainloop()
