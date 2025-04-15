import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://open.er-api.com/v6/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()

    if data["result"] == "success":
        rate = data["rates"].get(to_currency)
        if rate:
            return round(amount * rate, 2)
        else:
            raise ValueError(f"Exchange rate for {to_currency} not found.")
    else:
        raise Exception("Currency conversion failed.")


if __name__ == "__main__":
    print(convert_currency(1000, "USD", "AED"))