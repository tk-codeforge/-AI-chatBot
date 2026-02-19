import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState([]);

  const sendMessage = async () => {
    if (!message) return;

    const userMessage = { sender: "User", text: message };
    setChat([...chat, userMessage]);

    const response = await axios.post("http://127.0.0.1:5000/chat", {
      message: message,
    });

    const botMessage = { sender: "Bot", text: response.data.reply };
    setChat(prevChat => [...prevChat, botMessage]);

    setMessage("");
  };

  return (
    <div className="container">
      <h2>Chatbot</h2>

      <div className="chat-box">
        {chat.map((msg, index) => (
          <div key={index} className={msg.sender === "User" ? "user" : "bot"}>
            <strong>{msg.sender}:</strong> {msg.text}
          </div>
        ))}
      </div>

      <div className="input-area">
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type message..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;
