import pandas as pd
import matplotlib.pyplot as plt

# File paths
file_1_path = "/Users/kiki/Desktop/3/CLMMAXT_HKA_.csv"
file_2_path = "/Users/kiki/Desktop/3/CLMMINT_HKA_.csv"

# Read files and treat missing values as '***'
data_1 = pd.read_csv(file_1_path, encoding='utf-8', delimiter=',', skiprows=2, na_values='***')
data_2 = pd.read_csv(file_2_path, encoding='utf-8', delimiter=',', skiprows=2, na_values='***')

# Clean data, remove rows with missing values in the date columns
data_1_clean = data_1.dropna(subset=['年/Year', '月/Month', '日/Day'])
data_2_clean = data_2.dropna(subset=['年/Year', '月/Month', '日/Day'])

# Convert date columns to integer type
data_1_clean['年/Year'] = data_1_clean['年/Year'].astype(int)
data_1_clean['月/Month'] = data_1_clean['月/Month'].astype(int)
data_1_clean['日/Day'] = data_1_clean['日/Day'].astype(int)

data_2_clean['年/Year'] = data_2_clean['年/Year'].astype(int)
data_2_clean['月/Month'] = data_2_clean['月/Month'].astype(int)
data_2_clean['日/Day'] = data_2_clean['日/Day'].astype(int)

# Manually create date column
data_1_clean['Date'] = pd.to_datetime(data_1_clean['年/Year'].astype(str) + '-' + 
                                      data_1_clean['月/Month'].astype(str) + '-' + 
                                      data_1_clean['日/Day'].astype(str), errors='coerce')

data_2_clean['Date'] = pd.to_datetime(data_2_clean['年/Year'].astype(str) + '-' + 
                                      data_2_clean['月/Month'].astype(str) + '-' + 
                                      data_2_clean['日/Day'].astype(str), errors='coerce')

# Set plot area size
plt.figure(figsize=(10, 6))

# Plot the line chart for minimum temperatures
plt.plot(data_1_clean['Date'], data_1_clean['數值/Value'], label='Minimum Temperature (°C)', color='blue')

# Plot the line chart for maximum temperatures
plt.plot(data_2_clean['Date'], data_2_clean['數值/Value'], label='Maximum Temperature (°C)', color='red')

# Add title and labels
plt.title('Daily Maximum and Minimum Temperatures at Hong Kong International Airport')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')

# Show legend
plt.legend()

# Display the chart
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()