import requests
import sys

# Check if the URL argument is provided
if len(sys.argv) != 2:
    print("Usage: python script.py <URL>")
    sys.exit(1)

url = sys.argv[1]

try:
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Check if the 'X-Request-Id' header is present in the response
        if 'X-Request-Id' in response.headers:
            x_request_id = response.headers['X-Request-Id']
            print(f'X-Request-Id: {x_request_id}')
        else:
            print("The 'X-Request-Id' header is not present in the response.")
    else:
        print(f"Request failed with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")