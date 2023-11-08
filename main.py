import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

import os
print(os.listdir("c:/Users/Tuan Tran/Documents/GitHub/CECS450-project/datasets")) # Change this path depend on where you saved your files

# read in the data
annual_co2_per_country = pd.read_csv("c:/Users/Tuan Tran/Documents/GitHub/CECS450-project/datasets/annual-co2-emissions-per-country.csv", header=0)
annual_co2_per_country.head()