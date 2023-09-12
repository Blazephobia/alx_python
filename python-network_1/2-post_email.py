import requests
import sys

# Check if the URL and email arguments are provided
if len(sys.argv) != 3:
    print("Usage: python script.py <URL> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary with the email parameter
data = {'email': email}

try:
    response = requests.post(url, data=data)

    # Check if the request was successful
    if response.status_code == 200:
        print(f'Your email is: {email}')
        print(f'Response body: {response.text}')
    else:
        print(f"Request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
