#coding: utf-8

from tkinter import Tk
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import Text
from tkinter import END
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror

word = "book"
rletters = list(word)
board = ["_"] * len(word)
wrong = 0
stage = ["",\
         "_____     ",\
         "     |    ",\
         "     |    ",\
         "     ○    ",\
         "    |||    ",\
         "    | |  ",\
         "___________"]
count = len(stage)
count2 = len(word)

def hangman():
    #word = "cat"
    #rletters = list(word)
    #board = ["_"] * len(word)
    #wrong = 0
    #stage = ["",\
    #         "_____     ",\
    #         "     |    ",\
    #         "     |    ",\
    #         "     ○    ",\
    #         "    /|\\    ",\
    #         "    / \\    ",\
    #         "___________"]
    #count = len(stage)
    #print("Welcome to Hangman!!")

    global word, rletters, board, wrong, stage, count
    frag = False
    char = input.get()

    if len(char) != 1:
        showerror("ERROR!", "need 1 alphabet!")
    else:
        frag = True

    if frag == True:
        #print("\n")
        #startmsg = "enter a letter >>>"

        if char in rletters:
            cling = rletters.index(char)
            board[cling] = char
            rletters[cling] = "$"
        else:
            wrong += 1

        msg.insert(END, " ".join(board) +"\n")

        e = wrong + 1
        msg.insert(END, "\n".join(stage[0:e]))#"[0:e]まではeの一つ下の数まで表示する
        msg.insert(END, "\n")

        if "_" not in board:
            showinfo("CONGRATU!","you win!\n" + "the answer was {}".format("".join(board)))
            app.destroy()

        if wrong == (count - 1):
            msg.insert(END, "\n".join(stage))
            showinfo("SORRY", "you lose.\n" + "the answer was {}".format(word))
            app.destroy()

app = Tk()
app.geometry("600x400")
app.title("THE HANGMAN")

button = Button(app, text = "CHECK", font = ("Meiryo UI", 14), command = hangman)
button.place(x = 240, y = 95)

input = Entry(width = 1, font = ("Meiryo", 16))
input.place(x = 200, y = 100)

text = Label(app, text = "give one alphabet", font = ("Meiryo UI", 14))
text.place(x = 20, y = 100)

text2 = Label(app, text = "Welcome to Hangman!!", font = ("Meiryo UI", 14))
text2.place(x = 20, y = 30)

text3 = Label(app, text = "(the word has {} letters.)".format(count2),\
              font = ("Meiryo UI", 14))
text3.place(x = 20, y = 150)

msg = Text(app, font = ("Meiryo UI", 10))
msg.place(x = 400, y = 0, height = 400, width = 200)

app.mainloop()