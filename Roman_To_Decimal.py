import tkinter as tk
tallies = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


class RomanToDecimalConverter:
    def __init__(self, window):
        self.window = window
        self.window.title("Fasina Roman Numeral to Decimal Converter")

        self.label_roman = tk.Label(self.window, text="Enter Roman Numeral:")
        self.label_roman.pack(pady=10)
        self.entry_roman = tk.Entry(self.window)
        self.entry_roman.pack(pady=5)

        self.btn_convert = tk.Button(self.window, text="Convert Roman To Decimal", command=self.convert_roman)
        self.btn_convert.pack(pady=10)

        self.label_result = tk.Label(self.window, text="Decimal Value: ")
        self.label_result.pack(pady=10)

    def roman_to_decimal(self, roman):
        sums = 0
        for i in range(len(roman) - 1):
            left = roman[i]
            right = roman[i + 1]
            if tallies[left] < tallies[right]:
                sums -= tallies[left]
            else:
                sums += tallies[left]
        sums += tallies[roman[-1]]
        return sums

    def convert_roman(self):
        roman_number = self.entry_roman.get().upper()
        try:
            if not all(c in tallies for c in roman_number):
                raise ValueError("Invalid Roman numeral.")

            decimal_value = self.roman_to_decimal(roman_number)
            self.label_result.config(text=f"Decimal Value: {decimal_value}")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))


def main():
    window = tk.Tk()
    RomanToDecimalConverter(window)
    window.mainloop()


main()
