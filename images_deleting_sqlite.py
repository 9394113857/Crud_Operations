import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('Images.db')
cur = conn.cursor()

# Delete an image by its ID
cur.execute('DELETE FROM images WHERE id = ?', (1,))
conn.commit()

# Close the database connection
conn.close()
