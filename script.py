# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 18:22:51 2020

@author: 12253
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df1 = pd.read_csv('top_ten_games.csv')
df2 = pd.read_csv('LoL_top_ten_countries.csv')
df3 = pd.read_csv('viewers_by_time.csv')

# Bar Graph: Featured Games

games = ["LoL", "Dota 2", "CS:GO", "DayZ", "HOS", "Isaac", "Shows", "Hearth", "WoT", "Agar.io"]


sns.set(style='darkgrid', palette='muted')
fig1, ax1 = plt.subplots(figsize=(10, 10))
plt.bar(range(len(df1['game'])), df1['COUNT(game)'])
ax1.set_xticks(range(len(df1['game'])))
ax1.set_xticklabels(games)
ax1.set_xlabel('Game Title')
ax1.set_ylabel('Viewers')
ax1.set_title('Viewers by Game Title')
plt.show()
# Pie Chart: League of Legends Viewers' Whereabouts
fig2, ax2 = plt.subplots(figsize=(10, 10))
plt.pie(df2['COUNT(country)'], autopct='%1.0f%%', explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0), startangle = 45)
ax2.set_title('Top Ten Countries Streaming League of Legends')
plt.legend(df2['country'])
plt.show()

# Line Graph: Time Series Analysis

error=0.15
y_upper = [x + x*error for x in df3['COUNT(*)']]
y_lower = [x - x*error for x in df3['COUNT(*)']]
fig3, ax3 = plt.subplots(figsize=(10,8))
plt.plot(df3["strftime('%H', time)"], df3["COUNT(*)"])
ax3.set_title('Viewers vs Time')
ax3.set_xticks(df3["strftime('%H', time)"])
ax3.set_xticklabels(df3["strftime('%H', time)"])
ax3.set_xlabel('Time')
ax3.set_ylabel('Viewers')
plt.fill_between(df3["strftime('%H', time)"], y_lower, y_upper, alpha=0.2)
plt.show()