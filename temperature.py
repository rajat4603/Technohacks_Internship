import tkinter as tk

class TemperatureConverter:
    def __init__(self, master):
        self.master = master
        master.title("Temperature Converter")

        self.init_ui()

    def init_ui(self):
        # Create entry widgets
        self.fahrenheit_entry = tk.Entry(self.master, text="")
        self.fahrenheit_entry.grid(row=0, column=0, padx=5, pady=5)

        self.celsius_entry = tk.Entry(self.master, text="")
        self.celsius_entry.grid(row=1, column=0, padx=5, pady=5)

        # Create labels
        tk.Label(self.master, text="Fahrenheit:").grid(row=0, column=1, padx=5, pady=5)
        tk.Label(self.master, text="Celsius:").grid(row=1, column=1, padx=5, pady=5)

        # Create buttons
        tk.Button(self.master, text="Convert", command=self.convert).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(self.master, text="Clear", command=self.clear).grid(row=2, column=1, padx=5, pady=5)

    def convert(self):
        try:
            fahrenheit = float(self.fahrenheit_entry.get())
            celsius = (fahrenheit - 32) * 5 / 9

            self.celsius_entry.delete(0, "end")
            self.celsius_entry.insert(0, celsius)
        except ValueError:
            # Handle the case where the input is not a valid float
            pass

    def clear(self):
        self.fahrenheit_entry.delete(0, "end")
        self.celsius_entry.delete(0, "end")

def main():
    root = tk.Tk()
    converter = TemperatureConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()

