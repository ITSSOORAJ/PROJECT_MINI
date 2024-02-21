import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import threading
import shutil
'''from facerec import *
from register import *
from dbHandler import *'''

active_page = 0
thread_event = None
left_frame = None
right_frame = None
heading = None
webcam = None
img_label = None
img_read = None
img_list = []
slide_caption = None
slide_control_panel = None
current_slide = -1

root = tk.Tk()
root.geometry("1450x750+150+90")

pages = []
for i in range(4):
    pages.append(tk.Frame(root, bg="#202d42"))
    pages[i].pack(side="top", fill="both", expand=True)
    pages[i].place(x=0, y=0, relwidth=1, relheight=1)
    
def goBack():
    global active_page, thread_event, webcam

    if (active_page==3 and not thread_event.is_set()):
        thread_event.set()
        webcam.release()

    for widget in pages[active_page].winfo_children():
        widget.destroy()

    pages[0].lift()
    active_page = 0
    
def basicPageSetup(pageNo):
    global left_frame, right_frame, heading
    content = tk.Frame(pages[pageNo], bg="#202d42", pady=20)
    content.pack(expand="true", fill="both")

    '''left_frame = tk.Frame(content, bg="#202d42")
    left_frame.grid(row=0, column=0, sticky="nsew")'''
    left_frame = tk.LabelFrame(content, text="Detected Criminals", bg="#202d42", font="Arial 20 bold", bd=4,
                             foreground="#2ea3ef", labelanchor="n")
    left_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    right_frame = tk.LabelFrame(content, text="Detected Criminals", bg="#202d42", font="Arial 20 bold", bd=4,
                             foreground="#2ea3ef", labelanchor="n")
    right_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

    content.grid_columnconfigure(0, weight=1, uniform="group1")
    content.grid_columnconfigure(1, weight=1, uniform="group1")
    content.grid_rowconfigure(0, weight=1)

def getPage2():
    global active_page, left_frame, right_frame, img_label, heading
    img_label = None
    active_page = 2
    pages[2].lift()

    basicPageSetup(2)
    left_frame.configure(text="FACE1")
    right_frame.configure(text="FACE2")
    
    btn_grid = tk.Frame(left_frame, bg="#202d42")
    btn_grid1 = tk.Frame(right_frame,bg="#202d42")
    btn_grid.pack()
    btn_grid1.pack()

   

    '''tk.Button(btn_grid, text="Recognize", font="Arial 15 bold", padx=20, bg="#2196f3",
           fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
           activeforeground="white").grid(row=0, column=1, padx=25, pady=25)
    
    
    tk.Button(btn_grid1, text="Capture Image", font="Arial 15 bold", padx=20, bg="#2196f3",
            fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
            activeforeground="white").grid(row=0, column=1, padx=25, pady=25)

    tk.Button(btn_grid1, text="Recognize", font="Arial 15 bold", padx=20, bg="#2196f3",
           fg="white", pady=10, bd=0, highlightthickness=0, activebackground="#091428",
           activeforeground="white").grid(row=0, column=0, padx=25, pady=25)'''
    first_button = tk.Button(btn_grid, text="Capture Image", font="Arial 15 bold", padx=20, bg="#2196f3",
         fg="white", pady=10, bd=10, highlightthickness=0, activebackground="#091428",
         activeforeground="white")
    second_button = tk.Button(btn_grid, text="Recognize", font="Arial 15 bold", padx=20, bg="#2196f3",
         fg="white", pady=10, bd=10, highlightthickness=0, activebackground="#091428",
         activeforeground="white")

    second_button.pack(side="bottom", padx=25, pady=25)
    first_button.pack(side="bottom", padx=25, pady=25)

    first_button1 = tk.Button(btn_grid1, text="Capture Image", font="Arial 15 bold", padx=20, bg="#2196f3",
         fg="white", pady=10, bd=10, highlightthickness=0, activebackground="#091428",
         activeforeground="white")
    second_button1 = tk.Button(btn_grid1, text="Recognize", font="Arial 15 bold", padx=20, bg="#2196f3",
         fg="white", pady=10, bd=10, highlightthickness=0, activebackground="#091428",
         activeforeground="white")

    second_button1.pack(side="bottom", padx=25, pady=25)
    first_button1.pack(side="bottom", padx=25, pady=25)



    

    




tk.Label(pages[0], text="Facera", fg="white", bg="#202d42",
      font="Arial 35 bold", pady=30).pack()

logo = tk.PhotoImage(file = "logo.png")
tk.Label(pages[0], image=logo, bg="#202d42").pack()

btn_frame = tk.Frame(pages[0], bg="#202d42", pady=30)
btn_frame.pack()
'''tk.Button(btn_frame, text="Register Criminal", command=getPage1)
tk.Button(btn_frame, text="Detect Criminal", command=getPage2)
tk.Button(btn_frame, text="Video Surveillance", command=getPage3)'''#this was actual button format 

tk.Button(btn_frame, text="RECOG/SIMIL",command=getPage2)
tk.Button(btn_frame, text="CREATE DATA SET")

for btn in btn_frame.winfo_children():
    btn.configure(font="Arial 20", width=17, bg="#2196f3", fg="white",
        pady=15, bd=0, highlightthickness=0, activebackground="#091428", activeforeground="white")
    btn.pack(pady=30)



pages[0].lift()
root.mainloop()