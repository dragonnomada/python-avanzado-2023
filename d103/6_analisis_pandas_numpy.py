import pandas as pd
import numpy as np

d1 = pd.read_csv("../datasets/spotify_top_200.csv", sep=";")

d2 = d1[ ["Rank", "Energy", "Danceability", "Loudness", "Speechiness", "Acousticness", "Instrumentalness", "Valence"] ]

print(d2)

d2 = d2[ (d2["Energy"] > 0.1) & (d2["Danceability"] > 0.1) ]

d3 = d2.groupby("Rank").mean()

print(d3)

import matplotlib.pyplot as plt
 
# width of the bars
barWidth = 0.3
 
# Choose the height of the blue bars
bars1 = d3["Energy"][:10]
 
# Choose the height of the cyan bars
bars2 = d3["Danceability"][:10]
 
# # Choose the height of the error bars (bars1)
# yer1 = [0.5, 0.4, 0.5]
 
# # Choose the height of the error bars (bars2)
# yer2 = [1, 0.7, 1]
 
# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]
 
# Create blue bars
plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='poacee')
 
# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', capsize=7, label='sorgho')
 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))], d3.index[:10])
plt.ylabel('height')
plt.legend()
 
# Show graphic
plt.show()