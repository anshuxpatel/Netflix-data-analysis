import pandas as pd

data = pd.read_csv("netflix_data.csv")

print(data)
print("\nMovies and TV Shows Count:")

type_count = data["Type"].value_counts()

print(type_count)
print("\nGenre-wise Content Count:")

genre_count = data["Genre"].value_counts()

print(genre_count)
import matplotlib.pyplot as plt

genre_count.plot(kind="bar")

plt.title("Netflix Content by Genre")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")

plt.show()
type_count.plot(kind="pie", autopct="%1.1f%%")

plt.title("Movies vs TV Shows")
plt.ylabel("")

plt.show()
print("\nMost Common Genre:")

most_common_genre = genre_count.idxmax()

print(most_common_genre)
print("Total Titles:", genre_count.max())

print("\nContent Released by Year:")

year_count = data["Release_Year"].value_counts().sort_index()

print(year_count)
year_count.plot(kind="bar")

plt.title("Netflix Content by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.show()
print("\nHighest Content Release Year:")

highest_year = year_count.idxmax()

print("Year:", highest_year)
print("Total Titles:", year_count.max())
print("\n--- NETFLIX FINAL REPORT ---")

print("Total Titles:", len(data))
print("Total Movies:", type_count.get("Movie", 0))
print("Total TV Shows:", type_count.get("TV Show", 0))

print("Total Genres:", data["Genre"].nunique())
print("Most Common Genre:", genre_count.idxmax())
print("Highest Release Year:", year_count.idxmax())
data.to_csv("netflix_analysis_result.csv", index=False)

print("Netflix analysis data saved successfully!")