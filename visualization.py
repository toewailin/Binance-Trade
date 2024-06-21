# pip install -U  matplotlib

import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV file into a DataFrame
file_path = 'ADAUSDT_futures_klines.csv'
xrp_data = pd.read_csv(file_path)
# Convert the Open Time to datetime format for better plotting
xrp_data['Open Time'] = pd.to_datetime(xrp_data['Open Time'])

# Set Open Time as index
xrp_data.set_index('Open Time', inplace=True)

# Calculate Simple Moving Average (SMA) for 4 periods (equivalent to 1 hour of data)
xrp_data['SMA_4'] = xrp_data['Close'].rolling(window=4).mean()

# Plotting the Close prices and the SMA
plt.figure(figsize=(14, 7))
plt.plot(xrp_data['Close'], label='Close Price', color='blue')
plt.plot(xrp_data['SMA_4'], label='1-Hour SMA', color='red')
plt.title('XRPUSDT Close Price and 1-Hour Simple Moving Average')
plt.xlabel('Time')
plt.ylabel('Price (USDT)')
plt.legend()
plt.grid(True)
plt.show()
