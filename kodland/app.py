from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'super_tajny_klucz_hackathon_v2'

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, email TEXT, password_hash TEXT, points INTEGER DEFAULT 0)''')
    c.execute('''CREATE TABLE IF NOT EXISTS results (id INTEGER PRIMARY KEY, user_id INTEGER, score REAL, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

init_db()

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html', active_page='index')

@app.route('/kalkulator', methods=['GET', 'POST'])
def kalkulator():
    if request.method == 'POST':
        if 'user_id' in session:
            score = float(request.json['score'])
            conn = get_db()
            conn.execute("INSERT INTO results (user_id, score) VALUES (?, ?)", (session['user_id'], score))
            conn.commit()
            conn.close()
            return jsonify({"status": "zapisano"})
        return jsonify({"status": "niezalogowany"})
    return render_template('kalkulator.html', active_page='kalkulator')

@app.route('/ankiety')
def ankiety():
    return render_template('ankiety.html', active_page='ankiety')


@app.route('/glosuj', methods=['POST'])
def glosuj():
    if 'user_id' in session:
        conn = get_db()
        conn.execute("UPDATE users SET points = points + 50 WHERE id = ?", (session['user_id'],))
        conn.commit()
        conn.close()
        return jsonify({"status": "sukces", "msg": "Dodano +50 Eco-Punktów!"})
    return jsonify({"status": "niezalogowany", "msg": "Zaloguj się, aby otrzymać punkty!"})

@app.route('/narzedzia')
def narzedzia():
    return render_template('narzedzia.html', active_page='narzedzia')

@app.route('/kontakt')
def kontakt():
    return render_template('kontakt.html', active_page='kontakt')

@app.route('/profil', methods=['GET', 'POST'])
def profil():
    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = get_db()
        if action == 'register':
            email = request.form.get('email')
            password_confirm = request.form.get('password_confirm')
            
            if password != password_confirm:
                flash("Hasła nie są identyczne!", "error")
                return redirect(url_for('profil'))
                
            hashed_pw = generate_password_hash(password)
            try:
                conn.execute("INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)", (username, email, hashed_pw))
                conn.commit()
                flash("Konto utworzone! Możesz się teraz zalogować.", "success")
            except sqlite3.IntegrityError:
                flash("Taki użytkownik już istnieje!", "error")
                
        elif action == 'login':
            user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
            if user and check_password_hash(user['password_hash'], password):
                session['user_id'] = user['id']
                session['username'] = user['username']
                flash("Zalogowano pomyślnie!", "success")
            else:
                flash("Błędny login lub hasło.", "error")
                
        conn.close()
        return redirect(url_for('profil'))

    if 'user_id' in session:
        conn = get_db()
        user_data = conn.execute("SELECT points FROM users WHERE id = ?", (session['user_id'],)).fetchone()
        points = user_data['points'] if user_data else 0
        best_score = conn.execute("SELECT MIN(score) as min_score FROM results WHERE user_id = ?", (session['user_id'],)).fetchone()['min_score']
        conn.close()
        return render_template('profil.html', active_page='profil', best_score=best_score, points=points)
        
    return render_template('logowanie.html', active_page='profil')

@app.route('/wyloguj')
def wyloguj():
    session.clear()
    return redirect(url_for('profil'))

if __name__ == '__main__':
    app.run(debug=True)