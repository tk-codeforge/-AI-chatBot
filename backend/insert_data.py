from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["chatbot_db"]
collection = db["intents"]

data = [
    # Greeting
    {"text": "hello", "intent": "greeting"},
    {"text": "hi", "intent": "greeting"},
    {"text": "hey", "intent": "greeting"},
    {"text": "how are you", "intent": "greeting"},

    # Goodbye
    {"text": "bye", "intent": "goodbye"},
    {"text": "goodbye", "intent": "goodbye"},
    {"text": "see you later", "intent": "goodbye"},

    # Name
    {"text": "what is your name", "intent": "name"},
    {"text": "tell me your name", "intent": "name"},
    {"text": "who are you", "intent": "name"},
    {"text": "your name", "intent": "name"}
]


collection.insert_many(data)
print("Training data inserted!")
