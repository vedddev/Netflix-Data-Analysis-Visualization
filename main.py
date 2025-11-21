import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

# Load data
path = "F:\\Data sciance\\Project\\netflix_titles.csv"
data = pd.read_csv(path)

# Drop rows with missing important values
df = data.dropna(subset=['type','release_year','rating','country','duration'])

# Movies vs TV Shows
type_counts = df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index, type_counts.values, color=['skyblue','orange'])
plt.title('Number of Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()

# Content Rating Distribution
rating_counts = df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts.values, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Content Rating Distribution')
plt.tight_layout()
plt.savefig('Content_rating.png')
plt.show()

# Movie Duration Distribution
movie_df = df[df['type']=='Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace(' min','').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'], bins=30, color='red', edgecolor='black')
plt.title('Distribution of Movie Durations')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('Duration.png')
plt.show()

# Release Year Distribution
release_counts = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index, release_counts.values, color='orange')
plt.title('Distribution of Netflix Content by Release Year')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows/Movies')
plt.tight_layout()
plt.savefig('Release_Year.png')
plt.show()

# Top 10 Countries
country_counts = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_counts.index, country_counts.values, color='teal')
plt.title('Top 10 Countries by Number of Shows/Movies')
plt.xlabel('Number of Shows/Movies')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('top10_movies.png')
plt.show()

# Movies vs TV Shows over the Years
content_by_year = df.groupby(['release_year','type']).size().unstack().fillna(0)

fig, ax = plt.subplots(1,2,figsize=(12,5))

# Movies
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number of Movies')

# TV Shows
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='red')
ax[1].set_title('TV Shows Released Per Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV Shows')

fig.suptitle('Comparison: Movies vs TV Shows', fontsize=14)

plt.tight_layout()
plt.savefig('comparison.png')
plt.show()

