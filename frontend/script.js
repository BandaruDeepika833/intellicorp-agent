async function sendMessage() {
    const input = document.getElementById("userInput");
    const message = input.value;
    input.value = "";

    addMessage(message, "user");

    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ user_id: "demo", message })
    });

    const data = await response.json();
    addMessage(JSON.stringify(data, null, 2), "bot");
}

function addMessage(text, sender) {
    const box = document.getElementById("chatbox");
    const msg = document.createElement("div");

    msg.className = sender === "user" ? "msg-user" : "msg-bot";
    msg.textContent = text;

    box.appendChild(msg);
    box.scrollTop = box.scrollHeight;
}
