import sys, re, os, pyautogui, time, keyboard
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox


root = Tk(className="theMacroToolkit")
root.geometry("300x320")
root.iconbitmap('./favicon.ico')

#VARIABLES
commands = [ "help", "autoClicker", "preciseClicker",  "autoClickOnPosition", "getMousePosition", "write", "taco", "tacoAuto"]
command = StringVar()
command.set("help")

buttons = ["left", "right", "middle"]
bInput = StringVar()
bInput.set(buttons[0])

key = 'left shift'

#MACRO FUNCTIONS
def error():
    messagebox.showwarning("Invalid Inputs", "Please fill in all inputs correctly")
    reset(True)

def autClicker(d, b, i):
    time.sleep(d)
    click = True
    while click is True:
        if keyboard.is_pressed(key):
            click = False
            reset(True)
        else:
            pyautogui.click(button=b)
            time.sleep(i)

def preciseClicker(x, y, d, b, i):
    time.sleep(d)
    click = True
    while click is True:
        if keyboard.is_pressed(key):
            click = False
            reset(True)
        else:
            pyautogui.click(button=b, x=x, y=y)
            time.sleep(i)

def getMousePosition(d):
    time.sleep(d)
    xMouse, yMouse = pyautogui.position()
    messagebox.showinfo("Mouse position", f"({xMouse},{yMouse})")
    reset(True)

def autoClickOnPosition(d, i, b):
    click = True
    time.sleep(d)
    x, y = pyautogui.position()
    while click is True:
        if keyboard.is_pressed(key):
            click = False
            reset(True)
        else:
            pyautogui.click(button=b, x=x, y=y)
            time.sleep(i)

def write(s, a, i, d):
    time.sleep(d)
    while a != 0:
        if keyboard.is_pressed(key):
            click = False
            reset(True)
        else:
            pyautogui.write(s, interval=0.01)
            enter(i)
            a -= 1
    reset(True)

def taco(d):
    while d != 0:
        print(d)
        time.sleep(1)
        d -= 1
    tacoCommands = ["-w", "-t", "-ot", "-clean", "-buy karaoke", "-buy airplane", "-buy chef", "-buy music", "-buy flipper"]
    for i in range(len(tacoCommands)):
        pyautogui.write(tacoCommands[i], interval=0.01)
        enter(1.5)
        i += 1
    reset(True)

def tacoAuto(d):
    while d != 0:
        print(d)
        time.sleep(1)
        d -= 1
    play = True
    t = 0
    while play is True:
        if keyboard.is_pressed('end'):
            play = False
            main()
            break
        else:
            if t % 5 == 0:
                pyautogui.write("-t", interval=0.1)
                enter(1.5)
            if t % 10 == 0:
                pyautogui.write("-w", interval=0.1)
                enter(1.5)
            if t % 30 == 0:
                pyautogui.write("-ot", interval=0.1)
                enter(1.5)
            t += 1
            time.sleep(61)

#UI FUNCTIONS
def enter(t):
    keyboard.press("enter")
    keyboard.release("enter")
    time.sleep(t)

def clear(s):
    for i in s.winfo_children():
        i.destroy()

def reset(s=False):
    ans = 0
    if not s:
        ans = messagebox.askyesno("Reset?", "Are you sure you want to reset the window?")
    if ans == 1 or s:
        dropDown.config(state='normal')
        command.set("help")
        inputs = [xIn, yIn, iIn, dIn, bIn, aIn, sIn]
        for x in inputs:
            if x != bIn:
                x.delete(0, 'end')
            else:
                x.config(bg="SystemButtonFace")
            x.config(state=DISABLED)
        runBtn.config(text="Select", command=dropGet)
        main()

def callbackFloat(P):
    if P.replace('.', '', 1).isdigit() or P == "":
        return True
    else:
        return False

def callbackInt(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False

def conversionHandler(x=None, y=None, string=None, inv=None, delay=None, button=None, amount=None, function=None):
    try:
        if x is not None:
            x = int(x)
        if y is not None:
            y = int(y)
        if string is not None:
            string = str(string)
        if inv is not None:
            inv = float(inv)
        if delay is not None:
            delay = int(delay)
        if button is not None:
            button = str(button)
        if amount is not None:
            amount = int(amount)
    except (TypeError, ValueError):
        error()
        return
    finally:
        if function is None:
            messagebox.showwarning("No Function", "Something Internally Went Wrong")
            reset()
            return
        else:
            if function == "autoClicker":
                autClicker(delay, button, inv)
            if function == "preciseClicker":
                preciseClicker(x, y, delay, button, inv)
            if function == "autoClickOnPosition":
                autoClickOnPosition(delay, inv, button)
            if function == "getMousePosition":
                getMousePosition(delay)
            if function == "write":
                write(string, amount, inv, delay)
            if function == "taco":
                taco(delay)
            if function == "tacoAuto":
                tacoAuto(delay)

def dropGet():
    exe = command.get()
    if exe == "help":
        dropDown.config(state=DISABLED)
        runBtn.config(text="Run", command=helpL)
        print(exe)
        return
    if exe == "autoClicker":
        commandHandler(False, False, True, True, True, False)
        dropDown.config(state=DISABLED)
        runBtn.config(text="Run", command=lambda: conversionHandler(None, None, None, iIn.get(), dIn.get(), bInput.get(), None, exe))
        print(exe)
        return
    if exe == "preciseClicker":
        commandHandler(True, False, True, True, True, False)
        dropDown.config(state=DISABLED)
        runBtn.config(text="Run", command=lambda: conversionHandler(xIn.get(), yIn.get(), None, iIn.get(), dIn.get(), bInput.get(), None, exe))
        print(exe)
        return
    if exe == "autoClickOnPosition":
        commandHandler(False, False, True, True, True, False)
        dropDown.config(state=DISABLED)
        runBtn.config(text="Run", command=lambda: conversionHandler(None, None, None, iIn.get(), dIn.get(),  bInput.get(), None, exe))
        print(exe)
        return
    if exe == "getMousePosition":
        commandHandler(False, False, False, True, False, False)
        dropDown.config(state=DISABLED)
        runBtn.config(text="Run", command=lambda: conversionHandler(None, None, None, None, dIn.get(), None, None, exe))
        print(exe)
        return
    if exe == "write":
        commandHandler(False, True, True, True, False, True)
        dropDown.config(state=DISABLED)
        runBtn.config(text="Run", command=lambda: conversionHandler(None, None, sIn.get(), iIn.get(), dIn.get(), None, aIn.get(), exe))
        print(exe)
        return
    if exe == "taco":
        commandHandler(False, False, False, True, False, False)
        dropDown.config(state=DISABLED)
        runBtn.config(text="Run", command=lambda: conversionHandler(None, None, None, None, dIn.get(), None, None, exe))
        print(exe)
        return
    if exe == "tacoAuto":
        commandHandler(False, False, False, True, False, False)
        dropDown.config(state=DISABLED)
        runBtn.config(text="Run", command=lambda: conversionHandler(None, None, None, None, dIn.get(), None, None, exe))
        print(exe)
        return
def commandHandler(pos=False, string=False, inv=False, delay=False, btn=False, amount=False):
    if pos is True:
        xIn.config(state='normal')
        yIn.config(state='normal')
    if string is True:
        sIn.config(state='normal')
    if inv is True:
        iIn.config(state='normal')
    if delay is True:
        dIn.config(state='normal')
    if btn is True:
        bIn.config(state='normal', bg='white')
    if amount is True:
        aIn.config(state='normal')


#FRAMES
frame = Frame(root, relief='flat', bd=1)

#VALIDATION
vcmdF = root.register(callbackFloat)
vcmdI = root.register(callbackInt)
#FONTS
fontFooter = tkFont.Font(family="Consolas", size=8)
generalFont = tkFont.Font(family="Calibria", size=9)

#LABELS
titleLabel = Label(frame, text="Command : ", font=generalFont)
dropDown = OptionMenu(frame, command, *commands)
runBtn = Button(frame, text="Select", padx=18, borderwidth=1, relief="ridge", font=generalFont, command=lambda: dropGet())
clearBtn = Button(frame, text="Reset", padx=20, borderwidth=1, relief="ridge", font=generalFont, command=lambda: reset())
footer = Label(root, text=f"theMacroToolkit/Select-Created by H8rs", bd=1, relief=SUNKEN, anchor=E, padx=8, font=fontFooter)
xLabel = Label(frame, text="X coord    ", font=generalFont)
yLabel = Label(frame, text="Y coord    ", font=generalFont)
iLabel = Label(frame, text="Interval   ", font=generalFont)
dLabel = Label(frame, text="Delay      ", font=generalFont)
bLabel = Label(frame, text="Button     ", font=generalFont)
aLabel = Label(frame, text="Amount     ", font=generalFont)
sLabel = Label(frame, text="String     ", font=generalFont)
xIn = Entry(frame, validate='all', validatecommand=(vcmdI, '%P'), state=DISABLED)
yIn = Entry(frame, validate='all', validatecommand=(vcmdI, '%P'), state=DISABLED)
iIn = Entry(frame, validate='all', validatecommand=(vcmdF, '%P'), state=DISABLED)
dIn = Entry(frame, validate='all', validatecommand=(vcmdI, '%P'), state=DISABLED)
bIn = OptionMenu(frame, bInput, *buttons)
bIn.config(state=DISABLED, padx=5)
aIn = Entry(frame, validate='all', validatecommand=(vcmdI, '%P'), state=DISABLED)
sIn = Entry(frame, state=DISABLED)


#SCREEN FUNCTIONS
def helpL():
    commandList = Tk(className="Help List")
    commandList.geometry("880x270")
    commandList.resizable(False, False)
    commandList.iconbitmap('./favicon.ico')
    #Frame
    frame = LabelFrame(commandList, text="Commands", padx=5, pady=5)
    frame.pack(fill='both', expand=True, padx=10, pady=10)
    #Labels
    Label(frame, text="help :", padx=15, pady=3, justify="left").place(x=100, y=10)
    Label(frame, text="autoClicker :", padx=15, pady=3, justify="left").place(x=63, y=35)
    Label(frame, text="preciseClicker :", padx=15, pady=3, justify="left").place(x=50, y=60)
    Label(frame, text="autoClickOnPosition :", padx=15, pady=3, justify="left").place(x=15, y=85)
    Label(frame, text="getMousePosition :", padx=15, pady=3, justify="left").place(x=27, y=110)
    Label(frame, text="write :", padx=15, pady=3, justify="left").place(x=98, y=135)
    Label(frame, text="taco :", padx=15, pady=3, justify="left").place(x=100, y=160)
    Label(frame, text="tacoAuto :", padx=15, pady=3, justify="left").place(x=75, y=185)
    #Description
    Label(frame, text="Creates a window with this list", pady=3, justify="left").place(x=150, y=10)
    Label(frame, text="Automatically clicks at the current position of the mouse | Takes in interval, start delay, and button", pady=3, justify="left").place(x=150, y=35)
    Label(frame, text="Automatically clicks at a set position | Takes in x, y, interval, start delay, and button", pady=3, justify="left").place(x=150, y=60)
    Label(frame, text="Automatically clicks at the position of the mouse after the start delay ends | Takes in interval, start delay, and button", pady=3, justify="left").place(x=150, y=85)
    Label(frame, text="Gives the X and Y coords of the mouse after the start delay ends | Takes in start delay", pady=3, justify="left").place(x=150, y=110)
    Label(frame, text="Automatically types a given string, a set amount of times, at regular intervals | Takes in string, amount, interval, and start delay", pady=3, justify="left").place(x=150, y=135)
    Label(frame, text="Buys all boosts and completes tasks for the taco shack discord bot | Takes in start delay", pady=3, justify="left").place(x=150, y=160)
    Label(frame, text="AFK bot which times and completes the core task for the taco shack discord bot | Takes in start delay", pady=3, justify="left").place(x=150, y=185)
    #Button
    Button(commandList, text="Exit", command=commandList.destroy, borderwidth=1, relief="ridge", padx=13).place()
    commandList.mainloop()


def main():
    frame.pack(fill='both', expand=True, padx=10, pady=10)
    # DropDownCommand
    titleLabel.place(x=15, y=15)
    dropDown.place(x=100, y=10)
    dropDown.config(width=16, borderwidth=1, relief="ridge", font=generalFont)
    #Positionals
    xLabel.place(x=35, y=53)
    yLabel.place(x=35, y=78)
    xIn.place(x=95, y=53)
    yIn.place(x=95, y=78)
    #Timings
    iLabel.place(x=35, y=103)
    dLabel.place(x=35, y=128)
    iIn.place(x=95, y=103)
    dIn.place(x=95, y=128)
    #Amount
    aLabel.place(x=35, y=153)
    aIn.place(x=95, y=153)
    #Button
    bLabel.place(x=35, y=178)
    bIn.place(x=93, y=173)
    bIn.config(relief="ridge", borderwidth=1, width=14)
    #String
    sLabel.place(x=35, y=203)
    sIn.place(x=95, y=203)
    #Buttons
    runBtn.place(y=248, x=50)
    clearBtn.place(y=248, x=140)
    #Footer
    footer.pack()
    footer.config(width=300)


main()
root.update()
#Loop
root.resizable(False, False)
root.mainloop()
