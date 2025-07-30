from flask import Flask, request, jsonify

app = Flask(__name__)


users={
    "admin":"tos",
    "usr": "usrprofile"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    #input validation
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Incorrect Credentials'}), 400 
    username = data['username']
    password = data['password']

    #auth
    if username in users and users[username] ==password:
        return jsonify({'message': 'Login Successful'}), 200 
    else:
        return jsonify({'message':'invalid user or password'}), 401 
    
    if __name__ =='__main__':
        app.run(debug=True)
