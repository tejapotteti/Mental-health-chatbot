import sqlite3

# Connect to the database 
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create the users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE,
                password TEXT
            )''')

# Insert user data
users_data = [
    ('Vamsi', 'AP844'),
    ('Hitesh', 'AP787'),
    ('Teja', 'AP236'),
    ('Vishnu', 'AP845'),
    ('Nanda', 'AP826'),
    # Add data for the remaining users...
]

# Insert each user data, checking for duplicates
for username, password in users_data:
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    except sqlite3.IntegrityError:
        print(f"Username '{username}' already exists, skipping insertion.")

# Commit changes and close the connection
conn.commit()
conn.close()
