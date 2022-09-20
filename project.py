import tkinter as tk


from tkinter import *
from tkinter import ttk
from tkinter import messagebox


window = tk.Tk()
window.title("C$50 Currency Converter")
window.minsize(width = 600, height = 400)
window.configure(background="#4285F4")

amount_label = tk.Label(master = window, text = "Enter your amount in THB")
amount_label.configure(bg = "#4285F4", fg = "#CB4335", font = "Classique 20 bold")
amount_label.pack(pady = 20)

amount = IntVar()
amount_input = tk.Entry(master = window, textvariable = amount)
amount_input.pack()

currencies = StringVar(value = "Currencies")
currencies_label = tk.Label(master = window, text = "Choose currency")
currencies_label.configure(bg = "#4285F4", fg = "#FBBC05", font = "Classique 20 bold")
currencies_label.pack(pady = 20)
currencies_box = ttk.Combobox(master = window, textvariable = currencies)
currencies_box["values"] = ("USD", "EUR", "GBP", "JPY", "CNY","KRW")
currencies_box.pack()

result_label = tk.Label(master = window, text = "You will totally get")
result_label.configure(bg = "#4285F4", fg = "#2ECC71", font = "Classique 20 bold")
result_label.pack(pady = 20)
result_input = tk.Entry(master = window)
result_input.pack()


def convert():
    money = amount.get()
    currency = currencies.get()

    if money < 0:
        amount_input.delete(0, END)
        result = messagebox.showinfo(title = "ERROR!", message = "Amount must be an integer!")
    elif currency == "USD":
        result_input.delete(0, END)
        result = ((round(money * 0.0290, 2)), "USD")
        result_input.insert(0, result)
    elif currency == "EUR":
        result_input.delete(0, END)
        result = ((round(money * 0.0300, 2)), "EUR")
        result_input.insert(0, result)
    elif currency == "GBP":
        result_input.delete(0, END)
        result = ((round(money * 0.0226, 2)), "GBP")
        result_input.insert(0, result)
    elif currency == "JPY":
        result_input.delete(0, END)
        result = ((round(money * 3.4000, 2)), "JPY")
        result_input.insert(0, result)
    elif currency == "CNY":
        result_input.delete(0, END)
        result = ((round(money * 0.1900, 2)), "CNY")
        result_input.insert(0, result)
    elif currency == "KRW":
        result_input.delete(0, END)
        result = ((round(money * 35.7143, 2)), "KRW")
        result_input.insert(0, result)
    else:
        result_input.delete(0, END)
        result = messagebox.showinfo(title = "ERROR!", message = "Currency must be chosen!")



def clear():
    amount_input.delete(0, END)
    result_input.delete(0, END)
    currencies_box.delete(0, END)
    


convert_button = Button(master = window, text = "Convert", command = convert)
convert_button.configure(font = "Classique 12 bold")
convert_button.pack(pady = 10)

clear_button = Button(master = window, text = "Clear", command = clear)
clear_button.configure(font = "Classique 12 bold")
clear_button.pack()

window.mainloop()