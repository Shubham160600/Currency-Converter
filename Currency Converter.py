import requests

amount = float(input("Amount in USD: "))
to_currency = input("Convert to (e.g., EUR, INR): ").upper()
response = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()

if to_currency in response['rates']:
    converted = amount * response['rates'][to_currency]
    print(f"{amount} USD = {converted:.2f} {to_currency}")
else:
    print("Currency not found.")
