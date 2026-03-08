import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Title": ["Stranger Things", "Money Heist", "Extraction", "The Witcher", "Red Notice", "Narcos"],
    "Type": ["TV Show", "TV Show", "Movie", "TV Show", "Movie", "TV Show"],
    "Rating": ["TV-14", "TV-MA", "R", "TV-MA", "PG-13", "TV-MA"],
    "Year": [2016, 2017, 2020, 2019, 2021, 2015]
}

df = pd.DataFrame(data)

print("Dataset")
print(df)

print("\nDataset Info")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

type_count = df.groupby("Type")["Title"].count()
print("\nContent Count by Type")
print(type_count)

rating_count = df.groupby("Rating")["Title"].count()
print("\nContent Count by Rating")
print(rating_count)

type_count.plot(kind="bar")

plt.title("Netflix Content Distribution")
plt.xlabel("Type")
plt.ylabel("Count")

plt.show()
