import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Images.db')
cur = conn.cursor()

# Create a table for the images
cur.execute('''
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        image BLOB
    )
''')

# Open the image file and read its contents
# with open('image.jpg', 'rb') as f:
#     image_data = f.read()

# Insert the image into the database
# cur.execute('INSERT INTO images (name, image) VALUES (?, ?)', ('image.jpg', image_data))
# conn.commit()

# Close the database connection
conn.close()
