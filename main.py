import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

import os
print(os.listdir("c:/Users/Tuan Tran/Documents/GitHub/CECS450-project/datasets")) # Change this path depend on where you saved your files

# read in the data
annual_co2_per_country = pd.read_csv("c:/Users/Tuan Tran/Documents/GitHub/CECS450-project/datasets/annual-co2-emissions-per-country.csv", header=0)
annual_co2_per_country.head()

# format and graph
annual_co2_per_country = pd.DataFrame(annual_co2_per_country)

# choose a few specific countries
countries = ['China', 'United States', 'India', 'German', 'United Kingdom', 'France', 'Brazil']

# create a new dataframe with only the chosen countries
countries_data = annual_co2_per_country[annual_co2_per_country['Entity'].isin(countries)]

# group the data by country
for country in countries:
    country_data = countries_data[countries_data['Entity'] == country]
    plt.plot(country_data['Year'], country_data['Annual CO₂ emissions'], label=country)

plt.title('Annual CO2 Emissions per Country')
plt.xlabel('Year')
plt.ylabel('Annual CO2 Emissions')
plt.legend()
plt.grid(True)
plt.show()