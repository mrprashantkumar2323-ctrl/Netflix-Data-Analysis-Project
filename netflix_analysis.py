import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set_theme(style="whitegrid")

DATA_URL = "https://raw.githubusercontent.com/japnitahuja/netflix-data-analysis/main/netflix_titles.csv"
LOCAL_PATH = Path("data/netflix_titles.csv")

def load_data():
    if LOCAL_PATH.exists():
        return pd.read_csv(LOCAL_PATH)
    return pd.read_csv(DATA_URL)

def main():
    df = load_data()

    print("\n--- Shape ---")
    print(df.shape)

    print("\n--- Missing values ---")
    print(df.isna().sum().sort_values(ascending=False))

    # Cleaning
    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
    df["year_added"] = df["date_added"].dt.year
    df["month_added"] = df["date_added"].dt.month_name()

    for col in ["director", "cast", "country", "rating"]:
        df[col] = df[col].fillna("Unknown")

    df["duration_value"] = pd.to_numeric(
        df["duration"].astype(str).str.extract(r"(\d+)")[0],
        errors="coerce"
    )

    df["duration_unit"] = np.where(
        df["type"].eq("Movie"), "minutes",
        np.where(df["type"].eq("TV Show"), "seasons", "unknown")
    )

    # Basic KPI output
    print("\n--- KPIs ---")
    print("Total titles:", len(df))
    print("Movies:", (df["type"] == "Movie").sum())
    print("TV Shows:", (df["type"] == "TV Show").sum())
    print("Unique release years:", df["release_year"].nunique())

    # 1. Movie vs TV Show
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="type")
    plt.title("Netflix Content by Type")
    plt.xlabel("Content Type")
    plt.ylabel("Number of Titles")
    plt.tight_layout()
    plt.show()

    # 2. Release year trend
    yearly = df.groupby("release_year").size().reset_index(name="titles")
    yearly = yearly[yearly["release_year"] >= 2000]

    plt.figure(figsize=(12, 5))
    sns.lineplot(data=yearly, x="release_year", y="titles")
    plt.title("Netflix Titles by Release Year")
    plt.xlabel("Release Year")
    plt.ylabel("Number of Titles")
    plt.tight_layout()
    plt.show()

    # 3. Top ratings
    top_ratings = df["rating"].value_counts().head(10).reset_index()
    top_ratings.columns = ["rating", "titles"]

    plt.figure(figsize=(10, 5))
    sns.barplot(data=top_ratings, y="rating", x="titles")
    plt.title("Top Netflix Content Ratings")
    plt.xlabel("Number of Titles")
    plt.ylabel("Rating")
    plt.tight_layout()
    plt.show()

    # 4. Top countries (split multi-country rows)
    countries = (
        df.assign(country=df["country"].str.split(", "))
          .explode("country")
    )
    top_countries = countries["country"].value_counts().head(10).reset_index()
    top_countries.columns = ["country", "titles"]

    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_countries, y="country", x="titles")
    plt.title("Top Countries by Number of Netflix Titles")
    plt.xlabel("Number of Titles")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.show()

    # 5. Top genres
    genres = (
        df.assign(genre=df["listed_in"].str.split(", "))
          .explode("genre")
    )
    top_genres = genres["genre"].value_counts().head(10).reset_index()
    top_genres.columns = ["genre", "titles"]

    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_genres, y="genre", x="titles")
    plt.title("Top Netflix Genres")
    plt.xlabel("Number of Titles")
    plt.ylabel("Genre")
    plt.tight_layout()
    plt.show()

    # 6. Movie duration distribution
    movies = df[df["type"].eq("Movie") & df["duration_value"].notna()].copy()

    plt.figure(figsize=(10, 5))
    sns.histplot(movies["duration_value"], bins=30, kde=True)
    plt.title("Movie Duration Distribution")
    plt.xlabel("Duration (minutes)")
    plt.ylabel("Number of Movies")
    plt.tight_layout()
    plt.show()

    # 7. Content added over time
    added = df.dropna(subset=["year_added"]).groupby(["year_added", "type"]).size().reset_index(name="titles")

    plt.figure(figsize=(12, 5))
    sns.lineplot(data=added, x="year_added", y="titles", hue="type", marker="o")
    plt.title("Netflix Titles Added by Year")
    plt.xlabel("Year Added")
    plt.ylabel("Number of Titles")
    plt.tight_layout()
    plt.show()

    # Export cleaned data
    Path("output").mkdir(exist_ok=True)
    df.to_csv("output/netflix_titles_cleaned.csv", index=False)
    print("\nCleaned dataset saved to output/netflix_titles_cleaned.csv")

if __name__ == "__main__":
    main()
