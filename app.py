from flask import Flask
import mysql.connector
app = Flask(__name__)
@app.route('/')
def home():
    
 # Connect to MySQL/MariaDB#
    conn = mysql.connector.connect(
        host="localhost",
        user="exampleuser",
        password="salasana123",
        database="exampledb"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from MySQL!'")
    result = cursor.fetchone()

# Clean up
    cursor.close()
    conn.close()
    return f"<h1>{result[0]}</h1>"
if __name__ == '__name__':
    app.run(host='0.0.0.0', port=5000)
