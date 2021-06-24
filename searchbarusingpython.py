

# Being able to easily launch a browser can be a useful operation in many scripts. 
# For example, maybe a script performs some kind of deployment to a server and one 
# would like to have it quickly launch a browser so one can verify that it’s working. 
# Or maybe a program writes data out in the form of HTML pages and just like to fire 
# up a browser to see the result. Either way, the webbrowser module is a simple solution.

from tkinter import *
import webbrowser

win = Tk()
win.title("Search Bar")

def search():
    url = entry.get()
    webbrowser.open(url)

lblURL = Label(win, text = 'Enter a valid URL: ', font = ('arial', 10, 'bold'))
lblURL.grid(row=0, column=0)

entry = Entry(win, width=30)
entry.grid(row=0, column=1)

btnsearch = Button(win, text = 'GO', command=search)
btnsearch.grid(row=1, column=0, columnspan=2, pady=10)

btn_close = Button(win, text="Close", command=win.destroy)
btn_close.grid(row=1, column=1, columnspan=2, pady=10)

win.mainloop()