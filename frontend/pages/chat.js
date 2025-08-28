import { useState } from "react";

export default function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: "user", content: input };
    setMessages([...messages, userMessage]);
    setInput("");

    const res = await fetch("https://safespaceai.onrender.com/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ messages: [...messages, userMessage] }),
    });
    const data = await res.json();
    setMessages((prev) => [...prev, { role: "assistant", content: data.reply }]);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50 p-6">
      <h1 className="text-2xl font-bold mb-4">SafeSpace AI Chat</h1>
      <div className="w-full max-w-xl bg-white rounded-lg shadow p-4 mb-4 h-96 overflow-y-auto">
        {messages.map((m, i) => (
          <p key={i} className={m.role === "user" ? "text-right text-blue-600" : "text-left text-gray-800"}>
            <strong>{m.role === "user" ? "You" : "AI"}:</strong> {m.content}
          </p>
        ))}
      </div>
      <div className="flex w-full max-w-xl">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          className="flex-1 border rounded-l-lg p-2"
          placeholder="Type your message..."
        />
        <button onClick={sendMessage} className="px-4 bg-blue-600 text-white rounded-r-lg">Send</button>
      </div>
    </div>
  );
}
