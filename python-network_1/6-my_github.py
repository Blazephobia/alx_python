import requests
import sys

# Check if the username and password arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
personal_access_token = sys.argv[2]

# Create a session with Basic Authentication
session = requests.Session()
session.auth = (username, personal_access_token)

try:
    # Make a GET request to the GitHub API to get user information
    response = session.get('https://api.github.com/user')

    # Check if the request was successful
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        print(user_id)
    else:
        print("None")
except requests.exceptions.RequestException as e:
    print("None")
