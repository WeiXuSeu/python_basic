from flask import Flask
from flask_httpauth import HTTPBasicAuth


app = Flask(__name__)
auth = HTTPBasicAuth()
users = [
    {'username': 'harvy', 'password': '123456'},
    {'username': 'Michael', 'password': '123456'}
]


@auth.get_password
def get_password(username):
    for user in users:
        if user['username'] == username:
            return user['password']
    return None


@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()


if __name__ == "__main__":
    app.run(debug=True)