#pip install -U requests pandas

import requests
import pandas as pd

def get_binance_futures_klines(symbol='BTCUSDT', interval='5m', limit=100):
    url = f"https://fapi.binance.com/fapi/v1/klines"
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': limit
    }
    response = requests.get(url, params=params)
    data = response.json()

    # Define the column names for the data
    columns = [
        'Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 
        'Quote Asset Volume', 'Number of Trades', 'Taker Buy Base Asset Volume', 
        'Taker Buy Quote Asset Volume', 'Ignore'
    ]

    # Create a DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Convert the timestamp to a readable format
    df['Open Time'] = pd.to_datetime(df['Open Time'], unit='ms')
    df['Close Time'] = pd.to_datetime(df['Close Time'], unit='ms')

    return df

# ADAUSDT, XRPUSDT, MEMEUSDT, DOGEUSDT, 1000PEPEUSDT
symbol='ADAUSDT' 
#15m, 1h, 4h, 1d
interval='15m' 
#25, 50, 100
limit=50

# Fetch the data
klines_data = get_binance_futures_klines(symbol, interval, limit)

# Save the data to a CSV file
csv_file_path = f'{symbol}_futures_klines.csv'
klines_data.to_csv(csv_file_path, index=False)

print(f"Klines data has been saved to {csv_file_path}")