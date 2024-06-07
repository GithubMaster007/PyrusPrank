import tkinter as tk
import time
import pyautogui
import os, sys
from PIL import Image, ImageTk
import  winsound



time.sleep(5)

dir = os.path.dirname(os.path.abspath(sys.argv[0]))
print(dir)

pyautogui.hotkey("win", "d")

time.sleep(0.7)

im = pyautogui.screenshot("desktop.png")

root = tk.Tk()

root.geometry("{}x{}+0+0".format(root.winfo_screenwidth(),
                                 root.winfo_screenwidth()))

bg = tk.PhotoImage(file="desktop.png")

bgimage = tk.Label(root, image=bg, width=root.winfo_screenwidth(),
                   height=root.winfo_screenheight(), borderwidth=0)

bgimage.place(x=0, y=0)

def toggle_geom():
    pass
ISRUN = False
TOTALLOOP = 0


def updateImg(number, sleepNum):

    imgName = dir+"/bsod" + str(number) + ".png"

    img = Image.open(imgName).resize(
        (root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)

    bg1 = ImageTk.PhotoImage(img)

    bgimage.configure(image=bg1, cursor='none')
    bgimage.image = bg1
    root.update()
    time.sleep(sleepNum)

def initiate(e):

    global ISRUN

    if ISRUN == False:
        ISRUN = True
        time.sleep(1)
        updateImg(1, 3)
        updateImg(2, 4)
        updateImg(3, 4.5)
        updateImg(4, 0.1)
        winsound.PlaySound(dir+'/noise1.waw', winsound.SND_ASYNC)
        updateImg(3, 3)
        winsound.PlaySound(dir + '/noise2.waw', winsound.SND_ASYNC)
        updateImg(6, 0.02)
        updateImg(3, 0.1)
        winsound.PlaySound(dir + '/noise3.waw', winsound.SND_ASYNC)
        updateImg(4, 0.02)
        updateImg(3, 0.1)
        winsound.PlaySound(dir + '/final.waw', winsound.SND_ASYNC)
        updateImg(5, 3)
        winsound.PlaySound(dir + '/loop.waw', winsound.SND_ASYNC)

        root.after(0, update, 0)

def update(ind):
    global TOTALLOOP

    if ind == 80:
        ind = 0
        TOTALLOOP += 1

    if ind < 10:
        indText = "0" + str(ind)
    else:
        indText = str(ind)

    directoryName = dir+"/frame_" + indText + "_delay-0.05s.png"

    img = Image.open(directoryName).resize(
        (root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)

    bg2 = ImageTk.PhotoImage(img)

    bgimage.configure(image=bg2)
    bgimage.image = bg2
    root.update()
    ind+= 1

    if TOTALLOOP < 4:
        root.after(5, update, ind)
    else:
        img = Image.open(dir+"/bsod7.png").resize(
            (root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)

        bg1 = ImageTk.PhotoImage(img)

        bgimage.configure(image=bg1)
        bgimage.image = bg1
        root.update()
        winsound.PlaySound(None,winsound.SND_ASYNC)
        time.sleep(4)




bgimage.bind('<Button-1>', initiate)
root.attributes("-fullscreen", True)
root.bind('<Escape>', toggle_geom)
root.attributes('-topmost', True)
root.bind('<Alt-F4>', toggle_geom)
root.protocol("WM_DELETE_WINDOW", toggle_geom)

root.update()
root.mainloop()



