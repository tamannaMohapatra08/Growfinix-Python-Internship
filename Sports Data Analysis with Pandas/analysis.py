# ==============================
# IPL DATA ANALYSIS PROJECT
# Tech Stack: Pandas, Matplotlib
# ==============================

import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1. LOAD DATA
# ==============================
df = pd.read_csv("matches.csv")

print("Dataset Shape:", df.shape)
print(df.head())

# ==============================
# 2. DATA CLEANING
# ==============================
print("\nMissing Values:\n", df.isnull().sum())

df = df.dropna()

# ==============================
# 3. TEAM WIN RATE ANALYSIS
# ==============================

total_matches = df['team1'].value_counts() + df['team2'].value_counts()
wins = df['winner'].value_counts()

win_rate = (wins / total_matches) * 100

print("\nWin Rate of Teams:\n", win_rate.sort_values(ascending=False))

# ==============================
# 4. KKR ANALYSIS
# ==============================

kkr_matches = df[(df['team1'] == 'Kolkata Knight Riders') |
                 (df['team2'] == 'Kolkata Knight Riders')]

kkr_wins = df[df['winner'] == 'Kolkata Knight Riders']

kkr_win_rate = (len(kkr_wins) / len(kkr_matches)) * 100

print("\nKKR Matches:", len(kkr_matches))
print("KKR Wins:", len(kkr_wins))
print("KKR Win Rate:", kkr_win_rate)

# ==============================
# 5. TOSS ANALYSIS
# ==============================

toss_decision = df['toss_decision'].value_counts()
print("\nToss Decision Count:\n", toss_decision)

toss_win = df[df['toss_winner'] == df['winner']]
print("\nMatches where toss winner also won:", len(toss_win))

# ==============================
# 6. VISUALIZATION
# ==============================

# Top 10 teams by wins
wins.head(10).plot(kind='bar')
plt.title("Top Winning IPL Teams")
plt.xlabel("Teams")
plt.ylabel("Wins")
plt.xticks(rotation=45)
plt.show()

# Toss decision pie chart
toss_decision.plot(kind='pie', autopct='%1.1f%%')
plt.title("Toss Decision Distribution")
plt.ylabel("")
plt.show()

# KKR performance bar chart
plt.bar(["Matches", "Wins"], [len(kkr_matches), len(kkr_wins)])
plt.title("KKR Performance")
plt.show()