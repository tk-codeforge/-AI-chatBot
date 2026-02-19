# 🤖 AI Chatbot (React + Flask + MongoDB)

An AI-powered chatbot application built using React for frontend and Flask for backend, with MongoDB as the database.

---

## 🚀 Features

- Interactive chatbot UI
- Flask REST API backend
- MongoDB database integration
- Dynamic response generation
- Clean and modular project structure

---

## 🛠️ Tech Stack

Frontend:
- React.js
- Axios
- CSS

Backend:
- Flask
- Flask-CORS
- PyMongo

Database:
- MongoDB

---

## 📂 Project Structure

```bash
chatbot-project/
│
├── backend/
│   ├── app.py
│   ├── insert_data.py
│   ├── requirements.txt
│   ├── models/
│   └── venv/   (ignored)
│
├── frontend/
│   ├── package.json
│   ├── package-lock.json
│   ├── public/
│   └── src/
│       ├── components/
│       ├── App.js
│       └── index.js
│
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 🔹 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd chatbot-project
```

---

### 🔹 2️⃣ Backend Setup (Flask)

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python app.py
```

Backend will run on:
```
http://127.0.0.1:5000
```

---

### 🔹 3️⃣ Frontend Setup (React)

```bash
cd frontend
npm install
npm start
```

Frontend will run on:
```
http://localhost:3000
```

---

## 🔐 Environment Variables

Create a `.env` file in backend:

```
MONGO_URI=your_mongodb_connection_string
```

---

## 📌 API Endpoint

| Method | Endpoint | Description |
|--------|----------|------------|
| POST   | /chat    | Send user message and receive bot response |

---

## 🧠 Future Improvements

- Add authentication
- Integrate AI models
- Deploy on cloud (AWS / Render / Vercel)
- Improve NLP response handling

---

## 👨‍💻 Author

Tanmay Kumar

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!

