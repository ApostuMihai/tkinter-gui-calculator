from tkinter import *

root = Tk()
root.title("Calculator")
e = Entry(root, width=35, borderwidth=3)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)



def button_click(number):
  current_number = e.get()
  e.delete(0, END)
  e.insert(0, str(current_number) + str(number))

def button_clear():
   e.delete(0, END)


def button_add():
  first_number = e.get()
  global f_num
  global operation
  operation = "addition"
  f_num = int(first_number)
  e.delete(0, END)

def button_substract():
  global operation
  operation = "substraction"
  global f_num
  first_number = e.get()
  f_num = int(first_number)
  e.delete(0, END)
  

def button_division():
  global operation
  operation = "division"
  global f_num
  first_number = e.get()
  f_num = int(first_number)
  e.delete(0, END)

def button_multiply():
  global operation
  operation = "multiplication"
  global f_num
  first_number = e.get()
  f_num = int(first_number)
  e.delete(0, END)


def button_equals():
  second_number = e.get()
  e.delete(0, END)
  if operation == "addition":
    e.insert(0, f_num + int(second_number))
  elif operation == "substraction":
    e.insert(0, f_num - int(second_number))
  elif operation == "division":
    e.insert(0, f_num / int(second_number))
  elif operation == "multiplication":
    e.insert(0, f_num * int(second_number))





#Creating the number buttons
button_1 = Button(root, text = "1", padx=30, pady=15, command=lambda: button_click(1))
button_2 = Button(root, text = "2", padx=30, pady=15, command=lambda: button_click(2))
button_3 = Button(root, text = "3", padx=30, pady=15, command=lambda: button_click(3))
button_4 = Button(root, text = "4", padx=30, pady=15, command=lambda: button_click(4))
button_5 = Button(root, text = "5", padx=30, pady=15, command=lambda: button_click(5))
button_6 = Button(root, text = "6", padx=30, pady=15, command=lambda: button_click(6))
button_7 = Button(root, text = "7", padx=30, pady=15, command=lambda: button_click(7))
button_8 = Button(root, text = "8", padx=30, pady=15, command=lambda: button_click(8))
button_9 = Button(root, text = "9", padx=30, pady=15, command=lambda: button_click(9))
button_0 = Button(root, text = "0", padx=30, pady=15, command=lambda: button_click(0))

#Creating the symbols and clear buttons
button_clear = Button(root, text = "CLEAR", padx=30, pady=15, command= button_clear)

button_equals = Button(root, text = "=", padx=60, pady=15, command = button_equals)

button_add = Button(root, text = "+", padx=35, pady=15, command = button_add)

button_substract = Button(root, text="-", padx=35, pady=15, command = button_substract)

button_division = Button(root, text="/", padx=35, pady=15, command = button_division )

button_multiply = Button(root, text="*", padx=35, pady=15, command = button_multiply)

#Placing the buttons on the grid
button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)
button_add.grid(row = 1, column = 3)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)
button_substract.grid(row=2, column=3)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)
button_division.grid(row=3, column=3)


button_0.grid(row = 4, column = 0)
button_equals.grid(row=4, column= 1, columnspan=2)
button_multiply.grid(row=4, column=3)

button_clear.grid(row = 5, column = 1, columnspan=2)



# myBtn = Button(root, text = "Enter your name", command=myClick)

root.mainloop()


