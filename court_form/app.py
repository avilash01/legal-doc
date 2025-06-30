from flask import Flask, render_template, request, send_file
import sqlite3
from generate_doc import create_affidavit_doc

app = Flask(__name__)
DB_NAME = "court.db"

# Create table on startup
def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS affidavits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            court TEXT, location TEXT, ia_no TEXT, op_no TEXT,
            petitioner TEXT, respondent TEXT, petitioner_son_of TEXT,
            occupation TEXT, age TEXT, address TEXT, date TEXT, place TEXT
        )''')

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {key: request.form[key] for key in [
        'court', 'location', 'ia_no', 'op_no', 'petitioner',
        'respondent', 'petitioner_son_of', 'occupation', 'age',
        'address', 'date', 'place'
    ]}

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''INSERT INTO affidavits (
            court, location, ia_no, op_no,
            petitioner, respondent, petitioner_son_of,
            occupation, age, address, date, place
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', tuple(data.values()))

    output_path = create_affidavit_doc(data)
    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
