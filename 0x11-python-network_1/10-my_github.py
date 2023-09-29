#!/usr/bin/python3
"""
This that takes your GitHub credentials
(username and password) and uses the GitHub
API to display your id

"""


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <username> \
            <personal_access_token>".format(sys.argv[0]))
        sys.exit(1)
    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    url = "https://api.github.com/user"
    auth = (username, personal_access_token)
    response = requests.get(url, auth=auth)
    try:
        user_info = response.json()
        if "id" in user_info:
            print(user_info["id"])
        else:
            print("None")
    except ValueError:
        print("None")
