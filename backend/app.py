from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# MongoDB connection (for chat logs)
client = MongoClient("mongodb://localhost:27017/")
db = client["chatbot_db"]
logs_collection = db["chat_logs"]

def get_response(intent):
    responses = {
        "greeting": "Hello! How can I help you?",
        "goodbye": "Goodbye! Have a nice day!",
        "name": "I am an AI chatbot."
    }
    return responses.get(intent, "Sorry, I don't understand.")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    # Transform input
    X_input = vectorizer.transform([user_message])

    # Predict intent
    predicted_intent = model.predict(X_input)[0]

    bot_reply = get_response(predicted_intent)

    # Save chat log in MongoDB
    logs_collection.insert_one({
        "user_message": user_message,
        "bot_reply": bot_reply
    })

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
