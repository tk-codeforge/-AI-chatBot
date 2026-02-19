from pymongo import MongoClient
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["chatbot_db"]
collection = db["intents"]

# Fetch training data
data = list(collection.find({}, {"_id": 0}))

texts = [item["text"] for item in data]
labels = [item["intent"] for item in data]

# Convert text to numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# Save model and vectorizer
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved successfully!")
