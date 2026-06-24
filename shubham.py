import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Dataset
df = pd.read_csv("movies.csv")

# Keep Required Columns
df = df[['title', 'genres']]

# Check Data
print("Shape:", df.shape)

# Convert Genres into Numerical Features
cv = CountVectorizer(stop_words='english')

genre_matrix = cv.fit_transform(df['genres'])

print("Genre Matrix Shape:", genre_matrix.shape)

# Calculate Similarity
similarity = cosine_similarity(genre_matrix)

print("Similarity Matrix Shape:", similarity.shape)


# Recommendation Function
def recommend(movie_name):

    movie_index = df[df['title'] == movie_name].index

    if len(movie_index) == 0:
        print("Movie not found!")
        return

    movie_index = movie_index[0]

    distances = similarity[movie_index]

    movies = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    print("\nRecommended Movies:\n")

    for movie in movies:
        print(df.iloc[movie[0]]['title'])


# Show Some Movie Names
print("\nSample Movies:")
print(df['title'].head(10).to_list())

# Test Recommendation
recommend("GoldenEye (1995)")