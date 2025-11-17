from flask import Flask, request, jsonify, render_template
import smtplib
import ssl

app = Flask(__name__, template_folder="template",static_folder="static")

# -------- EMAIL CONFIGURATION --------
SENDER_EMAIL = "muhammedtesleemolatundun@gmail.com"
SENDER_PASSWORD = "dovu gewv whvk raqu"   # Gmail App Password
RECEIVER_EMAIL = "muhammedtesleemolatundun@gmail.com"


@app.route("/")
def home():
    return render_template("index.html")  # load your portfolio


@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if not name or not email or not message:
        return jsonify({"status": "error", "message": "All fields are required!"})

    # ----- Email Formatting -----
    email_message = f"""
    New Portfolio Contact Message

    Name: {name}
    Email: {email}

    Message:
    {message}
    """

    # ----- Sending Email -----
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, email_message)

        return jsonify({"status": "success", "message": "Message sent successfully!"})

    except Exception as e:
        return jsonify({"status": "error", "message": f"Failed to send: {str(e)}"})


if __name__ == "__main__":
    app.run(debug=True)
