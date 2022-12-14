Python 3.11.1 (v3.11.1:a7a450f84a, Dec  6 2022, 15:24:06) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
>>> 
>>> root =Tk()
>>> 
>>> # Creating a Label Widget
>>> myLabel1 = Label(root, text="The Video Game Shop")
>>> myLabel2 = Label(root, text="Main Page")
>>> myLabel3 = Label(root, text="Checkout Page")
>>> # Shoving it onto the screen
>>> 
>>> myLabel1.grid(row=0, column=0)
>>> myLabel2.grid(row=1, column=0)
>>> myLabel3.grid(row=2, column=0)
>>> 
>>> top = Toplevel()
>>> top.title('Checkout Page')
''
