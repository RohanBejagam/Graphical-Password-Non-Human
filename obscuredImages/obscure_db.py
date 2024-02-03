import hashlib
import sqlite3
import os


conn = sqlite3.connect("obscure_db.db")
cursor = conn.cursor()

print('Database created')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS garbled_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        original_text TEXT
    )
''')

conn.commit()
print('Table Created')

def insert_data(filename, original_obscure):
    # Insert data into the table
    cursor.execute('INSERT INTO garbled_table (filename, original_obscure) VALUES (?, ?)', (filename, original_obscure))
    
image_folder = 'C:/Users/91970/Desktop/major/Graphical-Passoword-Non-Human/obscureImages'

# Iterate through each file in the folder
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust file extensions as needed
        # You may want to extract original_text from the file or provide a default value
        base_name, extension = os.path.splitext(filename)
        original_text = base_name
        # h = hashlib.new('sha512_256') 
        # h.update(base_name.encode())
        # original_text = h.hexdigest()
        # Insert data into the authentication_info table
        insert_data(filename, original_obscure)

print('Data filled successfully...')   
conn.commit()
conn.close()