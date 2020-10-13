import tkinter as tk
from PIL import Image, ImageTk
import os


def ButtonCLick(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        v = scvalue.get()
        if v.isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        # print(scvalue.get())
        screen.update()
    elif text == "C":
        scvalue.set(" ")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


root = tk.Tk()
root.title("CALCULATOR BY YD")
root.wm_iconbitmap("Icon.ico")
root.geometry("800x530")
root.minsize(400, 530)
root.maxsize(400, 530)
CanvasScreenFrame = tk.Canvas(root, height=200, width=200, bg="black")
CanvasScreenFrame.pack()

# taking image for background of screen
img = Image.open("t3.jpg")
resized = img.resize((900, 300))
bgimage = ImageTk.PhotoImage(image=resized)
bgframe = tk.Label(CanvasScreenFrame, image=bgimage)
bgframe.place(x=0, y=0, relwidth=1, relheight=1)

# Actual screen for output
scvalue = tk.StringVar()
scvalue.set("")
screen = tk.Entry(CanvasScreenFrame, textvar=scvalue, font="Consolas 30 bold",
                  bg="black", fg="white")
screen.pack(ipadx=280, ipady=30, pady=50, padx=20)


def GUI():
    # Tk initialization and window attributes setting

    # root.mainloop()
    # quit()
    # ButtonMainFrame
    # Making Canvas for the Buttons Screen
    ButtonScreenCanvas = tk.Canvas(
        root, height=300, width=400)
    ButtonScreenCanvas.pack(fill="x")

    # Canvas Background
    img22 = Image.open("t4.jpg")
    resized22 = img22.resize((1600, 1200))
    bgimage22 = ImageTk.PhotoImage(resized22)
    bgButton2 = tk.Label(ButtonScreenCanvas, image=bgimage22)
    bgButton2.place(x=0, y=0, relwidth=1, relheight=1)

    # Makking Button Frame
    # ButtonFrame = tk.Frame(ButtonScreenCanvas, borderwidth=2, bg="black",
    #                        relief="groove")
    # ButtonFrame.pack(anchor="nw", side="bottom", pady=20, padx=35)

    # Making Buttons
    b1 = tk.Button(ButtonScreenCanvas, text="9", bg="orange", fg="white",
                   font="FranklingGothic 12 bold", padx=15, pady=14)
    b1.pack(side="left", padx=20, pady=7)
    b1.bind("<Button-1>", ButtonCLick)

    b2 = tk.Button(ButtonScreenCanvas, text="8", bg="orange", fg="white",
                   font="FranklingGothic 12 bold", padx=15, pady=14)
    b2.pack(side="left", padx=20, pady=7)
    b2.bind("<Button-1>", ButtonCLick)

    b5 = tk.Button(ButtonScreenCanvas, text="7", bg="orange", fg="white",
                   font="FranklingGothic 12 bold", padx=15, pady=14)
    b5.pack(side="left", padx=20, pady=7)
    b5.bind("<Button-1>", ButtonCLick)

    b6 = tk.Button(ButtonScreenCanvas, font="FranklingGothic 12 bold",
                   text="+",  bg="yellow", fg="red", padx=15, pady=14)
    b6.pack(side="left", padx=20, pady=7)
    b6.bind("<Button-1>", ButtonCLick)
######################################################
    ButtonScreenCanvas1 = tk.Canvas(root, height=300, width=400)
    ButtonScreenCanvas1.pack(fill="x")

    # Canvas Background
    img21 = Image.open("smoke1.jpg")
    resized21 = img21.resize((1600, 1200))
    bgimage21 = ImageTk.PhotoImage(resized21)
    bgButton1 = tk.Label(ButtonScreenCanvas1, image=bgimage21)
    bgButton1.place(x=0, y=0, relwidth=1, relheight=1)

    b7 = tk.Button(ButtonScreenCanvas1, text="6", bg="orange", fg="white",
                   font="FranklingGothic 12 bold", padx=15, pady=14)
    b7.pack(side="left", padx=20, pady=7)
    b7.bind("<Button-1>", ButtonCLick)

    b8 = tk.Button(ButtonScreenCanvas1, text="5", bg="orange", fg="white",
                   font="FranklingGothic 12 bold", padx=15, pady=14)
    b8.pack(side="left", padx=20, pady=7)
    b8.bind("<Button-1>", ButtonCLick)

    b9 = tk.Button(ButtonScreenCanvas1, font="FranklingGothic 12 bold",
                   text="4", bg="orange", fg="white", padx=15, pady=14)
    b9.pack(side="left", padx=20, pady=7)
    b9.bind("<Button-1>", ButtonCLick)

    b10 = tk.Button(ButtonScreenCanvas1, text="-",  bg="yellow", fg="red",
                    font="FranklingGothic 12 bold", padx=17, pady=14)
    b10.pack(side="left", padx=20, pady=7)
    b10.bind("<Button-1>", ButtonCLick)
    #######################
    ButtonScreenCanvas3 = tk.Canvas(
        root, height=300, width=400)
    ButtonScreenCanvas3.pack(fill="x")

    # Canvas Background
    img2 = Image.open("smoke2.jpg")
    resized2 = img2.resize((1600, 1200))
    bgimage2 = ImageTk.PhotoImage(resized2)
    bgButton = tk.Label(ButtonScreenCanvas3, image=bgimage2)
    bgButton.place(x=0, y=0, relwidth=1, relheight=1)

    b11 = tk.Button(ButtonScreenCanvas3, text="3", bg="orange", fg="white",
                    font="FranklingGothic 12 bold", padx=15, pady=14)
    b11.pack(side="left", padx=20, pady=7)
    b11.bind("<Button-1>", ButtonCLick)
    b12 = tk.Button(ButtonScreenCanvas3, font="FranklingGothic 12 bold",
                    text="2", bg="orange", fg="white", padx=15, pady=14)
    b12.pack(side="left", padx=20, pady=7)
    b12.bind("<Button-1>", ButtonCLick)
    b13 = tk.Button(ButtonScreenCanvas3, text="1", bg="orange", fg="white",
                    font="FranklingGothic 12 bold", padx=15, pady=14)
    b13.pack(side="left", padx=20, pady=7)
    b13.bind("<Button-1>", ButtonCLick)
    b14 = tk.Button(ButtonScreenCanvas3, font="FranklingGothic 12 bold",
                    text="*",  bg="yellow", fg="red", padx=14, pady=14)
    b14.pack(side="left", padx=20, pady=7)
    b14.bind("<Button-1>", ButtonCLick)
    ButtonScreenCanvas4 = tk.Canvas(
        root, height=300, width=400)
    ButtonScreenCanvas4.pack(fill="x")
    # Canvas Background
    img3 = Image.open("t4.jpg")
    resized3 = img3.resize((1600, 1200))
    bgimage3 = ImageTk.PhotoImage(resized3)
    bgButton3 = tk.Label(ButtonScreenCanvas4, image=bgimage3)
    bgButton3.place(x=0, y=0, relwidth=1, relheight=1)

    b15 = tk.Button(ButtonScreenCanvas4, text="/", bg="yellow", fg="red",
                    font="FranklingGothic 12 bold", padx=17, pady=14)
    b15.pack(side="left", padx=20, pady=7)
    b15.bind("<Button-1>", ButtonCLick)
    b16 = tk.Button(ButtonScreenCanvas4, font="FranklingGothic 12 bold",
                    text="0", bg="orange", fg="white", padx=15, pady=14)
    b16.pack(side="left", padx=20, pady=7)
    b16.bind("<Button-1>", ButtonCLick)
    b17 = tk.Button(ButtonScreenCanvas4, text="C", bg="red", fg="white",
                    font="FranklingGothic 12 bold", padx=13, pady=14)
    b17.pack(side="left", padx=20, pady=7)
    b17.bind("<Button-1>", ButtonCLick)
    b18 = tk.Button(ButtonScreenCanvas4, font="FranklingGothic 12 bold",
                    text="=", bg="blue", fg="white", padx=15, pady=14)
    b18.pack(side="left", padx=20, pady=7)
    b18.bind("<Button-1>", ButtonCLick)
    tk.Label(root, text="copyright 2020", bg="black",
             fg="white", font="consolas 12").pack(side="bottom", anchor="s", fill="x")
    root.mainloop()


if __name__ == "__main__":
    GUI()
