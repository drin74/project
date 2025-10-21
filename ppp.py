import tkinter as tk
import requests

window = tk.Tk()
window.title("Currency Converter")

label1 = tk.Label(window, text="Amount:")
label1.pack()

entry = tk.Entry(window)
entry.pack()

label2 = tk.Label(window, text="Base Currency:")
label2.pack()

base_currency_var = tk.StringVar(window)
base_currency_var.set("USD")  # Default base currency

base_currency_dropdown = tk.OptionMenu(window, base_currency_var, "USD", "EUR", "GBP", "INR")
base_currency_dropdown.pack()

label3 = tk.Label(window, text="Target Currency:")
label3.pack()

target_currency_var = tk.StringVar(window)
target_currency_var.set("EUR")  # Default target currency

target_currency_dropdown = tk.OptionMenu(window, target_currency_var, "USD", "EUR", "GBP", "INR")
target_currency_dropdown.pack()

label4 = tk.Label(window, text="Converted Amount:")
label4.pack()

result_label = tk.Label(window, text="")
result_label.pack()

button = tk.Button(window, text="Convert")
button.pack()

window.mainloop()