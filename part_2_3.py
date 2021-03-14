import pandas as pd
import matplotlib.pyplot as plt


CSV_FILE = "./data/report_2_3.csv"

df = pd.read_csv(CSV_FILE)
df.set_index('time', inplace=True)
title = 'Infection Trend in Time Series per Age Group'
df.groupby('age')['daily_infections'].plot(title=title, legend=True)
plt.savefig('./part_2_3.png')
plt.show()
