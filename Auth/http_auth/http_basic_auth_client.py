import requests


def http_basic_auth_request():
    request_url = "http://127.0.0.1:5000/"
    queryUsername = "harvy"
    queryPassword = "333333"
    try:
        response = requests.get(request_url, auth=(queryUsername, queryPassword), verify=False)
        status_code = response.status_code
        if status_code != 200:
            return False
        else:
            return True
    except Exception, e:
        return True


if __name__ == "__main__":
    http_basic_auth_request()