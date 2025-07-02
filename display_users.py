import sqlite3

# Connect to the database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Fetch all rows from the users table
c.execute("SELECT * FROM users")
rows = c.fetchall()

# Display the contents of the users table
for row in rows:
    print(row)

# Close the connection
conn.close()
