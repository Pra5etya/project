import nltk
from nltk.corpus import movie_reviews
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
import random

# Download dataset
nltk.download('movie_reviews')

def extract_features(words):
    return dict([(word, True) for word in words])

# Memuat ulasan dan labelnya
reviews = [(list(movie_reviews.words(fileid)), category)
           for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)]

# Mengacak data agar tidak berurutan
random.shuffle(reviews)

# Membagi data menjadi fitur dan label
featuresets = [(extract_features(review), category) for (review, category) in reviews]

# Membagi data menjadi training set dan test set
train_set, test_set = featuresets[:1600], featuresets[1600:]

# Melatih model NaiveBayesClassifier
classifier = NaiveBayesClassifier.train(train_set)

# Evaluasi model
print("Akurasi: ", accuracy(classifier, test_set))

# Contoh dataset film dan ulasan
movie_data = [
    {'title': 'Film A', 'genre': 'Action', 'review': 'This is a great action movie.'},
    {'title': 'Film B', 'genre': 'Comedy', 'review': 'This comedy movie is hilarious.'},
    {'title': 'Film C', 'genre': 'Drama', 'review': 'A touching drama with excellent performances.'},
    {'title': 'Film D', 'genre': 'Action', 'review': 'A thrilling action movie with non-stop excitement.'},
    {'title': 'Film E', 'genre': 'Comedy', 'review': 'A fun and entertaining comedy.'},
    {'title': 'Film F', 'genre': 'Drama', 'review': 'A dramatic storyline that keeps you hooked.'},
    # Tambahkan lebih banyak film dan ulasan jika diperlukan
]

# Function to get recommendations
def get_recommendations(genre, top_n=5):
    genre_movies = [movie for movie in movie_data if movie['genre'].lower() == genre.lower()]
    genre_movies_with_sentiment = []

    for movie in genre_movies:
        review_words = movie['review'].split()
        features = extract_features(review_words)
        sentiment = classifier.classify(features)
        genre_movies_with_sentiment.append((movie['title'], sentiment))

    # Sort by positive sentiment
    sorted_movies = sorted(genre_movies_with_sentiment, key=lambda x: x[1], reverse=True)
    return sorted_movies[:top_n]

# User interaction
user_genre = input("Masukkan genre yang Anda inginkan (misal: Action, Comedy, Drama): ")
recommendations = get_recommendations(user_genre)

print(f"Rekomendasi top {len(recommendations)} film dalam genre {user_genre}:")
for i, (title, sentiment) in enumerate(recommendations, start=1):
    print(f"{i}. {title} - Sentimen: {sentiment}")
