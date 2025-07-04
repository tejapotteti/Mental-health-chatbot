#  Mental and Health Assistance Chatbot

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A friendly, easy-to-use chatbot that provides support for mental wellness and common health questions.  
Built with **Python**, **Flask**, **HTML/CSS**, and **NLTK** for natural language processing.

---

##  Features

✅ User authentication (Login)  
✅ Rich CSV knowledge base (mental health + health FAQs)  
✅ Guided suggestions for user queries  
✅ Clean HTML/CSS frontend with pink theme  
✅ "Back to Main Menu" button and chat command  
✅ Fallback responses with helpful examples  
✅ Ready for deployment on Render or other cloud platforms  

---



### Clone the repository

```bash
git clone https://github.com/tejapotteti/mental-health-chatbot.git
cd mental-health-chatbot
```

---

### Install dependencies

Make sure you have **Python 3.8+** installed.

Install required Python packages:

```bash
pip install -r requirements.txt
```

---

### Start the application

```bash
python app.py
```

---

### Open in your browser

```
http://127.0.0.1:5000/
```

✅ Login with your credentials and start chatting!

---

##  Example Questions to Try

Here are some example phrases you can type:

- **hi**
- **I feel sad**
- **I have fever**
- **I am stressed**
- **I can’t sleep**
- **I feel lonely**
- **I need motivation**
- **I have headache**
- **what is depression**
- **how to boost immunity**

---

##  How It Works

- The chatbot loads a **CSV file of pre-defined question-response pairs**.
- User messages are preprocessed with **NLTK** (tokenization, stop words removal, lemmatization).
- The chatbot uses **cosine similarity** to find the best match response.
- If no match is found, it shows a fallback message.
- A friendly **HTML/CSS frontend** is used for interaction.

---

##  Future Enhancements

✅ Add GPT or other AI integration for dynamic answers  
✅ Improve spelling correction and fuzzy matching  
✅ Add user registration and history tracking  
✅ Dockerize for easier deployment  

---

## Project Structure

```
mental-health-chatbot/
├── app.py                 # Main Flask application
├── chatbot.csv            # Knowledge base of questions and answers
├── create_database.py     # Script to create SQLite DB
├── display_users.py       # Script to display users
├── users.db               # SQLite database
├── templates/
│   ├── login.html         # Login page
│   ├── signup.html        # Signup page
│   └── chat.html          # Chat interface
├── static/
│   └── styles.css         # Stylesheet
└── README.md              # Project documentation
```

---

##  Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

##  License

This project is licensed under the MIT License.

---

##  Live Demo

*([Live Link](https://mental-health-chatbot-8ehv.onrender.com/))*

---
