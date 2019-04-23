#!/usr/bin/env python
"""Basic authentication example
This example demonstrates how to protect Flask endpoints with basic
authentication, using secure hashed passwords.
After running this example, visit http://localhost:5000 in your browser. To
gain access, you can use (username=john, password=hello) or
(username=susan, password=bye).
"""
from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

"""
users = {
    "harvy": generate_password_hash("333333"),
    "susan": generate_password_hash("bye")
}
"""

users = {'harvy': 'pbkdf2:sha256:150000$vke2Ra1U$e84f8d8008defb565df7aa574d8e1fa7bdb94c91b253986956f36b3bc9462c41',
 'susan': 'pbkdf2:sha256:150000$SZMtW6Ed$b03eea611d8cdddd2a06fa188a18e802496d5dc94815ed113802aa3b9bb4f5a3'}


@auth.verify_password
def verify_password(username, password):
    if username in users:
        return check_password_hash(users.get(username), password)
    return False


@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()


if __name__ == '__main__':
    app.run(debug=True)
