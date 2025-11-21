import pandas as pd
import matplotlib.pyplot as plt

# Netflix color palette
netflix_red = "#E50914"
netflix_dark = "#221f1f"
netflix_gray = "#b81d24"
netflix_white = "#f5f5f1"

plt.style.use("dark_background")

# Load data
path = "F:\\Data sciance\\Project\\netflix_titles.csv"
data = pd.read_csv(path)

# Drop rows with missing important values
df = data.dropna(subset=['type','release_year','rating','country','duration'])

# Prepare Data
type_counts = df['type'].value_counts()
rating_counts = df['rating'].value_counts()
movie_df = df[df['type']=='Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace(' min','').astype(int)
release_counts = df['release_year'].value_counts().sort_index()
country_counts = df['country'].value_counts().head(10)
content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)

# Create dashboard
fig, axes = plt.subplots(3, 2, figsize=(15, 14))
axes = axes.flatten()

# 1. Movies vs TV Shows
axes[0].bar(type_counts.index, type_counts.values, color=[netflix_red, netflix_gray])
axes[0].set_title("Movies vs TV Shows", fontsize=14, fontweight="bold", color=netflix_white)
axes[0].set_xlabel("Type")
axes[0].set_ylabel("Count")
for i, v in enumerate(type_counts.values):
    axes[0].text(i, v+50, str(v), ha='center', fontsize=10, color=netflix_white)

# 2. Rating Distribution
axes[1].pie(rating_counts.values, labels=rating_counts.index,
            autopct='%1.1f%%', startangle=90, colors=[netflix_red, netflix_gray, netflix_white, "orange", "purple"])
axes[1].set_title("Content Rating Distribution", fontsize=14, fontweight="bold", color=netflix_white)

# 3. Movie Duration Histogram
axes[2].hist(movie_df['duration_int'], bins=30, color=netflix_red, edgecolor=netflix_white)
axes[2].set_title("Distribution of Movie Durations", fontsize=14, fontweight="bold", color=netflix_white)
axes[2].set_xlabel("Duration (minutes)")
axes[2].set_ylabel("Number of Movies")

# 4. Release Year Scatter
axes[3].scatter(release_counts.index, release_counts.values, color=netflix_red)
axes[3].set_title("Content by Release Year", fontsize=14, fontweight="bold", color=netflix_white)
axes[3].set_xlabel("Release Year")
axes[3].set_ylabel("Number of Titles")

# 5. Top 10 Countries
axes[4].barh(country_counts.index, country_counts.values, color=netflix_gray)
axes[4].set_title("Top 10 Countries", fontsize=14, fontweight="bold", color=netflix_white)
axes[4].set_xlabel("Number of Titles")
axes[4].invert_yaxis()  # Highest on top
for i, v in enumerate(country_counts.values):
    axes[4].text(v+10, i, str(v), va='center', fontsize=10, color=netflix_white)

# 6. Movies vs TV Shows Over the Years
axes[5].plot(content_by_year.index, content_by_year['Movie'], label="Movies", color=netflix_red, linewidth=2)
axes[5].plot(content_by_year.index, content_by_year['TV Show'], label="TV Shows", color=netflix_gray, linewidth=2)
axes[5].set_title("Movies vs TV Shows Over the Years", fontsize=14, fontweight="bold", color=netflix_white)
axes[5].set_xlabel("Year")
axes[5].set_ylabel("Count")
axes[5].legend(facecolor=netflix_dark, edgecolor=netflix_white, fontsize=10)

# Adjust layout
fig.suptitle("📺 Netflix Content Analysis Dashboard", fontsize=18, fontweight="bold", color=netflix_red)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig("netflix_dashboard.png", facecolor=netflix_dark, dpi=300)
plt.show()
