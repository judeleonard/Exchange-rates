import requests
import csv
import os

## Define Variables ####

# Xe Currency Data API endpoint
api_url = "https://xecdapi.xe.com/v1/convert_from.json/"

# Set your Xe Currency API key
API_KEY = os.environ["api_key"]  



# Define the source currency and list of target currencies
currency_from = "USD"
target_currencies = ["NGN", "KES", "EGP", "GHS", "UGX", "MAD", "XOF"]

# Create a list to store the exchange rate results
exchange_rates = []
currency_to_USD_rate = 1

# path to load data
csv_file = "./data/exchange_rates.csv"


def sendGetRequest():
    """
    Sends get request to XE currency api based on the latest exchange rates and exports result
    to a csv file.

    Args:
        None
    """

    # Define request headers with the API_KEY
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        for currency_to in target_currencies:
            # Construct the request URL following the documentation
            url = f"{api_url}?from={currency_from}&to={currency_to}&amount={currency_to_USD_rate}"

            # Send a GET request to the Xe Currency API
            response = requests.get(url, headers=headers)

            # Check if the request was successful
            if response.status_code == 200:
                data = response.json()
                USD_to_currency_rate = data['to'][0]['mid']

                # Grab the timestamp from the response object
                timestamp = data["timestamp"]

                exchange_rates.append((timestamp, currency_from, USD_to_currency_rate, currency_to_USD_rate, currency_to))
            else:
                print(f"Failed to fetch data for {currency_to}. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")

    # Save the exchange rate results to a CSV file
    with open(csv_file, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["timestamp", "currency_from", "USD_to_currency_rate", "currency_to_USD_rate", "currency_to"])
        csvwriter.writerows(exchange_rates)

    print(f"Exchange rates saved to {csv_file}")





if __name__ == "__main__":
    sendGetRequest()
