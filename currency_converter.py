import requests
# NOTE: Replace "YOUR_API_KEY" with your actual ExchangeRate API key

API_KEY = "YOUR_API_KEY"  # Replace this with your real API key
# Do NOT hardcode USD here. Let the user choose it.
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/" 


def convert_currency(amount, from_currency, to_currency):
    url = BASE_URL + from_currency.upper()
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch exchange rates.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        return

    data = response.json()
    try:
        rate = data['conversion_rates'][to_currency.upper()]
        converted = amount * rate
        print(f"\n💱 {amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
        print(f"(Exchange rate: 1 {from_currency.upper()} = {rate} {to_currency.upper()})")
    except KeyError:
        print("Invalid target currency!")

try:
    amount = float(input("Enter amount: "))
    from_currency = input("From currency (e.g., USD): ")
    to_currency = input("To currency (e.g., INR): ")

    convert_currency(amount, from_currency, to_currency)

except ValueError:
    print("Invalid amount!")
