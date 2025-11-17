async function sendMessage() {
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();
    const status = document.getElementById("status");

    if (!name || !email || !message) {
        status.innerHTML = "❌ All fields are required!";
        status.classList.add("text-red-400");
        return;
    }

    status.innerHTML = "⏳ Sending...";
    status.classList.remove("text-red-400");
    status.classList.add("text-yellow-300");

    const response = await fetch("/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, message })
    });

    const result = await response.json();

    if (result.status === "success") {
        status.innerHTML = "✅ Message sent successfully!";
        status.classList.remove("text-red-400", "text-yellow-300");
        status.classList.add("text-green-400");

        document.getElementById("name").value = "";
        document.getElementById("email").value = "";
        document.getElementById("message").value = "";

    } else {
        status.innerHTML = "❌ " + result.message;
        status.classList.remove("text-green-400", "text-yellow-300");
        status.classList.add("text-red-400");
    }
}
