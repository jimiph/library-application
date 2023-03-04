from tkinter import *
import backend

window = Tk()

############## Alt + Shift + Down or Up is a useful keyword
# ===================== Labels ======================
l1 = Label(window, text='Title')
l1.grid(row=0, column=0)

l2 = Label(window, text='Author')
l2.grid(row=0, column=2)

l3 = Label(window, text='Year')
l3.grid(row=1, column=0)

l4 = Label(window, text='ISBN')
l4.grid(row=1, column=2)


def clearList():
    list1.delete(0, END)


def fillList(books):
    for book in books:
        list1.insert(END, book)


def getSelectedRow(event):
    global selectedBook
    if len(list1.curselection()) > 0:
        index = list1.curselection()[0]
        selectedBook = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selectedBook[1])
        e2.delete(0, END)
        e2.insert(END, selectedBook[2])
        e3.delete(0, END)
        e3.insert(END, selectedBook[3])
        e4.delete(0, END)
        e4.insert(END, selectedBook[4])


# ===================== Entries =====================
titleText = StringVar()
e1 = Entry(window, textvariable=titleText)
e1.grid(row=0, column=1)

authorText = StringVar()
e2 = Entry(window, textvariable=authorText)
e2.grid(row=0, column=3)

yearText = StringVar()
e3 = Entry(window, textvariable=yearText)
e3.grid(row=1, column=1)

isbnText = StringVar()
e4 = Entry(window, textvariable=isbnText)
e4.grid(row=1, column=3)

list1 = Listbox(window, width=30, height=5)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview())


def viewCommand():
    clearList()
    books = backend.view()
    fillList(books)


b1 = Button(window, text='View All', width=12, command=lambda: viewCommand())
b1.grid(row=2, column=3)


def searchCommand():
    clearList()
    books = backend.search(titleText.get(), authorText.get(), yearText.get(), isbnText.get())
    fillList(books)


b2 = Button(window, text='Search Entry', width=12, command=searchCommand)
b2.grid(row=3, column=3)


def addCommand():
    books = backend.insert(titleText.get(), authorText.get(), yearText.get(), isbnText.get())
    viewCommand()


b3 = Button(window, text='Add Entry', width=12, command=addCommand)
b3.grid(row=4, column=3)


def updateCommand():
    backend.update(selectedBook[0], titleText.get(), authorText.get(), yearText.get(), isbnText.get())
    viewCommand()


b4 = Button(window, text='Update Selected', width=12, command=updateCommand)
b4.grid(row=5, column=3)


def deleteCommand():
    backend.delete(selectedBook[0])
    viewCommand()


list1.bind("<<ListboxSelect>>", getSelectedRow)
b5 = Button(window, text='Delete Selected', width=12, command=deleteCommand)
b5.grid(row=6, column=3)

b6 = Button(window, text='Close', width=12)
b6.grid(row=7, column=3)

window.mainloop()
