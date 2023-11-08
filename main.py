import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

import os

print(os.listdir(
    "c:/Users/Tuan Tran/Documents/GitHub/CECS450-project/datasets"))  # Change this path depend on where you saved your files

# read in the data
annual_co2_per_country = pd.read_csv(
    "c:/Users/Tuan Tran/Documents/GitHub/CECS450-project/datasets/annual-co2-emissions-per-country.csv", header=0)
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

# read in the data
global_co2_fossil_land = pd.read_csv(
    "c:/Users/Tuan Tran/Documents/GitHub/CECS450-project/datasets/global-co2-fossil-plus-land-use.csv", header=0)
global_co2_fossil_land.head()
# Create a DataFrame from the data
global_co2_fossil_land = pd.DataFrame(global_co2_fossil_land)
world_data = global_co2_fossil_land[global_co2_fossil_land['Entity'] == 'World']

# Extract the Year and Annual CO₂ emissions from land-use change values
years = world_data['Year']
emissions_fossil_fuel = world_data['Annual CO₂ emissions including land-use change'] - world_data[
    'Annual CO₂ emissions from land-use change']
emissions_land_use_change = world_data['Annual CO₂ emissions from land-use change']
emissions_total = world_data['Annual CO₂ emissions including land-use change']

# Create the line graph for global CO₂ emissions
plt.plot(years, emissions_fossil_fuel, marker='o', linestyle='-', color='b', label='Fossil Fuel')
plt.plot(years, emissions_land_use_change, marker='o', linestyle='-', color='g', label='Land Use Change')
plt.plot(years, emissions_total, marker='o', linestyle='-', color='r', label='Total (Fossil Fuel + Land Use Change)')
plt.title('Global CO₂ Emissions')
plt.xlabel('Year')
plt.ylabel('Annual CO₂ Emissions')
plt.grid(True)
plt.legend()

plt.show()
