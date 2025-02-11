import sqlite3
import json

# Connect to database (creates file if not exists)
conn = sqlite3.connect('patient_data.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS PatientData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data JSON
    )
''')

def store_data(json_data):
    """Insert JSON data into SQLite database."""
    cursor.execute("INSERT INTO PatientData (data) VALUES (?)", (json.dumps(json_data),))
    conn.commit()

# Load extracted JSON
with open("output.json", "r") as json_file:
    data = json.load(json_file)

store_data(data)
print("Data stored successfully in SQLite!")
