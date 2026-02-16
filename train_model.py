import pandas as pd
import re
import pickle
import nltk
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

nltk.download('stopwords')

print("Loading dataset...")
df = pd.read_csv("IMDB Dataset.csv")

# Text cleaning function
def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower()
    return text

print("Cleaning text...")
df['review'] = df['review'].apply(clean_text)

# Convert sentiment to numbers
df['sentiment'] = df['sentiment'].map({'positive':1, 'negative':0})

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    df['review'], df['sentiment'], test_size=0.2, random_state=42
)

# TF-IDF
print("Vectorizing text...")
vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train model
print("Training model...")
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Evaluate model
print("Evaluating model...")
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)
print(f"\nModel Accuracy: {accuracy*100:.2f}%\n")
print(classification_report(y_test, predictions))

# Save model
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("\nModel and Vectorizer saved successfully ✅")
