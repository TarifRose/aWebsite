"""
from flask import Flask, request, jsonify, redirect, url_for, render_template

app = Flask(__name__)

key = {
    "admin": {"password": "123", "redirect": "mineui"},
    "twr": {"password": "321", "redirect": "mineui"}
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Incorrect Credentials'}), 400

    username = data['username']
    password = data['password']

    if username in key and key[username]['password'] == password:
        redirect_page = key[username]['redirect']
        return redirect(url_for(redirect_page))
    else:
        return jsonify({'message': 'Invalid user or password'}), 401

@app.route('/mineui')
def mineui():
    return render_template('mineui.html')

if __name__ == '__main__':
    app.run(debug=True)

    """
