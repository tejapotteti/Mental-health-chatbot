from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import nltk

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"  # needed for session handling

# Load chatbot dataset
df = pd.read_csv("chatbot.csv")

# Preprocess function
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word not in string.punctuation]
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    return ' '.join(tokens)

# Route: Login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Validate user against SQLite
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session["username"] = username
            return redirect(url_for("chat"))
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return render_template("signup.html", error="Passwords do not match")

        # Check if username already exists
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = c.fetchone()
        if existing_user:
            conn.close()
            return render_template("signup.html", error="Username already exists")

        # Insert new user
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        return render_template("signup.html", success="Account created successfully! You can now log in.")

    return render_template("signup.html")


# Route: Chat page
@app.route("/chat", methods=["GET", "POST"])
def chat():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        user_input = request.form["message"]
        response = get_response(user_input)
        return {"response": response}

    return render_template("chat.html", username=session["username"])

# Chatbot logic
def get_response(user_input):
    user_input_processed = preprocess_text(user_input)
    # Try to find a close match
    for i, row in df.iterrows():
        if user_input_processed in preprocess_text(row["user_input"]):
            return row["chatbot_response"]
    return "I'm not sure how to respond to that, but I'm here to help!"

# Run app
if __name__ == "__main__":
    app.run(debug=True)
