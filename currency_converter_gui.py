import requests
import tkinter as tk
from tkinter import messagebox

# NOTE: Replace with your actual API key from exchangerate-api.com
API_KEY = "YOUR_API_KEY"  
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_curr = entry_from.get().upper()
        to_curr = entry_to.get().upper()

        url = BASE_URL + from_curr
        response = requests.get(url)

        if response.status_code != 200:
            messagebox.showerror("Error", "Failed to fetch exchange rates.")
            return

        data = response.json()
        rate = data['conversion_rates'].get(to_curr)

        if rate is None:
            messagebox.showerror("Error", f"Invalid target currency: {to_curr}")
            return

        converted = amount * rate
        result_label.config(
            text=f"{amount} {from_curr} = {converted:.2f} {to_curr}\n(1 {from_curr} = {rate} {to_curr})"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# Create GUI Window
window = tk.Tk()
window.title("Currency Converter")
window.geometry("400x300")
window.resizable(False, False)

# UI Elements
tk.Label(window, text="Amount:").pack(pady=5)
entry_amount = tk.Entry(window)
entry_amount.pack()

tk.Label(window, text="From Currency (e.g., USD):").pack(pady=5)
entry_from = tk.Entry(window)
entry_from.pack()

tk.Label(window, text="To Currency (e.g., INR):").pack(pady=5)
entry_to = tk.Entry(window)
entry_to.pack()

tk.Button(window, text="Convert", command=convert_currency).pack(pady=15)

result_label = tk.Label(window, text="", font=("Arial", 12), wraplength=350)
result_label.pack()

# Start the GUI app
window.mainloop()
