import pandas as pd
import matplotlib.pyplot as plt

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

# Create a big figure with subplots
fig, axes = plt.subplots(3, 2, figsize=(14, 14))  # 3 rows, 2 columns
axes = axes.flatten()  # flatten 2D array into 1D for easy indexing

# 1. Movies vs TV Shows
axes[0].bar(type_counts.index, type_counts.values, color=['skyblue','orange'])
axes[0].set_title('Movies vs TV Shows')
axes[0].set_xlabel('Type')
axes[0].set_ylabel('Count')

# 2. Rating Distribution
axes[1].pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
axes[1].set_title('Content Rating Distribution')

# 3. Movie Duration Histogram
axes[2].hist(movie_df['duration_int'], bins=30, color='red', edgecolor='black')
axes[2].set_title('Distribution of Movie Durations')
axes[2].set_xlabel('Duration (minutes)')
axes[2].set_ylabel('Number of Movies')

# 4. Release Year Scatter
axes[3].scatter(release_counts.index, release_counts.values, color='orange')
axes[3].set_title('Content by Release Year')
axes[3].set_xlabel('Year')
axes[3].set_ylabel('Number of Titles')

# 5. Top 10 Countries
axes[4].barh(country_counts.index, country_counts.values, color='teal')
axes[4].set_title('Top 10 Countries')
axes[4].set_xlabel('Number of Titles')
axes[4].set_ylabel('Country')

# 6. Movies vs TV Shows Over Time
axes[5].plot(content_by_year.index, content_by_year['Movie'], label='Movies', color='blue')
axes[5].plot(content_by_year.index, content_by_year['TV Show'], label='TV Shows', color='red')
axes[5].set_title('Movies vs TV Shows Over the Years')
axes[5].set_xlabel('Year')
axes[5].set_ylabel('Count')
axes[5].legend()

# Adjust layout
plt.tight_layout()
plt.savefig("netflix_analysis_dashboard.png")
plt.show()
