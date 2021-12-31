from tkinter import *

numbers = "1234567890"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def input1():
    root1 = Tk()
    sc1 = Label(root1, text="Enter the amount to shift by: ")
    sc1.grid(column=0, row=0)
    entry = Entry(root1)
    entry.grid(column=1, row=0)
    sc2 = Label(root1, text="Enter the message to shift: ")
    sc2.grid(column=0, row=1)
    entry1 = Entry(root1)
    entry1.grid(column=1, row=1)

    def shiftcipher():
        newmessage = ""
        shift = entry.get()
        message = entry1.get()
        for x in range(len(message)):
            if message[x].isalpha():
                location = alphabet.find(message[x])
                location1 = location + int(shift)
                if location < 26 and location1 > 25:
                    location1 = location1 % 26
                elif location > 25 and location1 > 51:
                    location1 = location1 % 26 + 26
                elif location < 26 and location1 < 0:
                    location1 = location1 % 26
                    location1 = 25 - location1
                elif location > 25 and location1 < 26:
                    location1 = location1 % 26
                    location1 = 51 - location1
                newmessage = newmessage + alphabet[location1]
            else:
                location = numbers.find(message[x])
                location1 = location + int(shift)
                if location1 > 9:
                    location1 = location1 % 10
                if location1 < 0:
                    location1 = location1 % 10
                    location = 9 - location1
                newmessage = newmessage + numbers[location]
        answer = Label(root1, text=newmessage)
        answer.grid(column=2, row=2)
    btn = Button(root1, text="RUN", command=shiftcipher)
    btn.grid(column=1, row=2)
    root1.mainloop()


def input2():
    root2 = Tk()
    sc1 = Label(root2, text="Enter the word to shift by: ")
    sc1.grid(column=0, row=0)
    entry = Entry(root2)
    entry.grid(column=1, row=0)
    sc2 = Label(root2, text="Enter the message to shift: ")
    sc2.grid(column=0, row=1)
    entry1 = Entry(root2)
    entry1.grid(column=1, row=1)

    def vigenerecipher():
        newmessage = ""
        shift = entry.get()
        message = entry1.get()
        a = 0
        for x in range(len(message)):
            if message[x] != " ":
                if message[x].isalpha():
                    location = alphabet.find(message[x])
                    location1 = location + alphabet.find(shift[a])
                    if location < 26 and location1 > 25:
                        location1 = location1 % 26
                    elif location > 25 and location1 > 51:
                        location1 = location1 % 26 + 26
                    newmessage = newmessage + alphabet[location1]
                    if a == len(shift) - 1:
                        a = 0
                    else:
                        a += 1
                else:
                    location = numbers.find(message[x])
                    location1 = location + alphabet.find(shift[a])
                    if location1 > 9:
                        location1 = location1 % 10
                    newmessage = newmessage + numbers[location1]
                    if a == len(shift) - 1:
                        a = 0
                    else:
                        a += 1
            else:
                newmessage = newmessage + " "
        answer = Label(root2, text=newmessage)
        answer.grid(column=2, row=2)
    btn = Button(root2, text="RUN", command=vigenerecipher)
    btn.grid(column=1, row=2)
    root2.mainloop()


def input3():
    root3 = Tk()
    sc1 = Label(root3, text="Enter the amount of rows to shift by: ")
    sc1.grid(column=0, row=0)
    entry = Entry(root3)
    entry.grid(column=1, row=0)
    sc2 = Label(root3, text="Enter the message to shift: ")
    sc2.grid(column=0, row=1)
    entry1 = Entry(root3)
    entry1.grid(column=1, row=1)

    def railfencecipher():
        shift = entry.get()
        message = entry1.get()
        arr = []
        a = 1
        b = 0
        newmessage = ""
        for x in range(int(shift)):
            arr.append([])
        for y in range(len(message)):
            arr[b].append(message[y])
            if b > int(shift) - 2:
                a = -1
            elif b < 1:
                a = 1
            b += a
        for c in range(len(arr)):
            for d in range(len(arr[c])):
                newmessage = newmessage + arr[c][d]
        answer = Label(root3, text=newmessage)
        answer.grid(column=2, row=2)
    btn = Button(root3, text="RUN", command=railfencecipher)
    btn.grid(column=1, row=2)
    root3.mainloop()


def input4():
    root4 = Tk()
    sc2 = Label(root4, text="Enter the message to shift: ")
    sc2.grid(column=0, row=0)
    entry1 = Entry(root4)
    entry1.grid(column=1, row=0)

    def bruteforce():
        newmessage = ""
        message = entry1.get()
        for y in range(1, 26):
            for x in range(len(message)):
                if message[x] != " ":
                    if message[x].isalpha():
                        location = alphabet.find(message[x])
                        location1 = location + y
                        if location < 26 and location1 > 25:
                            location1 = location1 % 26
                        elif location > 25 and location1 > 51:
                            location1 = location1 & 26 + 26
                        newmessage = newmessage + alphabet[abs(location1)]
                    else:
                        location = numbers.find(message[x])
                        location1 = location + y
                        if location1 > 9:
                            location1 = location1 % 10
                        newmessage = newmessage + numbers[abs(location1)]
                else:
                    newmessage = newmessage + " "
            newmessage = newmessage + " "
        answer = Label(root4, text=newmessage)
        answer.grid(column=2, row=2)
    btn = Button(root4, text="RUN", command=bruteforce)
    btn.grid(column=1, row=2)
    root4.mainloop()


def leave():
    exit()


def main():
    root = Tk()
    shift = Button(root, text="Shift Cipher", command=input1)
    shift.grid(column=0, row=0)
    vigenere = Button(root, text="Vigenere Cipher", command=input2)
    vigenere.grid(column=1, row=0)
    railfence = Button(root, text="Railfence Cipher", command=input3)
    railfence.grid(column=2, row=0)
    bruteforce = Button(root, text="Brute Force Shift Cipher", command=input4)
    bruteforce.grid(column=0, row=1)
    lv = Button(root, text="Exit", command=leave)
    lv.grid(column=1, row=1)
    root.mainloop()


def login():
    root5 = Tk()
    sc2 = Label(root5, text="Password: ")
    sc2.grid(column=0, row=0)
    entry1 = Entry(root5)
    entry1.grid(column=1, row=0)

    def password():
        code = "private"
        entry = entry1.get()
        if code != entry:
            answer = Label(root5, text="The password you entered is incorrect.")
            answer.grid(column=1, row=2)
        else:
            main()
    enter = Button(root5, text="Enter", command=password)
    enter.grid(column=1, row=1)
    root5.mainloop()


login()
