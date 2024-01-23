
import tkinter as tk
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self, master):
        self.master = master
        master.title("Currency Converter")

        self.cr = CurrencyRates()

        self.init_ui()

    def init_ui(self):
        # Create entry widgets
        self.amount_entry = tk.Entry(self.master, text="")
        self.amount_entry.grid(row=0, column=0, padx=5, pady=5)

        self.from_currency_entry = tk.Entry(self.master, text="")
        self.from_currency_entry.grid(row=1, column=0, padx=5, pady=5)

        self.to_currency_entry = tk.Entry(self.master, text="")
        self.to_currency_entry.grid(row=2, column=0, padx=5, pady=5)

        # Create labels
        tk.Label(self.master, text="Amount:").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.master, text="From:").grid(row=1, column=1, padx=5, pady=5)
        tk.Label(self.master, text="To:").grid(row=2, column=1, padx=5, pady=5)

        # Create buttons
        tk.Button(self.master, text="Convert", command=self.convert).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(self.master, text="Clear", command=self.clear).grid(row=3, column=1, padx=5, pady=5)

        # Create dropdown menus
        self.from_currencies = sorted(self.cr.get_rates('').keys())
        self.to_currencies = sorted(self.cr.get_rates('').keys())

        self.from_currency_var = tk.StringVar(self.master)
        self.from_currency_var.set(self.from_currencies[0])
        tk.OptionMenu(self.master, self.from_currency_var, *self.from_currencies).grid(row=1, column=2, padx=5, pady=5)

        self.to_currency_var = tk.StringVar(self.master)
        self.to_currency_var.set(self.to_currencies[0])
        tk.OptionMenu(self.master, self.to_currency_var, *self.to_currencies).grid(row=2, column=2, padx=5, pady=5)

    def convert(self):
        amount = float(self.amount_entry.get())
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()

        rate = self.cr.get_rate(from_currency, to_currency)
        result = amount * rate

        self.to_currency_entry.delete(0, "end")
        self.to_currency_entry.insert(0, result)

    def clear(self):
        self.amount_entry.delete(0, "end")
        self.from_currency_entry.delete(0, "end")
        self.to_currency_entry.delete(0, "end")

def main():
    root = tk.Tk()
    converter = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
