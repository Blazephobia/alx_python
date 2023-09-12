import requests
import sys

# Check if the URL argument is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)

    # Check if the 'X-Request-Id' header is present in the response
    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
    else:
        print("The 'X-Request-Id' header is not present in the response.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
