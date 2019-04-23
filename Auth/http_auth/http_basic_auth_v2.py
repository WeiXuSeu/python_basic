from functools import wraps
from flask import request, Response,Flask
app = Flask(__name__)


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    try:
        return username == "harvy" and password == "111111"
    except Exception, e:
        return False


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response('Could not verify your access level for that URL.\n'
                    'You have to login with proper credentials', 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def basic_auth_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorator


@app.route('/')
@basic_auth_required
def show_user_profile():
    return 'open page!!'


if __name__ == "__main__":
    app.run(debug=True)

