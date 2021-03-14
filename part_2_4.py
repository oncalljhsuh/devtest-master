import pandas as pd
import matplotlib.pyplot as plt


CSV_FILE = "./data/report_2_3.csv"

df = pd.read_csv(CSV_FILE)
df.sort_values('time', inplace=True)
df_over20 = df[df['age'] > 20]
df_over20.set_index('time', inplace=True)
title = 'Acuumulated infectious people aged group over 20'
df = df_over20['daily_infections'].cumsum(axis=0).to_frame()
df.plot(title=title, legend=False)
plt.savefig('./part_2_4.png')
plt.show()
